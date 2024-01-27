import asyncio
import logging
from aiogram import Bot, Dispatcher, Router
from aiogram.filters.command import Command
from aiogram.types import Message
from aiogram import F
from root import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()
rt = Router


@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(text='Выберете действие', reply_markup=start)


@dp.message(F.text == 'Выгрузить заказы в чат')
async def order(message: Message):
    pass  # Buyoda datebasaga kiritilgan barcha malumotlar yuboriladi


@dp.message(F.text == 'Выбрать заказ')
async def order(message: Message):
    await message.answer(reply_markup=...)  # Buyoda zakaz idlari button bolib yuboriladi


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
