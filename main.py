from fastapi import FastAPI
# from pydantic import BaseModel

# Создаем экземпляр приложения FastAPI
app = FastAPI()

@app.get("/")
async def welcome() -> dict:
    return {"message": "Hello World"}


@app.get("/user/A/B")
async def news() -> dict:
    return {"message": f"Hello, Tester!"}


@app.get("/id")
async def id_paginator(username: str= "alex", age: int= 24) -> dict:
    return {"User": username, "Age": age}



# @app.get("/user/{first_name}/{last_name}")
# async def news(first_name: str, last_name: str) -> dict:
#     return {"message": f"Hello, {first_name} {last_name}"}




# @app.post("/products/")
# async def create_product():
#
#
#     """
#     Создает новый продукт в системе.
#     - **name**: название продукта
#     - **price**: цена продукта
#     - **quantity**: количество на складе
#     """
#     return
#
#
# # Определение базового маршрута
# @app.get("/")
# async def root():
#     return {"message": "Hello, FastAPI!"}
#
#
# # GET-запрос — получение данных:
# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     return {"item_id": item_id}
#
#
# # POST-запрос — добавление данных
#
# class Item(BaseModel):
#     name: str
#     price: float
#
#
# @app.post("/items/")
# async def create_item(item: Item):
#     return {"name": item.name, "price": item.price}
#
#
# # PUT-запрос — обновление данных
# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):
#     return {"item_id": item_id, "name": item.name, "price": item.price}
#
#
# # DELETE-запрос — удаление данных
# @app.delete("/items/{item_id}")
# async def delete_item(item_id: int):
#     return {"message": "Item deleted", "item_id": item_id}
