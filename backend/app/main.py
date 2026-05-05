from fastapi import FastAPI, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Tour
from sqlalchemy import text
from pydantic import BaseModel
from passlib.context import CryptContext
from fastapi.responses import HTMLResponse
from jose import jwt
from datetime import datetime, timedelta

app = FastAPI()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET_KEY = "supersecretkey"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

@app.get("/")
def home():
    return {"message": "Сервер работает!"}


@app.get("/tours")
def get_tours():
    db: Session = SessionLocal()

    tours = db.query(Tour).all()

    result = []

    for tour in tours:
        result.append({
            "tour_id": tour.tour_id,
            "title": tour.title,
            "region": tour.region,
            "price": float(tour.price)
        })

    db.close()

    return result



class BookingCreate(BaseModel):
    user_id: int
    tour_id: int
    participants_count: int
    participants_info: str


@app.post("/booking")
def booking(data: BookingCreate):
    db = SessionLocal()

    query = """
    INSERT INTO bookings
    (user_id, tour_id, participants_count, participants_info)
    VALUES
    (:user_id, :tour_id, :participants_count, :participants_info)
    """

    db.execute(
        text(query),
        {
            "user_id": data.user_id,
            "tour_id": data.tour_id,
            "participants_count": data.participants_count,
            "participants_info": data.participants_info
        }
    )

    db.commit()
    db.close()

    return {"message": "Запись создана"}       


@app.post("/favorites")
def favorites():
    return {"message": "Добавлено в избранное"} 



class UserCreate(BaseModel):
    full_name: str
    phone: str
    email: str
    region: str
    password: str


class UserLogin(BaseModel):
    email: str
    password: str

def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


@app.get("/register-page", response_class=HTMLResponse)
def register_page():
    with open("app/templates/register.html", "r", encoding="utf-8") as file:
        return file.read()

@app.post("/register")
def register(user: UserCreate):
    db = SessionLocal()

    try:
        hashed_password = pwd_context.hash(user.password)

        query = """
        INSERT INTO users (full_name, phone, email, region, password)
        VALUES (:full_name, :phone, :email, :region, :password)
        """

        db.execute(text(query), {
            "full_name": user.full_name,
            "phone": user.phone,
            "email": user.email,
            "region": user.region,
            "password": hashed_password
        })

        db.commit()
        return {"message": "Пользователь зарегистрирован"}

    except Exception as e:
        db.rollback()
        return {"error": str(e)}

    finally:
        db.close()

@app.post("/login")
def login(user: UserLogin):
    db = SessionLocal()

    result = db.execute(
        text("SELECT * FROM users WHERE email = :email"),
        {"email": user.email}
    ).fetchone()

    if not result:
        db.close()
        raise HTTPException(status_code=404, detail="Пользователь не найден")

    if not pwd_context.verify(user.password, result.password):
        db.close()
        raise HTTPException(status_code=401, detail="Неверный пароль")

    token = create_access_token({
        "sub": str(result.user_id)
    })

    db.close()

    return {
        "access_token": token,
        "token_type": "bearer"
    }       