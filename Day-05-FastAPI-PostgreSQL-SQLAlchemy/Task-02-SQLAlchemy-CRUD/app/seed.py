import os

from pydantic import EmailStr, TypeAdapter, ValidationError
from sqlalchemy import select

from .database import SessionLocal
from .models import User
from .security import hash_password

email_adapter = TypeAdapter(EmailStr)


def main() -> None:
    teacher_email, teacher_password = _required_credentials("TEACHER")
    student_email, student_password = _required_credentials("STUDENT")

    users = (
        ("teacher", teacher_email, teacher_password, "Seed Teacher"),
        ("student", student_email, student_password, "Seed Student"),
    )
    with SessionLocal() as db:
        for role, email, password, name in users:
            user = db.scalar(select(User).where(User.email == email))
            if user is None:
                db.add(
                    User(
                        name=name,
                        email=email,
                        password_hash=hash_password(password),
                        role=role,
                        is_active=True,
                    )
                )
            elif user.role != role:
                raise RuntimeError(
                    f"{email} already exists with role {user.role!r}; "
                    "correct the seed configuration or existing account."
                )
        db.commit()
    print("Teacher and student seed accounts are ready.")


def _required_credentials(role: str) -> tuple[str, str]:
    prefix = f"SEED_{role}"
    email = os.getenv(f"{prefix}_EMAIL", "").strip().lower()
    password = os.getenv(f"{prefix}_PASSWORD", "")
    if not email or not password:
        raise RuntimeError(f"Set {prefix}_EMAIL and {prefix}_PASSWORD before seeding.")
    try:
        email = str(email_adapter.validate_python(email)).lower()
    except ValidationError as error:
        raise RuntimeError(f"{prefix}_EMAIL must be a valid email address.") from error
    if len(password) < 8 or len(password) > 128:
        raise RuntimeError(f"{prefix}_PASSWORD must contain 8 to 128 characters.")
    return email, password


if __name__ == "__main__":
    main()
