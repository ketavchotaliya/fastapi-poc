from fastapi import FastAPI
from routes import blogs

app = FastAPI()

app.include_router(blogs.router)


@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}
