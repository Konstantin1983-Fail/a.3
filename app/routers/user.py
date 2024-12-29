from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import Annotated, List
from app.db.depends import get_db
from app.models.user import User
from app.schemas.user import UserResponse, UserCreate, UserUpdate
from sqlalchemy import select
from slugify import slugify

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/", response_model=List[UserResponse])
def all_users(db: Annotated[Session, Depends(get_db)]):
    """
    Возвращает список всех пользователей из базы данных.
    """
    result = db.scalars(select(User)).all()
    return result

@router.get("/{user_id}", response_model=UserResponse)
def user_by_id(user_id: int, db: Annotated[Session, Depends(get_db)]) -> User:
    """
    Возвращает пользователя по его ID.
    Если пользователь не найден, выбрасывает исключение 404.
    """
    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(status_code=404, detail="User was not found")
    return user

@router.post("/create", status_code=status.HTTP_201_CREATED, response_model=UserResponse)
def create_user(user: UserCreate, db: Annotated[Session, Depends(get_db)]):
    """
    Создает нового пользователя в базе данных.
    Возвращает статус 201 и сообщение об успешном выполнении.
    """
    slug = slugify(user.username)
    new_user = User(
        username=user.username,
        firstname=user.firstname,
        lastname=user.lastname,
        age=user.age,
        slug=slug
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.put("/update/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user: UserUpdate, db: Annotated[Session, Depends(get_db)]):
    """
    Обновляет данные пользователя по его ID.
    Если пользователь не найден, выбрасывает исключение 404.
    """
    db_user = db.scalar(select(User).where(User.id == user_id))
    if db_user is None:
        raise HTTPException(status_code=404, detail="User was not found")
    db_user.firstname = user.firstname
    db_user.lastname = user.lastname
    db_user.age = user.age
    db.commit()
    db.refresh(db_user)
    return db_user

@router.delete("/delete/{user_id}")
def delete_user(user_id: int, db: Annotated[Session, Depends(get_db)]):
    """
    Удаляет пользователя по его ID.
    Если пользователь не найден, выбрасывает исключение 404.
    """
    db_user = db.scalar(select(User).where(User.id == user_id))
    if db_user is None:
        raise HTTPException(status_code=404, detail="User was not found")
    db.delete(db_user)
    db.commit()
    return {"status_code": status.HTTP_200_OK, "transaction": "User deleted successfully!"}