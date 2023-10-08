from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


start_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Biz haqimizda'),
            KeyboardButton('Kurslar')
        ]
        # [KeyboardButton('Kurslar')],
    ], resize_keyboard=True)

cours_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Foundation Python🐍'),
            KeyboardButton('Foundation Java☕')
        ],
        [
            KeyboardButton('Backend'),
            KeyboardButton('Frontend')
        ],
        [
            KeyboardButton('Data Science'),
            KeyboardButton('Android')
        ],
        [
            KeyboardButton('Kids')
        ]
    ],
    resize_keyboard=True
)

pyt_found = InlineKeyboardMarkup(
    inline_keyboard=[
        [
        InlineKeyboardButton(text='Obuna bolish', callback_data='1')
        ]
    ]
)

obuna = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Contact', request_contact=True),
            KeyboardButton('Location', request_location=True)
        ]
    ],
    resize_keyboard=True
)