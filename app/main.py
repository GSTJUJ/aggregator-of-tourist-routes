from fastapi import FastAPI

from app.routes import auth
from app.routes import booking
from app.routes import tours

app = FastAPI()

app.include_router(auth.router)
app.include_router(booking.router)
app.include_router(tours.router)


@app.get("/")
def home():
    return {"message": "Сервер работает!"}
