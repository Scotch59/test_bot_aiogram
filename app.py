import asyncio
from \
    aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

bot = Bot(token='6616598911:AAH7Kog6vo_24cJwVNU40eDgmMBw_GAOh4U')
dp = Dispatcher()


@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer('Это была стартовая команда')


@dp.message()
async def echo(message: types.Message):
    await message.answer(message.text)
    await message.reply(message.text)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


asyncio.run(main())