from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy import text

from app.database.database import SessionLocal
from app.config import settings

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/login"
)


def get_db():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


def get_current_user(
    token: str = Depends(oauth2_scheme)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Не удалось проверить токен",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(
            token,
            settings.secret_key,
            algorithms=[settings.algorithm]
        )

        user_id = payload.get("sub")

        if user_id is None:
            raise credentials_exception

    except JWTError:
        raise credentials_exception

    db = SessionLocal()

    result = db.execute(
        text(
            "SELECT * FROM users WHERE id = :user_id"
        ),
        {"user_id": int(user_id)}
    ).fetchone()

    db.close()

    if result is None:
        raise credentials_exception

    return result
    
