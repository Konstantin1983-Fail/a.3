from fastapi import FastAPI, HTTPException, Path
from pydantic import BaseModel
from typing import List, Annotated

app = FastAPI()

class User(BaseModel):
    id: int
    username: str
    age: int

users: List[User] = []

@app.get("/users", response_model=List[User])
async def get_users() -> List[User]:
    return users

@app.post("/user/{username}/{age}", response_model=User)
async def create_user(
    username: Annotated[str, Path(description="Enter username", example="UrbanUser")],
    age: Annotated[int, Path(description="Enter age", example=24)]
) -> User:
    user_id = max((user.id for user in users), default=0) + 1
    new_user = User(id=user_id, username=username, age=age)
    users.append(new_user)
    return new_user

@app.put("/user/{user_id}/{username}/{age}", response_model=User)
async def update_user(
    user_id: Annotated[int, Path(description="Enter user ID", example=1)],
    username: Annotated[str, Path(description="Enter username", example="UrbanProfi")],
    age: Annotated[int, Path(description="Enter age", example=28)]
) -> User:
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail="User was not found")

@app.delete("/user/{user_id}", response_model=User)
async def delete_user(
    user_id: Annotated[int, Path(description="Enter user ID", example=1)]
) -> User:
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return user
    raise HTTPException(status_code=404, detail="User was not found")

# Запуск приложения
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="127.0.0.1", port=8001)
