from flask import Flask

app = Flask('PokeberriesStats')


@app.route('/')
def index():
    return "OK"


@app.route('/allBerryStats')
def all_berry_stats():
    return "Test"


if __name__ == '__main__':
    app.run()
