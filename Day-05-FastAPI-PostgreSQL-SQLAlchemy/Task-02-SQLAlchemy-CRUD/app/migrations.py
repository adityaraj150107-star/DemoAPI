from sqlalchemy import inspect, text

from .database import engine


def migrate_legacy_users() -> None:
    columns = {column["name"] for column in inspect(engine).get_columns("users")}
    with engine.begin() as connection:
        if "password_hash" not in columns:
            connection.execute(
                text(
                    "ALTER TABLE users ADD COLUMN password_hash "
                    "VARCHAR(255) NOT NULL DEFAULT '!'"
                )
            )
            connection.execute(
                text("ALTER TABLE users ALTER COLUMN password_hash DROP DEFAULT")
            )
        if "role" not in columns:
            connection.execute(
                text(
                    "ALTER TABLE users ADD COLUMN role "
                    "VARCHAR(20) NOT NULL DEFAULT 'student'"
                )
            )
            connection.execute(text("ALTER TABLE users ALTER COLUMN role DROP DEFAULT"))
