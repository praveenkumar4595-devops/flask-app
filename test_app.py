import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home_status_code(client):
    """Test that the home route returns status code 200."""
    response = client.get("/")
    assert response.status_code == 200

def test_home_content(client):
    """Test that the home route returns the expected content."""
    response = client.get("/")
    # Update the expected text based on your app
    assert b"Hello, Flask App running on Docker!" in response.data
