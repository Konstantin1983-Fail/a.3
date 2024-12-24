from fastapi import FastAPI, Path, HTTPException
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}

@app.get("/users")
async def get_users() -> dict:
    return users

@app.post("/user/{username}/{age}")
async def create_user(
    username: Annotated[str, Path(description="Enter username", example="UrbanUser")],
    age: Annotated[int, Path(description="Enter age", example=24)]
) -> str:
    user_id = str(int(max(users.keys(), key=int)) + 1) if users else '1'
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} is registered"

@app.put("/user/{user_id}/{username}/{age}")
async def update_user(
    user_id: Annotated[str, Path(description="Enter user ID", example="1")],
    username: Annotated[str, Path(description="Enter username", example="UrbanProfi")],
    age: Annotated[int, Path(description="Enter age", example=28)]
) -> str:
    if user_id in users:
        users[user_id] = f"Имя: {username}, возраст: {age}"
        return f"User {user_id} has been updated"
    else:
        raise HTTPException(status_code=404, detail="User not found")

@app.delete("/user/{user_id}")
async def delete_user(
    user_id: Annotated[str, Path(description="Enter user ID", example="2")]
) -> str:
    if user_id in users:
        del users[user_id]
        return f"User {user_id} has been deleted"
    else:
        raise HTTPException(status_code=404, detail="User not found")

# Запуск приложения
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="127.0.0.1", port=8001)

