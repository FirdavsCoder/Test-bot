from aiogram import types
from aiogram.dispatcher import filters

from loader import dp



SUPERUSERS = ['1849953640','1034634714', '5561697303', '5004733569']



@dp.message_handler(chat_id = SUPERUSERS, commands=['start'])
async def send_welcome(msg: types.Message):
    await msg.answer("Xush kelibsiz hurmatli ADMIN!")