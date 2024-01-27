import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.filters.command import Command
from aiogram.types import Message

from root import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: Message):
    await message.answer('Выберете действие')


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
