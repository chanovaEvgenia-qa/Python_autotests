import requests
import pytest

def test_statuscode():
    response = requests.get('https://petstore.swagger.io/v2/pet/5000')
    assert response.status_code == 200

def test_piece_of_body():
    response = requests.get('https://petstore.swagger.io/v2/pet/5000')
    assert response.json()['name'] == 'Flaffy'