from tg_bot import main
from dotenv import load_dotenv
import os
import argparse
from tg_bot import get_files_address
from fetch_epic_pictures import get_epic_urls
from fetch_epic_pictures import downloads_epic_pictures
from fetch_spacex_last_launch import get_spacex_urls
from fetch_spacex_last_launch import downloads_spacex_pictures
from fetch_nasa_pictures import get_nasa_pictures, downloads_nasa_pictures


def start(delay, chat_id, tg_bot_token, image_addresses, params, folder):
    epic_links = get_epic_urls(params)
    downloads_epic_pictures(epic_links, params, folder)
    spacex_links = get_spacex_urls()
    downloads_spacex_pictures(spacex_links, folder)
    nasa_links = get_nasa_pictures(nasa_token)
    downloads_nasa_pictures(nasa_links, folder)
    main(delay, chat_id, tg_bot_token, image_addresses)


if __name__ == "__main__":
    load_dotenv()
    folder = 'images'
    try:
        os.mkdir(folder)
    except:
        pass
    parser = argparse.ArgumentParser(
        description = 'Описание что делает программа'
    )
    parser.add_argument('-delay',
    '--delay',
    help = 'Ваша ссылка',
    default = 14400,
    type = int)
    args = parser.parse_args()
    delay = args.delay
    tg_bot_token = os.environ["TG_BOT_TOKEN"]
    nasa_token = os.environ["NASA_TOKEN"]
    chat_id = os.environ["TG_CHAT_ID"]
    image_addresses = get_files_address()
    params = {
        "api_key": nasa_token
    }
    start(delay, chat_id, tg_bot_token, image_addresses, params, folder)
