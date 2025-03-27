import pytest
from flask import Flask
import os
from app.blueprints import web

@pytest.fixture
def client():
    app = Flask(__name__)
    app.config['TESTING'] = True

    # Configure template folder
    app.template_folder = os.path.join(os.path.dirname(__file__), '../templates')

    app.register_blueprint(web.bp)

    with app.test_client() as client:
        yield client


def test_index(client):
    response = client.get('/')
    assert response.status_code == 200

def test_about(client):
    response = client.get('/about')
    assert response.status_code == 200
    assert b'JovicDevelopers' in response.data