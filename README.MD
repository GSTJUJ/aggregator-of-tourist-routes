## Technology Stack

### Frontend

* HTML5
* CSS3
* JavaScript 
* Jinja2 Templates
* FastAPI StaticFiles

### Backend

* Python 3.11+
* FastAPI
* SQLAlchemy
* Pydantic
* Uvicorn
* JWT Authentication
* Passlib + BCrypt

### Database

* PostgreSQL

### Additional Libraries

* BeautifulSoup4
* Python Dotenv

## Architecture

The application is built as a monolithic FastAPI web application.

The frontend is implemented using Jinja2 templates and static assets (CSS, JavaScript, images) located in the `templates/` and `static/` directories. Pages are rendered on the server side and delivered to the client through FastAPI routes.

The backend provides:

- authentication and authorization;
- database interaction;
- route aggregation from multiple data providers;
- normalization of JSON, XML and HTML data into a unified data model;
- tourist route management and presentation;
- server-side page rendering.

## Data Aggregation

The application aggregates tourist routes from multiple provider types:

- JSON providers;
- XML providers;
- HTML providers.

Data from all providers is normalized into a unified internal model, allowing routes to be stored, searched and displayed through a common interface regardless of the original data source.

## Test Credentials

The following account can be used for testing:

| Parameter | Value                               |
| --------- | ----------------------------------- |
| Email     | [test@mail.ru]                      |
| Password  | 0000                                |

## Main Technologies

| Layer          | Technologies                  |
| -------------- | ----------------------------- |
| Frontend       | HTML, CSS, JavaScript, Jinja2 |
| Backend        | FastAPI, Python               |
| ORM            | SQLAlchemy                    |
| Database       | PostgreSQL                    |
| Authentication | JWT                           |
| Server         | Uvicorn                       |

