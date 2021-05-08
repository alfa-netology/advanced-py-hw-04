import requests

headers = {'Authorization': '<PLACE YANDEX TOKEN HERE>'}
url = 'https://cloud-api.yandex.net/v1/disk/resources'

def make_folder(name):
    params = {'path': name}
    response = requests.put(url, params=params, headers=headers)
    return response.status_code

