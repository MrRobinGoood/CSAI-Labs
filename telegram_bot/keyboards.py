from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

instruction = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Поисковые запросы', callback_data='instruction_command')],
    [InlineKeyboardButton(text='Торговые карточки', callback_data='instruction_trade_card')],
    [InlineKeyboardButton(text='Компании', callback_data='instruction_company')],
    [InlineKeyboardButton(text='Коллекции', callback_data='instruction_collection')]
])

trade_card = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Заказчик', callback_data='trade_card_company')],
    [InlineKeyboardButton(text='Объекты закупки', callback_data='trade_card_purchase_object')],
    [InlineKeyboardButton(text='Документы', callback_data='trade_card_document')]
])


# admin_panel= InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text='Список файлов', callback_data='list_files')],
#     [InlineKeyboardButton(text='Добавить файлы', callback_data='add_file')],
#     [InlineKeyboardButton(text='Удалить файлы', callback_data='delete_file')]
#
# ])
#
# complete_panel = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text='Готово', callback_data='complete')]
#
# ])