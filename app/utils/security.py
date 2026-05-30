import hashlib

import bcrypt
from jose import jwt

from datetime import datetime, timedelta

from app.config import settings


PASSWORD_HASH_PREFIX = "sha256_bcrypt$"


def prepare_password(password: str):
    return hashlib.sha256(
        password.encode("utf-8")
    ).hexdigest().encode("ascii")


def hash_password(password: str):

    password_hash = bcrypt.hashpw(
        prepare_password(password),
        bcrypt.gensalt()
    ).decode("utf-8")

    return f"{PASSWORD_HASH_PREFIX}{password_hash}"


def verify_password(
    plain_password: str,
    hashed_password: str
):

    if hashed_password.startswith(PASSWORD_HASH_PREFIX):
        stored_hash = hashed_password.removeprefix(
            PASSWORD_HASH_PREFIX
        ).encode("utf-8")

        return bcrypt.checkpw(
            prepare_password(plain_password),
            stored_hash
        )

    try:
        return bcrypt.checkpw(
            plain_password.encode("utf-8"),
            hashed_password.encode("utf-8")
        )
    except ValueError:
        return False


def create_access_token(data: dict):

    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(
        minutes=settings.access_token_expire_minutes
    )

    to_encode.update({"exp": expire})

    return jwt.encode(
        to_encode,
        settings.secret_key,
        algorithm=settings.algorithm
    )
