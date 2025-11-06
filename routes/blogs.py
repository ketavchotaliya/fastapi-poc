from fastapi import APIRouter

router = APIRouter(
    tags=["Blogs"],
    prefix="/blogs"
)


@router.get("/", )
def get_blogs():
    return "Hello from Blog Route"
