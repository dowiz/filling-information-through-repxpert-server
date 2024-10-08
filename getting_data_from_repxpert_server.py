import requests


def get_data(unicode, vendor):
    url = f"http://localhost:3000/?query={unicode}&brand={vendor}"

    response = requests.get(url)

    return response.json()
