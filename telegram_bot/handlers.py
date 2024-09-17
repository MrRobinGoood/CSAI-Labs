import time
import datetime

from aiogram import Bot, Router
from aiogram import F
from aiogram.types import Message
from aiogram.filters import Command
from keyboards import instruction, trade_card
from aiogram.filters import Filter, CommandObject

router = Router()


class IsCreator(Filter):
    async def __call__(self, message: Message, bot: Bot) -> bool:
        member = await bot.get_chat_member(message.chat.id, message.from_user.id)
        print(member.status)
        return member.status == member.status.CREATOR

class IsPrivate(Filter):
    async def __call__(self, message: Message) -> bool:
        if message.chat.type != "private":
            await message.reply(f"Данная команда поддерживается только в личных сообщениях @TenderCoinBot")
        return message.chat.type == "private"

class HasArgs(Filter):
    async def __call__(self, message: Message, command: CommandObject) -> bool:
        if not command.args:
            await message.reply(f"Ошибка! Пожалуйста укажите аргументы для команды.")
        return bool(command.args)
async def reply_not_allowed(message: Message):
    await message.reply("Данная функция недоступна в чатах с задачами!")


@router.message(Command('start'))
async def start(message: Message):
    await message.answer("Добро пожаловать в TenderCoin Бот! Для помощи напишите /help")
    await message.delete()

@router.message(Command('help'))
async def help(message: Message):
    await message.answer("Инструкция по использованию бота:\n-\n-\n-", reply_markup=instruction)
    await message.delete()

@router.message(Command('tc'), HasArgs())
async def help(message: Message, command: CommandObject):
    #поиск торговой карточки if not tc
    # await message.reply("Ошибка! Торговой карточки с данным номером не найдено.")
    await message.answer(f"Торговая карточка №{command.args}.\nНазвание: блабла\n-\n-\n", reply_markup=trade_card)
    await message.delete()

# @router.message(Command('start'))
# async def start(message: Message):
#     await message.answer(
#         f'Страница 1 из 3\n<blockquote><b>Тендер на закупку оборудования - 056734</b>\n<code>/open_tc345672</code>\nНачальная цена - 100000\nОрганизатор - Муниципальный округ\n<code>/open cmp23471</code>\nМесто поставки - Россия\n<code>/like 345672</code> <code>/collect 345672</code></blockquote>',
#         parse_mode="html")
#
# @router.message(Command('delete_topic'))
# async def start(message: Message, bot: Bot):
#     await bot.close_forum_topic(chat_id=message.chat.id, message_thread_id=message.message_thread_id)
#
#
# @router.message(Command('pin'))
# async def start(message: Message, bot: Bot):
#     await message.pin()
#
#
# @router.message(Command('new'))
# async def start(message: Message, bot: Bot):
#     forumTopic = await bot.create_forum_topic(message.chat.id, f'новый топик {i}')
#     await bot.send_message(chat_id=message.chat.id, message_thread_id=forumTopic.message_thread_id,
#                            text=f'Новый топик {i} успешно создан!')
#
#
#
# @router.message(Command('invite'))
# async def start(message: Message, bot: Bot):
#     link = await bot.create_chat_invite_link(chat_id=message.chat.id,
#                                              expire_date=datetime.datetime.now() + datetime.timedelta(days=1),
#                                              member_limit=1)
#     await message.answer(f'Ссылка приглашение: {link.invite_link}')
#
#
# @router.message(F.text)
# async def start(message: Message):
#     print(message.text)