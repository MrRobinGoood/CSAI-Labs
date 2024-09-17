from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

instruction = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Поисковые запросы', callback_data='instruction_command')],
    [InlineKeyboardButton(text='Торговые карточки', callback_data='instruction_trade_card')],
    [InlineKeyboardButton(text='Компании', callback_data='instruction_company')],
    [InlineKeyboardButton(text='Коллекции', callback_data='instruction_collection')]
])
