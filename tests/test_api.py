import os

import pytest
from starlette.testclient import TestClient

from backend.main import app

API_BASE_URL = "/api/v1"


@pytest.fixture()
def test_app(monkeypatch):
    client = TestClient(app)
    yield client


def test_create(test_app: TestClient):
    files = {"file": open("tests/testdata/Gintama.jpg", "rb")}
    data = {"name": "test_name", "price": 20, "description": "Some description"}
    response = test_app.post(f"{API_BASE_URL}/items/", files=files, data=data)
    assert response.status_code == 201
    resp_data = response.json()
    data["id"] = resp_data["id"]
    data["image"] = "static/Gintama.jpg"
    assert response.json() == data


def test_read_all(test_app: TestClient):
    response = test_app.get(f"{API_BASE_URL}/items/")
    assert response.status_code == 200
    resp_data = response.json()
    data = {
        "name": "test_name",
        "price": 20,
        "image": "static/Gintama.jpg",
        "id": resp_data[0]["id"],
    }
    assert resp_data == [data]


def test_read_single(test_app: TestClient):
    response = test_app.get(f"{API_BASE_URL}/items/1")
    assert response.status_code == 200
    resp_data = response.json()
    data = {
        "name": "test_name",
        "description": "Some description",
        "price": 20,
        "image": "static/Gintama.jpg",
        "id": 1,
    }
    assert resp_data == data


def test_read_single_fail(test_app: TestClient):
    response = test_app.get(f"{API_BASE_URL}/items/100")
    assert response.status_code == 404


def test_delete(test_app: TestClient):
    response = test_app.delete(f"{API_BASE_URL}/items/", params={"id": 1})
    assert response.status_code == 204


def teardown_module(module):
    os.remove("data-test.db")
