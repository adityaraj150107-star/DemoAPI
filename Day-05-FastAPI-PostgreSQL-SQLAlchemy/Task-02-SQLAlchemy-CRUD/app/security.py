import hashlib
import os
from datetime import datetime, timedelta, timezone
from uuid import uuid4

import jwt
from pwdlib import PasswordHash

JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
if (
    not JWT_SECRET_KEY
    or len(JWT_SECRET_KEY.encode("utf-8")) < 32
    or JWT_SECRET_KEY.startswith("replace-with-")
):
    raise RuntimeError("JWT_SECRET_KEY must contain at least 32 bytes.")

JWT_ALGORITHM = "HS256"
ACCESS_TOKEN_MINUTES = int(os.getenv("ACCESS_TOKEN_MINUTES", "15"))
REFRESH_TOKEN_DAYS = int(os.getenv("REFRESH_TOKEN_DAYS", "7"))
if ACCESS_TOKEN_MINUTES < 1 or REFRESH_TOKEN_DAYS < 1:
    raise RuntimeError("Token lifetimes must be positive integers.")

password_hasher = PasswordHash.recommended()


def hash_password(password: str) -> str:
    return password_hasher.hash(password)


def verify_password(password: str, password_hash: str) -> bool:
    if password_hash == "!":
        return False
    return password_hasher.verify(password, password_hash)


def hash_refresh_token(token: str) -> str:
    return hashlib.sha256(token.encode("utf-8")).hexdigest()


def create_session_tokens(user_id: int, session_id: str) -> tuple[str, str, datetime]:
    now = datetime.now(timezone.utc)
    access_expires_at = now + timedelta(minutes=ACCESS_TOKEN_MINUTES)
    refresh_expires_at = now + timedelta(days=REFRESH_TOKEN_DAYS)
    access_token = jwt.encode(
        {
            "sub": str(user_id),
            "sid": session_id,
            "type": "access",
            "iat": now,
            "exp": access_expires_at,
        },
        JWT_SECRET_KEY,
        algorithm=JWT_ALGORITHM,
    )
    refresh_token = jwt.encode(
        {
            "sub": str(user_id),
            "sid": session_id,
            "type": "refresh",
            "jti": uuid4().hex,
            "iat": now,
            "exp": refresh_expires_at,
        },
        JWT_SECRET_KEY,
        algorithm=JWT_ALGORITHM,
    )
    return access_token, refresh_token, refresh_expires_at


def decode_token(token: str, expected_type: str) -> dict[str, object]:
    claims = jwt.decode(
        token,
        JWT_SECRET_KEY,
        algorithms=[JWT_ALGORITHM],
        options={"require": ["exp", "sub", "sid", "type"]},
    )
    if claims.get("type") != expected_type:
        raise jwt.InvalidTokenError("Unexpected token type.")
    return claims
