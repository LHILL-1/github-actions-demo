import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'app'))

import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home_returns_200(client):
    """Home endpoint should return 200 OK"""
    response = client.get("/")
    assert response.status_code == 200


def test_home_returns_message(client):
    """Home endpoint should return expected message"""
    response = client.get("/")
    data = response.get_json()
    assert data["message"] == "Hello from FRESHKIDS!"
    assert data["status"] == "running"


def test_health_endpoint(client):
    """Health check endpoint should return healthy"""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "healthy"


def test_add_endpoint(client):
    """Add endpoint should correctly sum two numbers"""
    response = client.get("/add/3/7")
    assert response.status_code == 200
    data = response.get_json()
    assert data["result"] == 10


def test_add_large_numbers(client):
    """Add endpoint should handle larger numbers"""
    response = client.get("/add/100/200")
    data = response.get_json()
    assert data["result"] == 300
