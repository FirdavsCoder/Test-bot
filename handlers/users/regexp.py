from email.message import Message
from aiogram import types
from aiogram.dispatcher.filters import Regexp

from loader import dp


EMAIL_REGEX = r'[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'
PHONE_NUM = r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'
COMMAND_EMAIL_REGEX = r"/email:" + EMAIL_REGEX
URL_EXP = r'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()!@:%_\+.~#?&\/\/=]*)'


@dp.message_handler(Regexp(EMAIL_REGEX))
async def regexp_email(msg: types.Message):
    await msg.answer("Emailingiz qabul qilindi!")
    
    
@dp.message_handler(Regexp(PHONE_NUM))
async def regexp_num(msg: types.Message):
    await msg.answer("Nomeringiz qabul qilindi!")
    
    
@dp.message_handler(regexp_commands = [COMMAND_EMAIL_REGEX])
async def regexp_commans(msg: types.Message):
    await msg.answer("Emailingiz qabul qilindi!")
    
@dp.message_handler(Regexp(URL_EXP))
async def regexp_url(msg: types.Message):
    await msg.answer("link qabul qilindi!")