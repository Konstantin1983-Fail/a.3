import os
from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv

# Загружаем токен из .env
load_dotenv()
API_TOKEN = os.getenv("API_TOKEN")

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Данные о продуктах
products = [
    {
        "name": "Игрушка Гусь",
        "description": "Мягкая игрушка в виде гуся. Отличный подарок!",
        "price": "500",
        "image": "images/goose_toy.jpg"
    },
    {
        "name": "Игрушка Нот-кот",
        "description": "Кот, который всегда поёт!",
        "price": "600",
        "image": "images/not_cat_toy.jpg"
    },
    {
        "name": "Игрушка Собака",
        "description": "Пушистая собака с добрыми глазами.",
        "price": "700",
        "image": "images/dog_toy.jpg"
    },
    {
        "name": "Игрушка Улыбашка",
        "description": "Забавная игрушка, дарит радость.",
        "price": "450",
        "image": "images/some_other_toy.jpg"
    }
]

# Кнопки главного меню
button_buy = KeyboardButton("Купить")
button_info = KeyboardButton("Информация")
button_calculate = KeyboardButton("Рассчитать")

# Главная клавиатура
main_menu = ReplyKeyboardMarkup(resize_keyboard=True).row(button_buy, button_info, button_calculate)

# Inline-клавиатура для продуктов
product_menu = InlineKeyboardMarkup(row_width=2)
for product in products:
    product_menu.add(InlineKeyboardButton(
        text=product["name"],
        callback_data="product_buying"
    ))

# Обработчик команды /start
@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.answer("Добро пожаловать! Выберите действие:", reply_markup=main_menu)

# Обработчик кнопки "Купить"
@dp.message_handler(Text(equals="Купить"))
async def get_buying_list(message: types.Message):
    for product in products:
        # Отправляем описание продукта вместе с картинкой
        await message.answer_photo(
            photo=open(product["image"], "rb"),  # Открываем файл картинки
            caption=(
                f"Название: {product['name']}\n"
                f"Описание: {product['description']}\n"
                f"Цена: {product['price']} руб."
            )
        )
    # В конце показываем Inline-клавиатуру
    await message.answer("Выберите игрушку для покупки:", reply_markup=product_menu)

# Обработчик Inline-кнопки
@dp.callback_query_handler(lambda call: call.data == "product_buying")
async def send_confirm_message(call: types.CallbackQuery):
    await call.message.answer("Вы успешно приобрели игрушку!")
    await call.answer()  # Закрываем callback-запрос

# Запуск бота
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
