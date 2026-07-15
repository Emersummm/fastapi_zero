from http import HTTPStatus

from jwt import decode

from fastapi_zero.security import ALGORITHM, SECRET_KEY, create_access_token


def test_jwt_token_creation():
    data = {'test': 'testuser'}
    token = create_access_token(data)
    decoded_token = decode(token, SECRET_KEY, algorithms=ALGORITHM)
    assert decoded_token['test'] == 'testuser'
    assert 'exp' in decoded_token


def test_jwt_invalid_token(client):
    response = client.delete(
        '/users/1', headers={'Authorization': 'Bearer token-invalido'}
    )

    assert response.status_code == HTTPStatus.UNAUTHORIZED
    assert response.json() == {'detail': 'Could not validate credentials'}
