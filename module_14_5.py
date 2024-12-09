import os
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from dotenv import load_dotenv
from crud_functions1 import initiate_db, add_user, is_included

# Загружаем токен из .env
load_dotenv()
API_TOKEN = os.getenv("API_TOKEN")

# Создаём бота и диспетчер
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())

# Машина состояний для этапов регистрации
class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()

# Кнопка "Регистрация"
def registration_button():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton("Регистрация")
    keyboard.add(button)
    return keyboard

# Стартовое сообщение с кнопкой
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.answer(
        "Добро пожаловать! Нажмите кнопку 'Регистрация', чтобы начать.",
        reply_markup=registration_button()
    )

# Обработчик нажатия на кнопку "Регистрация"
@dp.message_handler(lambda message: message.text == "Регистрация")
async def start_registration(message: types.Message):
    await message.answer(
        "Введите имя пользователя (только латинский алфавит):",
        reply_markup=types.ReplyKeyboardRemove()
    )
    await RegistrationState.username.set()

# Получение имени пользователя
@dp.message_handler(state=RegistrationState.username)
async def set_username(message: types.Message, state: FSMContext):
    username = message.text.strip()

    if is_included(username):  # Проверка существования пользователя
        await message.answer("Пользователь с таким именем уже существует, введите другое имя.")
    else:
        await state.update_data(username=username)
        await message.answer("Введите свой email:")
        await RegistrationState.email.set()

# Получение email
@dp.message_handler(state=RegistrationState.email)
async def set_email(message: types.Message, state: FSMContext):
    email = message.text.strip()
    await state.update_data(email=email)
    await message.answer("Введите свой возраст:")
    await RegistrationState.age.set()

# Получение возраста и завершение регистрации
@dp.message_handler(state=RegistrationState.age)
async def set_age(message: types.Message, state: FSMContext):
    try:
        age = int(message.text.strip())  # Проверка на число
        user_data = await state.get_data()
        username = user_data['username']
        email = user_data['email']

        # Сохранение данных
        add_user(username, email, age)
        await message.answer(
            f"Регистрация успешна! Привет, {username}!",
            reply_markup=registration_button()
        )
        await state.finish()
    except ValueError:
        await message.answer("Введите корректный возраст (число).")

if __name__ == '__main__':
    initiate_db()
    executor.start_polling(dp, skip_updates=True)
