from datetime import datetime, timezone
from typing import Annotated
from uuid import uuid4

import hmac
import jwt
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from .database import get_db
from .dependencies import get_current_auth_session, get_current_user, unauthorized
from .models import AuthSession, User
from .schemas import (
    LoginRequest,
    RefreshRequest,
    RegisterRequest,
    TokenResponse,
    UserResponse,
)
from .security import (
    ACCESS_TOKEN_MINUTES,
    create_session_tokens,
    decode_token,
    hash_password,
    hash_refresh_token,
    verify_password,
)

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)
def register(
    payload: RegisterRequest,
    db: Annotated[Session, Depends(get_db)],
) -> User:
    user = User(
        name=payload.name,
        email=str(payload.email).lower(),
        age=payload.age,
        is_active=True,
        password_hash=hash_password(payload.password),
        role="student",
    )
    db.add(user)
    try:
        db.commit()
        db.refresh(user)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="A user with this email already exists.",
        ) from None
    return user


@router.post("/login", response_model=TokenResponse)
def login(
    payload: LoginRequest,
    db: Annotated[Session, Depends(get_db)],
) -> TokenResponse:
    user = db.scalar(select(User).where(User.email == str(payload.email).lower()))
    if (
        user is None
        or not user.is_active
        or not verify_password(payload.password, user.password_hash)
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password.",
            headers={"WWW-Authenticate": "Bearer"},
        )

    session_id = str(uuid4())
    access_token, refresh_token, expires_at = create_session_tokens(
        user.id, session_id
    )
    db.add(
        AuthSession(
            id=session_id,
            user_id=user.id,
            refresh_token_hash=hash_refresh_token(refresh_token),
            expires_at=expires_at,
        )
    )
    db.commit()
    return TokenResponse(
        access_token=access_token,
        refresh_token=refresh_token,
        expires_in=ACCESS_TOKEN_MINUTES * 60,
        user=user,
    )


@router.post("/refresh", response_model=TokenResponse)
def refresh(
    payload: RefreshRequest,
    db: Annotated[Session, Depends(get_db)],
) -> TokenResponse:
    try:
        claims = decode_token(payload.refresh_token, "refresh")
        user_id = int(str(claims["sub"]))
        session_id = str(claims["sid"])
    except (jwt.InvalidTokenError, KeyError, TypeError, ValueError):
        raise unauthorized() from None

    auth_session = db.scalar(
        select(AuthSession)
        .where(AuthSession.id == session_id)
        .with_for_update()
    )
    now = datetime.now(timezone.utc)
    if (
        auth_session is None
        or auth_session.user_id != user_id
        or auth_session.revoked_at is not None
        or _as_utc(auth_session.expires_at) <= now
        or not _constant_time_hash_match(
            payload.refresh_token, auth_session.refresh_token_hash
        )
    ):
        raise unauthorized()

    user = db.get(User, user_id)
    if user is None or not user.is_active:
        raise unauthorized()

    access_token, refresh_token, expires_at = create_session_tokens(
        user.id, session_id
    )
    auth_session.refresh_token_hash = hash_refresh_token(refresh_token)
    auth_session.expires_at = expires_at
    db.commit()
    return TokenResponse(
        access_token=access_token,
        refresh_token=refresh_token,
        expires_in=ACCESS_TOKEN_MINUTES * 60,
        user=user,
    )


@router.post("/logout", status_code=status.HTTP_204_NO_CONTENT)
def logout(
    auth_session: Annotated[AuthSession, Depends(get_current_auth_session)],
    db: Annotated[Session, Depends(get_db)],
) -> None:
    auth_session.revoked_at = datetime.now(timezone.utc)
    db.commit()


@router.get("/me", response_model=UserResponse)
def read_me(
    user: Annotated[User, Depends(get_current_user)],
) -> User:
    return user


def _as_utc(value: datetime) -> datetime:
    if value.tzinfo is None:
        return value.replace(tzinfo=timezone.utc)
    return value.astimezone(timezone.utc)


def _constant_time_hash_match(token: str, token_hash: str) -> bool:
    return hmac.compare_digest(hash_refresh_token(token), token_hash)
