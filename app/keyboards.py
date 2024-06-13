from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)


letsStartAB = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='Поехали!')
    ]
], resize_keyboard=True, one_time_keyboard=True)

letsStartAAM = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='Погнали!')
    ]
], resize_keyboard=True, one_time_keyboard=True)

gameMain = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='Строительство'),
        KeyboardButton(text='Информация')
    ],
    [
        KeyboardButton(text='Меню')
    ]
], resize_keyboard=True, one_time_keyboard=True)

gameConstruction = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='Здания'),
        KeyboardButton(text='Парки')
    ]
], resize_keyboard=True, one_time_keyboard=True)

surveys = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Всё обо мне', callback_data='allAboutMe')
    ],
    [
        InlineKeyboardButton(text='Наш Бот', callback_data="aboutBot")
    ]
])

shopSelect = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Меню', callback_data='menu'),
        InlineKeyboardButton(text='Браслет', callback_data='anklet')
    ],
    [
        InlineKeyboardButton(text='Худи Вдохновителей', callback_data='hoodie'),
        InlineKeyboardButton(text='Термокружка', callback_data='termocup')
    ]
])

buySmth = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Назад', callback_data='comeBack'),
        InlineKeyboardButton(text='Купить', callback_data='buy')
    ]
])

timetable = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Назад', callback_data='menu'),
        InlineKeyboardButton(text='Настроить расписание', callback_data='changeTimetable')
    ]
])

build = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Построить', callback_data='build')
    ]
])