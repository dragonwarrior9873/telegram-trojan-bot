import logging
import time
import csv
import config
# from plugins.execute_db_queries import Executor
from plugins.process_requests import get_response
from aiogram import *
from telethon.sync import TelegramClient, events


logging.basicConfig(level=logging.INFO)
bot = Bot(token=config.API_TOKEN)
dp = Dispatcher(bot)


client = TelegramClient('name', '21387552', '4d1cf513f60b6af34d200429e5e92df9')

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm CSV parser bot!\nSend me your .csv file below👇.")


@dp.message_handler()
async def process_message(message: types.Message):
    await message.answer('Send me your .csv file below👇')


@dp.message_handler(content_types=['document'])
async def process_documents(message: types.Message):
    if message.document.mime_type == config.CSV_MIME_TYPE:
        response = get_response(message)
        reader = csv.reader(response.text.split('\n'), delimiter=';')
        try:
            for row in reader:
                if len(row) > 0:
                    data_list = row[0].split(",")
                    address = data_list[0]
                    if address == "address":
                         continue
                    print(address)  # Trying to access an index that doesn't exist
                    await client.send_message(config.TARGET_CHANNEL, address)
                    time.sleep(3)  # Pause the program for 2 seconds
        except IndexError:
                    print("Error parsing CSV file.")

        await message.answer('Adding parsed data from CSV file to database...') 
        await message.answer(f'Success. rows added to database.')
    else:
        await message.answer('Expected .CSV file format, try again')



if __name__ == '__main__':
    client.start()
    executor.start_polling(dp, skip_updates=True)
    # client.run_until_disconnected()

