import json
import urllib.request

CUSTOM_USR_AGENT = 'Mozilla/5.0'


# Custom errors
class PokeberriesErrors(Exception):
    pass


# HTTP Utils
def get_response_as_json(url):
    c_headers = {'User-Agent': CUSTOM_USR_AGENT}
    request = urllib.request.Request(url, headers=c_headers)
    with urllib.request.urlopen(request) as response:
        data = json.load(response)
    return data
