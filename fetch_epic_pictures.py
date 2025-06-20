import datetime
import requests
from dotenv import load_dotenv
import os


def get_epic_urls(params):
    date = (datetime.datetime.now() - datetime.timedelta(days=2)).strftime("%Y/%m/%d")
    epic_links = []
    method_url = "https://api.nasa.gov/EPIC/api/natural/"
    response = requests.get(method_url, params=params)
    response.raise_for_status()
    response_json = response.json()
    for element in response_json:
        picture = element["image"]
        picture_url = f"https://api.nasa.gov/EPIC/archive/natural/{date}/png/{picture}.png"
        epic_links.append(picture_url)
    return epic_links


def downloads_epic_pictures(epic_links, params, folder):
    for picture_num, picture in enumerate(epic_links):
        image = requests.get(picture, params=params)
        with open(f"{folder}/image_epic_{picture_num}.png", 'wb') as file:
            file.write(image.content)


if __name__ == "__main__":
    load_dotenv()
    nasa_token = os.environ["NASA_TOKEN"]
    params = {
        "api_key": nasa_token
    }
    folder = 'images'
    try:
        os.mkdir(folder)
    except:
        pass
    epic_links = get_epic_urls(params)
    downloads_epic_pictures(epic_links, params, folder)
