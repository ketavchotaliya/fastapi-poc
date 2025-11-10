from fastapi import FastAPI
from routes import blogs, users, auth
from utils.database import create_db_tables

app = FastAPI(redoc_url=None)

APP_VERSION = "v1"


@app.on_event("startup")
def startup_event():
    """
    Function executed when the application starts up.
    """
    create_db_tables()
    print("FastAPI application started up and database tables created.")


app.include_router(blogs.router, tags=["Blogs"], prefix=f"/api/{APP_VERSION}/blogs")
app.include_router(users.router, tags=["Users"], prefix=f"/api/{APP_VERSION}/user")
app.include_router(auth.router, tags=["Auth"], prefix=f"/api/{APP_VERSION}")
