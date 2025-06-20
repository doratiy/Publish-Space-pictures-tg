import requests
import os


def get_spacex_urls():
    method_url = "https://api.spacexdata.com/v5/launches/"
    params = {
        "id": "5eb87d46ffd86e000604b388"
    }
    response = requests.get(method_url, params=params)
    response.raise_for_status()
    response_json = response.json()
    for response in reversed(response_json):
        if response["links"]["flickr"]["original"]:
            spacex_links = response["links"]["flickr"]["original"]
            return spacex_links


def downloads_spacex_pictures(spacex_links, folder):
    for picture_num, image in enumerate(spacex_links):
        image = requests.get(image)
        with open(f"{folder}/image_spacex_{picture_num}.jpg", 'wb') as file:
            file.write(image.content)


if __name__ == "__main__":
    folder = 'images'
    try:
        os.mkdir(folder)
    except:
        pass
    links_spacex = get_spacex_urls()
    response = get_spacex_urls()
    downloads_spacex_pictures(response, folder)
