from fastapi import FastAPI
from routes import blogs, users
from utils.database import create_db_tables

app = FastAPI()

@app.on_event("startup")
def startup_event():
    """
    Function executed when the application starts up.
    """
    create_db_tables()
    print("FastAPI application started up and database tables created.")

app.include_router(blogs.router)
app.include_router(users.router)


@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}
