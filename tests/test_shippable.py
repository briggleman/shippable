import pytest
import json

from shippable.factory import create_app


@pytest.fixture
def app(request):
    config = {
        "TESTING": True
    }

    app = create_app(config)

    with app.app_context():
        yield app

@pytest.fixture
def client(request, app):
    client = app.test_client()
    return client

def index(client):
    return client.get("/", follow_redirects=True)

def test_get_index(client, app):
    rv = client.get("/")
    assert rv.data == b'{"response": "hello world!"}'
    assert rv.status_code == 200

def test_post_index(client, app):
    rv = client.post("/?foo=bar")
    assert rv.status_code != 200

def test_get_ping(client, app):
    rv = client.get("/ping")
    assert rv.data == b'{"ping": "pong!"}'
    assert rv.status_code == 200

def test_post_ping(client, app):
    rv = client.post("/?foo=bar")
    assert rv.status_code != 200