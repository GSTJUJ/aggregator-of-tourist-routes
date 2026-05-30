from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy import inspect, text
from sqlalchemy.exc import IntegrityError

from app.database.database import SessionLocal
from app.schemas.user import UserCreate, UserLogin
from app.utils.dependencies import get_current_user
from app.utils.security import create_access_token, hash_password, verify_password


router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


def create_user_token(user_id: int):
    return create_access_token({"sub": str(user_id)})


def get_user_columns(db):
    return {
        column["name"]
        for column in inspect(db.get_bind()).get_columns("users")
    }


@router.get("/register-page", response_class=HTMLResponse)
def register_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="register.html"
    )


@router.get("/login-page", response_class=HTMLResponse)
def login_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="login.html"
    )


@router.get("/profile", response_class=HTMLResponse)
def profile_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="profile.html"
    )


@router.get("/me")
def me(current_user=Depends(get_current_user)):
    user = current_user._mapping

    return {
        "id": user["id"],
        "full_name": user.get("full_name") or user.get("username") or "",
        "phone": user.get("phone") or "",
        "email": user["email"],
        "region": user.get("region") or "",
    }


@router.post("/register")
def register(user: UserCreate):
    db = SessionLocal()

    try:
        hashed_password = hash_password(user.password)

        columns = get_user_columns(db)
        values = {
            "email": user.email,
        }

        if "full_name" in columns:
            values["full_name"] = user.full_name
        if "phone" in columns:
            values["phone"] = user.phone
        if "region" in columns:
            values["region"] = user.region
        if "password" in columns:
            values["password"] = hashed_password
        if "username" in columns:
            values["username"] = user.email
        if "hashed_password" in columns:
            values["hashed_password"] = hashed_password

        column_names = ", ".join(values.keys())
        placeholders = ", ".join(f":{column}" for column in values)
        db.execute(
            text(f"INSERT INTO users ({column_names}) VALUES ({placeholders})"),
            values,
        )

        db.commit()

        created_user = db.execute(
            text("SELECT id FROM users WHERE email = :email"),
            {"email": user.email},
        ).fetchone()

        return {
            "message": "Пользователь зарегистрирован",
            "access_token": create_user_token(created_user.id),
            "token_type": "bearer",
        }

    except IntegrityError:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail="Пользователь с таким email уже существует",
        )

    except Exception as e:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail=str(e),
        )

    finally:
        db.close()


@router.post("/login")
def login(user: UserLogin):
    db = SessionLocal()

    result = db.execute(
        text("SELECT * FROM users WHERE email = :email"),
        {"email": user.email},
    ).fetchone()

    if not result:
        db.close()

        raise HTTPException(
            status_code=404,
            detail="Пользователь не найден",
        )

    db_user = result._mapping
    password_hash = db_user.get("password") or db_user.get("hashed_password")

    if not password_hash or not verify_password(user.password, password_hash):
        db.close()

        raise HTTPException(
            status_code=401,
            detail="Неверный пароль",
        )

    token = create_user_token(db_user["id"])

    db.close()

    return {
        "access_token": token,
        "token_type": "bearer",
    }
