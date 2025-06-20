from random import random
import random
import telegram
from dotenv import load_dotenv
import os
import time


def get_files_address():
    image_addresses = []
    for address, dirs, files in os.walk('images'):
        for name in files:
            image_address = os.path.join(address, name)
            image_addresses.append(image_address)
    return image_addresses


def send(delay, chat_id, tg_bot_token, image_addresses):
    bot = telegram.Bot(token=tg_bot_token)
    random.shuffle(image_addresses)
    for image in image_addresses:
        bot.send_photo(chat_id=chat_id, photo=open(image, 'rb'))
        time.sleep(delay)


def main(delay, chat_id, tg_bot_token, image_addresses):
    get_files_address()
    send(delay, chat_id, tg_bot_token, image_addresses)


if __name__ == "__main__":
    load_dotenv()
    tg_bot_token = os.environ["TG_BOT_TOKEN"]
    get_files_address()
    delay = 14800
    chat_id = os.environ["TG_CHAT_ID"]
    image_addresses = get_files_address()
    send(delay, chat_id, tg_bot_token, image_addresses)
