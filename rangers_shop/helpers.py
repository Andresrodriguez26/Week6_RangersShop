import decimal
import requests 
import requests_cache
import json




# Set up our API cache location (this is going to make a temporary database storage for our api calls)

requests_cache.install_cache("image_cache", backend="sqlite")


def get_image(search):
    url = "https://google-search72.p.rapidapi.com/imagesearch"

    querystring = {"q": search,"gl":"us","lr":"lang_en","num":"10","start":"0"}

    headers = {
        "X-RapidAPI-Key": "5ff0a59abemsh1a7801ed3d86869p10af1bjsn0d5785b8ed5a",
        "X-RapidAPI-Host": "google-search72.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    data = response.json()

    img_url = ""

    if "items" in data.keys():
        img_url = data["items"][0]["originalImageUrl"]

    return img_url



class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return str(obj)
        return json.JSONEncoder(JSONEncoder, self).default(obj) # if not the JSONEncoder from json class can handle it