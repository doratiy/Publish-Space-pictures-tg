import requests
from dotenv import load_dotenv
import os
import time


def get_nasa_pictures(nasa_token):
    nasa_links = []
    method_url = "https://api.nasa.gov/planetary/apod"
    params = {
        "count": 5,
        "api_key": nasa_token
    }
    response = requests.get(method_url, params=params)
    response.raise_for_status()
    for response in (response.json()):
        if response["media_type"] == "image":
            nasa_links.append(response["url"])
    return nasa_links


def downloads_nasa_pictures(nasa_links, folder):
    for picture_num, picture in enumerate(nasa_links):
        ext = os.path.splitext(picture.split()[0])[1]
        response = requests.get(picture)
        response.raise_for_status()
        with open(f"{folder}/image_apod_{picture_num}{ext}", 'wb') as file:
            file.write(response.content)
        time.sleep(5)


if __name__ == "__main__":
    folder = 'images'
    try:
        os.mkdir(folder)
    except:
        pass
    load_dotenv()
    nasa_token = os.environ["NASA_TOKEN"]
    nasa_links = get_nasa_pictures(nasa_token)
    downloads_nasa_pictures(nasa_links, folder)
