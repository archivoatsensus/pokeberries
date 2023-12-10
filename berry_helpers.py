from utils import get_response_as_json
from multiprocessing import Manager, Pool

manager = Manager()
growth_time_list = manager.list()


class BerriesManager:

    def __init__(self, url):
        self.url = url
        self.berries_index = []
        self.growth_time_list = manager.list()

    def get_berries_index(self):
        self.berries_index = get_berry_index_from_source(self.url)

    def get_berries_growth_time(self):
        berry_urls = []
        for berry in self.berries_index:
            berry_urls.append(berry['url'])

        with Pool() as pool:
            pool.map(self.populate_berries_growth_time, berry_urls)

    def populate_berries_growth_time(self, url):
        data = get_response_as_json(url)
        self.growth_time_list.append(data['growth_time'])


def get_berry_index_from_source(url):
    """
    Although we could have constructed each berry URL sequentially with the current dataset
    (e.g. /berry/64), we decided to use the URL field of the Berries API data structure
    considering possible changes in the future
    """
    berries_index = []
    data = get_response_as_json(url)
    berries_index.extend(data['results'])
    if data['next'] is not None:
        berries_index.extend(get_berry_index_from_source(data['next']))
    return berries_index
