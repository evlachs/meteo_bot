import asyncio
from aiogram import executor

from loader import dp
from message_sender import send_message


async def on_startup(dp):
    loop = asyncio.get_event_loop()
    loop.create_task(send_message(60))


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
