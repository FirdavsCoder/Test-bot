from aiogram import types
from aiogram.dispatcher import filters

from loader import dp


@dp.message_handler(content_types=types.ContentType.PHOTO)
async def send_photo(msg: types.Message):
    await msg.answer("Bu qanday rasm?🖼")
    
    
@dp.message_handler(content_types=types.ContentType.VOICE)
async def send_voice(msg: types.Message):
    await msg.answer("Yaxshi eshitmadim!🗣")
    
    
@dp.message_handler(content_types=types.ContentType.CONTACT)
async def send_contact(msg: types.Message):
    await msg.answer("Kim bu odam?🫂")
    

@dp.message_handler(content_types=types.ContentType.STICKER)
async def send_sticker(msg: types.Message):
    await msg.answer('☺️')
    
    
@dp.message_handler(content_types=types.ContentType.LOCATION)
async def send_location(msg: types.Message):
    await msg.answer("Bu qayer?📍")
    
