from aiogram import types
from aiogram.dispatcher.filters import Text

from loader import dp



@dp.message_handler(Text(contains = 'salom', ignore_case = True))
async def send_come(msg: types.Message):
    await msg.answer("Alik")