import requests

def test_single_user():
    url = 'https://reqres.in/api/users/1'
    res = requests.get(url)
    assert res.status_code == 200
    assert res.headers['Content-Type'] == 'application/json; charset=utf-8'
    user = res.json()['data']
    assert 'id' in user
    assert 'email' in user


def test_create_user():
    url = 'https://reqres.in/api/users/'
    data  = {
        "name": "test",
        "job": "test"
    }
    res = requests.post(url, data)
    assert res.status_code == 201
    assert res.headers['Content-Type'] == 'application/json; charset=utf-8'
    user = res.json()
    assert data['name'] in user['name']
    assert data['job'] in user['job']

def test_update_user():
    url = 'https://reqres.in/api/users/2'
    data  = {
        "name": "test",
        "job": "test"
    }
    res = requests.put(url, data)
    assert res.status_code == 200
    assert res.headers['Content-Type'] == 'application/json; charset=utf-8'
    user = res.json()
    assert data['name'] in user['name']
    assert data['job'] in user['job']

def test_delete_user():
    url = 'https://reqres.in/api/users/2'
    res = requests.delete(url)
    assert res.status_code == 204
    assert res.content == b''
