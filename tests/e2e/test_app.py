
def test_index(app, client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.text == 'Pokeberries OK'


def test_all_berries(app, client):
    response = client.get('/allBerryStats')

    # check headers as required
    assert response.headers['Content-Type'] == 'application/json'

    # check basic integrity
    resp_as_dic = response.get_json()
    total_growth_time_freq = sum(list(resp_as_dic['frequency_growth_time'].values()))
    total_names = len(resp_as_dic['berries_names'])
    assert total_growth_time_freq == total_names
