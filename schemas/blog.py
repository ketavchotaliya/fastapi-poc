from pydantic import BaseModel


class BlogBase(BaseModel):
    title: str
    body: str


class BlogRequest(BlogBase):
    user_id: int
    pass


class BlogResponse(BlogBase):
    # creator: UserBase

    class Config:
        from_attributes = True
