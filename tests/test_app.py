from http import HTTPStatus

import pytest
from fastapi.testclient import TestClient

from fastapi_zero import app as app_module


@pytest.fixture(autouse=True)
def reset_db():
    app_module.db = {
        1: app_module.Item(
            name='Caneca',
            description='Caneca térmica preta',
            price=39.90,
            tags=['quente', 'café'],
            type=app_module.ItemType.gadget,
        ),
        2: app_module.Item(
            name='Caderno',
            description='Caderno de anotações',
            price=24.50,
            tags=['papelaria'],
            type=app_module.ItemType.book,
        ),
    }


client = TestClient(app_module.app)


def test_read_root():
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'message': 'Olá! Acesse /items para testar o CRUD'
    }


def test_list_items():
    response = client.get('/items')

    assert response.status_code == HTTPStatus.OK
    payload = response.json()
    assert payload['count'] == len(app_module.db)
    assert payload['items'][0]['name'] == 'Caneca'


def test_filter_items_by_type():
    response = client.get('/items', params={'item_type': 'book'})

    assert response.status_code == HTTPStatus.OK
    payload = response.json()
    assert payload['count'] == 1
    assert payload['items'][0]['name'] == 'Caderno'


def test_read_existing_item():
    response = client.get('/items/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json()['name'] == 'Caneca'


def test_read_missing_item():
    response = client.get('/items/999')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json()['detail'] == 'Item não encontrado'


def test_create_item():
    response = client.post(
        '/items',
        json={
            'name': 'Mouse',
            'description': 'Mouse sem fio',
            'price': 89.90,
            'tags': ['periférico'],
            'type': 'gadget',
            'in_stock': True,
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    payload = response.json()
    assert payload['item_id'] == len(app_module.db)
    assert payload['item']['name'] == 'Mouse'


def test_update_item():
    response = client.put(
        '/items/1',
        json={
            'name': 'Caneca Premium',
            'description': 'Caneca térmica premium',
            'price': 49.90,
            'tags': ['quente'],
            'type': 'tool',
            'in_stock': False,
        },
    )

    assert response.status_code == HTTPStatus.OK
    payload = response.json()
    assert payload['item_id'] == 1
    assert payload['item']['name'] == 'Caneca Premium'
