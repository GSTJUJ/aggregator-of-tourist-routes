from fastapi import APIRouter, HTTPException
from fastapi.responses import HTMLResponse
from sqlalchemy import text

from app.database.database import SessionLocal

from app.schemas.user import (
    UserCreate,
    UserLogin
)

from app.utils.security import (
    hash_password,
    verify_password,
    create_access_token
)

router = APIRouter()


@router.get(
    "/register-page",
    response_class=HTMLResponse
)
def register_page():
    with open(
        "app/templates/register.html",
        "r",
        encoding="utf-8"
    ) as file:
        return file.read()


@router.post("/register")
def register(user: UserCreate):
    db = SessionLocal()

    try:
        hashed_password = hash_password(
            user.password
        )

        query = """
        INSERT INTO users
        (full_name, phone, email, region, password)

        VALUES
        (:full_name, :phone, :email, :region, :password)
        """

        db.execute(
            text(query),
            {
                "full_name": user.full_name,
                "phone": user.phone,
                "email": user.email,
                "region": user.region,
                "password": hashed_password
            }
        )

        db.commit()

        return {
            "message": "Пользователь зарегистрирован"
        }

    except Exception as e:
        db.rollback()

        return {
            "error": str(e)
        }

    finally:
        db.close()


@router.post("/login")
def login(user: UserLogin):
    db = SessionLocal()

    result = db.execute(
        text(
            "SELECT * FROM users WHERE email = :email"
        ),
        {"email": user.email}
    ).fetchone()

    if not result:
        db.close()

        raise HTTPException(
            status_code=404,
            detail="Пользователь не найден"
        )

    if not verify_password(
        user.password,
        result.password
    ):
        db.close()

        raise HTTPException(
            status_code=401,
            detail="Неверный пароль"
        )

    token = create_access_token({
        "sub": str(result.user_id)
    })

    db.close()

    return {
        "access_token": token,
        "token_type": "bearer"
    }