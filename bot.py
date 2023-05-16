from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TOKEN
import json

with open ('data/data.json','r',encoding='utf-8') as f:
    data=json.load(f)






bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    data3 = ''

    for i in range(len(data)):
        data2 = ''
        for key,value in data[i].items():
            data2 = data2 + f'{key} : {value} , '
        print(data2)
        data3 = data3 + '\n\n' + data2
    await message.reply(data3)



@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Напиши мне что-нибудь, и я отпрпавлю этот текст тебе в ответ!")


@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)


if __name__ == '__main__':
    executor.start_polling(dp)
