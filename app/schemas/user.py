from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    firstname: str
    lastname: str
    age: int
    slug: str

class UserCreate(UserBase):
    username: str
    firstname: str
    lastname: str
    age: int


class UserUpdate(BaseModel):
    firstname: str
    lastname: str
    age: int

class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True  # Ранее orm_mode=True
