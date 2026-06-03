from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy import inspect, text

from app.api.routes import aggregation
from app.api.routes import auth
from app.api.routes import tours
from app.api.routes.search import router as search_router

from app.database.database import Base, engine
from app.database.database import SessionLocal

from app.models.user import User
from app.models.tour import Tour
from app.models.booking import Booking
from app.services.aggregation_service import AggregationService


Base.metadata.create_all(bind=engine)


def ensure_user_profile_columns():
    inspector = inspect(engine)

    if "users" not in inspector.get_table_names():
        return

    columns = {
        column["name"]
        for column in inspector.get_columns("users")
    }

    profile_columns = {
        "full_name": "VARCHAR(255)",
        "phone": "VARCHAR(50)",
        "region": "VARCHAR(255)",
        "password": "VARCHAR",
    }

    with engine.begin() as connection:
        for column_name, column_type in profile_columns.items():
            if column_name not in columns:
                connection.execute(
                    text(
                        f"ALTER TABLE users "
                        f"ADD COLUMN {column_name} {column_type}"
                    )
                )


ensure_user_profile_columns()


app = FastAPI()


app.include_router(aggregation.router)
app.include_router(auth.router)
app.include_router(tours.router)
app.include_router(search_router)


app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="app/templates")


@app.on_event("startup")
async def load_initial_tours():
    db = SessionLocal()

    try:
        if db.query(Tour).count() == 0:
            service = AggregationService()
            await service.aggregate(db)
    finally:
        db.close()


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="first_page.html"
    )


@app.get("/excursions", response_class=HTMLResponse)
async def excursions_page(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="excursions.html"
    )


@app.get("/schools", response_class=HTMLResponse)
async def schools_page(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="schools.html"
    )


@app.get("/about", response_class=HTMLResponse)
async def about_page(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="about.html"
    )


@app.get("/contacts", response_class=HTMLResponse)
async def contacts_page(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="contacts.html"
    )
