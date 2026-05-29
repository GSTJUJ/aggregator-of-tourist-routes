from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from app.api.routes import aggregation
from app.api.routes import tours
from app.api.routes.search import router as search_router

from app.database.database import Base, engine

from app.models.user import User
from app.models.tour import Tour
from app.models.booking import Booking


Base.metadata.create_all(bind=engine)


app = FastAPI()


app.include_router(aggregation.router)
app.include_router(tours.router)
app.include_router(search_router)


app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="app/templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="first_page.html"
    )
