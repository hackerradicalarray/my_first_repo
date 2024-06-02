import asyncio
import config
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
import logging
import random
from keyboards import keyboard
from random_fox import fox

#Логирование
logging.basicConfig(level=logging.INFO)

# Объект бота и диспетчера
bot = Bot(token=config.token)
dp = Dispatcher()


@dp.message(Command(commands=['start']))
async def start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.full_name}!', reply_markup=keyboard)


@dp.message(Command(commands=['стоп']))
@dp.message(Command(commands=['stop']))
async def stop (message: types.Message):
    print(message.from_user.full_name)
    await message.answer(f'До скорой встречи, {message.chat.first_name}!', reply_markup=keyboard)


@dp.message(Command(commands=['инфо', 'info']))
@dp.message(F.text.lower() == 'инфо')
async def info(message: types.Message):
    number = random.randint(0, 100)
    await message.answer(f'Твоё число: {number}!')


@dp.message(F.text.lower() == 'Покажи лису')
async def info(message: types.Message):
    img_fox = fox()
    await message.answer('Привет, лови лису')
    await message.answer_photo(img_fox)
    img_fox = fox()
    await bot.send_photo(message.from_user.id, img_fox)


@dp.message(F.text)
async def msg(message: types.Message):
    if 'привет' in message.text.lower():
        await message.reply('И тебе привет!')
    elif 'Как дела?' in message.text.lower():
        await message.reply('Нормально, а у тебя?')
    else:
        await message.reply('Не понимаю тебя...')


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
