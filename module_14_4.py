import os
from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv
import crud_functions  # Функции работы с базой данных

# Инициализация базы данных и добавление тестовых данных
crud_functions.initiate_db()
crud_functions.add_test_data()

# Загружаем токен из .env
load_dotenv()
API_TOKEN = os.getenv("API_TOKEN")

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Кнопки главного меню
button_buy = KeyboardButton("Купить")
button_info = KeyboardButton("Информация")
button_calculate = KeyboardButton("Рассчитать")

# Главная клавиатура
main_menu = ReplyKeyboardMarkup(resize_keyboard=True).row(button_buy, button_info, button_calculate)

# Inline-клавиатура для продуктов
products = crud_functions.get_products_by_category("Фрукты")  # Используем фиктивную категорию для примера
product_menu = InlineKeyboardMarkup(row_width=2)
for product in products:
    product_menu.add(InlineKeyboardButton(
        text=product[0],  # Название продукта
        callback_data="product_buying"
    ))


# Обработчик команды /start
@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.answer("Добро пожаловать! Выберите действие:", reply_markup=main_menu)


# Обработчик кнопки "Купить"
@dp.message_handler(Text(equals="Купить"))
async def get_buying_list(message: types.Message):
    products = crud_functions.get_products_by_category("Фрукты")  # Замените "Фрукты" на вашу категорию
    for product in products:
        # Отправляем описание продукта вместе с картинкой
        await message.answer_photo(
            photo=open(product[3], "rb"),  # Путь к картинке
            caption=(
                f"Название: {product[0]}\n"
                f"Описание: {product[1]}\n"
                f"Цена: {product[2]} руб."
            )
        )
    # В конце показываем Inline-клавиатуру
    await message.answer("Выберите продукт для покупки:", reply_markup=product_menu)


# Обработчик Inline-кнопки
@dp.callback_query_handler(lambda call: call.data == "product_buying")
async def send_confirm_message(call: types.CallbackQuery):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()  # Закрываем callback-запрос


# Запуск бота
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
