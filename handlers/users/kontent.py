from aiogram import types
from aiogram.dispatcher import filters

from loader import dp


@dp.message_handler(content_types=types.ContentType.PHOTO)
async def send_photo(msg: types.Message):
    await msg.answer("Bu qanday rasm?πΌ")
    
    
@dp.message_handler(content_types=types.ContentType.VOICE)
async def send_voice(msg: types.Message):
    await msg.answer("Yaxshi eshitmadim!π£")
    
    
@dp.message_handler(content_types=types.ContentType.CONTACT)
async def send_contact(msg: types.Message):
    await msg.answer("Kim bu odam?π«")
    

@dp.message_handler(content_types=types.ContentType.STICKER)
async def send_sticker(msg: types.Message):
    await msg.answer('βΊοΈ')
    
    
@dp.message_handler(content_types=types.ContentType.LOCATION)
async def send_location(msg: types.Message):
    await msg.answer("Bu qayer?π")
    
