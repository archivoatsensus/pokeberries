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


# Calculations utils
def calculate_median(values):
    values_length = len(values)
    sorted_values = sorted(values)
    reference_middle_offset = int(values_length / 2)
    if values_length % 2 != 0:
        return sorted_values[reference_middle_offset]

    middle_a = sorted_values[reference_middle_offset - 1]
    middle_b = sorted_values[reference_middle_offset]
    return (middle_a + middle_b) / 2


def calculate_variance(values):
    mean = sum(values) / len(values)
    squared_mean_distances = [(x - mean) ** 2 for x in values]
    return sum(squared_mean_distances) / len(values)
