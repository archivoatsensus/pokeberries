# Pokeberries Stats

A Pokeberries statistics API


## Configuration
### Python
Developed and tested with: `Python 3.10.12`

### Dependencies
Install with (recommended virtual environment for local running):
`./pokeberries$ pip install -r requirements.txt`

### Environment variables
- `POKEBERRIES_PORT`
The PORT where the Pokeberries Stats App will be listening (recommended: 5005)

- `POKEBERRIES_SOURCE_URL`
The Berries endPoint complete url to be used as a source of information (e.g. https://pokeapi.co/api/v2/berry/)


## Usage
### Back-end start
`./pokeberries$ python3 app.py`

### Local usage
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
You can run unit and end-to-end tests (needs installed dependencies):
`./pokeberries$ python3 -m pytest -v`

