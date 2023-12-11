# Pokeberries Stats

A Pokeberries statistics API


## Configuration
### Python
Developed and tested with: `Python 3.10.12`

### Dependencies
Install with:
`./pokeberries$ pip install -r requirements.txt`
(recommended Python virtual environment for local running)

### Environment variables
- `POKEBERRIES_PORT`
The PORT where the Pokeberries Stats App will be listening (suggested: 5005)

- `POKEBERRIES_SOURCE_URL`
The Berries endPoint complete url to be used as a source of information (e.g. https://pokeapi.co/api/v2/berry/)

### Containerized version
Steps:
- build image: `./pokeberries$ docker build -t pokeberries:latest .`
- run container: `./pokeberries$ docker run -d -e POKEBERRIES_PORT=5005 -e POKEBERRIES_SOURCE_URL=https://pokeapi.co/api/v2/berry/ --restart=always -p 5005:5005 pokeberries:latest`

(tested with Docker version 24.0.5)

## Usage
### Back-end start
`./pokeberries$ python3 app.py`

### Local usage (development mode)
To test the API listening OK:
`http://127.0.0.1:5005/`

To get Pokeberries statistics:
`http://127.0.0.1:5005/allBerryStats`

### Deployed version for testing usages
To test the API listening OK:
`https://archivoatsensus.pythonanywhere.com/`

To get Pokeberries statistics:
`https://archivoatsensus.pythonanywhere.com/allBerryStats`

## Tests
You can run unit and end-to-end basic tests (needs installed dependencies):
`./pokeberries$ python3 -m pytest -v`
