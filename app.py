import os
import time
from flask import Flask, jsonify
import logging

from berries import BerriesManager
from utils import PokeberriesErrors

SOURCE_URL_ENV_NAME = 'POKEBERRIES_SOURCE_URL'
PORT_ENV_NAME = 'POKEBERRIES_PORT'
SOURCE_URL = None
PORT = None
DEV_HOST = '0.0.0.0'

app_config = False

logging.basicConfig(level=logging.INFO)
log = logging.getLogger()

app = Flask('PokeberriesStats')


@app.route('/')
def index():
    return "Pokeberries OK", 200


@app.route('/allBerryStats')
def all_berry_stats():
    """
    Flask route defaults to the required method GET
    """
    if not app_config:
        load_config()

    start = time.time()
    berries = BerriesManager(SOURCE_URL)
    berries.get_berries_index()
    berries.get_berries_growth_time()
    berries.process_statistics()
    finish = time.time()
    log.info('Processed %i records in %f seconds' % (len(berries.growth_time_list), finish - start))

    # Flask jsonify provides the required ``application/json`` Content-Type (mimetype)
    return jsonify(berries.statistics)


@app.errorhandler(500)
def internal_error(error):
    return "Pokeberries Stats: Server error", 500


def load_config():
    global app_config, SOURCE_URL, PORT
    SOURCE_URL = os.getenv(SOURCE_URL_ENV_NAME)
    PORT = os.getenv(PORT_ENV_NAME)
    if SOURCE_URL is None or PORT is None:
        raise PokeberriesErrors('Some environment variables need to be configured, check README')
    app_config = True


if __name__ == '__main__':
    load_config()
    app.run(host=DEV_HOST, port=PORT)
