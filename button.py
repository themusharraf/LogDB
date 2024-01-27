from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType, InlineKeyboardMarkup, \
    InlineKeyboardButton

start = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='Выгрузить заказы в чат')
    ],
    [
        KeyboardButton(text='Выбрать заказ'),
        KeyboardButton(text='Показать выполненные заказы')
    ]
], resize_keyboard=1)
