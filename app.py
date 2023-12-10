import os
import time
from flask import Flask

from berry_helpers import BerriesManager
from utils import PokeberriesErrors

SOURCE_URL_ENV_NAME = 'POKEBERRIES_SOURCE_URL'
SOURCE_URL = None

app = Flask('PokeberriesStats')


@app.route('/')
def index():
    return "Pokeberries OK", 200


@app.route('/allBerryStats')
def all_berry_stats():
    """
    route defaults to method GET
    """
    start = time.time()
    berries = BerriesManager(SOURCE_URL)
    berries.get_berries_index()
    berries.get_berries_growth_time()
    finish = time.time()
    print('Process %i records in %f seconds' % (len(berries.growth_time_list), finish - start))

    # TBD: return the processed statistics
    return berries.berries_index, 200


@app.errorhandler(500)
def internal_error(error):
    return "Pokeberries Stats: Server error", 500


if __name__ == '__main__':
    SOURCE_URL = os.getenv(SOURCE_URL_ENV_NAME)
    if SOURCE_URL is None:
        raise PokeberriesErrors('The %s environment variable must be configured' % SOURCE_URL_ENV_NAME)
    app.run()
