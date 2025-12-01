import pytest
from unittest.mock import patch
from source.app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_ask_endpoint_no_data(client):

    response = client.post("/api/ask", json={})

    assert response.status_code == 400
    assert "error" in response.get_json()


def test_ask_endpoint_missing_topic(client):
 
    payload = {"pergunta_errada": "Qualquer coisa"}
    response = client.post("/api/ask", json=payload)

    assert response.status_code == 400
    assert "topic" in response.get_json()["error"]


@patch("source.routes.routes.get_ai_response")
def test_ask_endpoint_success(mock_get_ai, client):
 
    mock_get_ai.return_value = "Esta é uma resposta simulada da IA."

    payload = {"topic": "Docker"}
    response = client.post("/api/ask", json=payload)

    assert response.status_code == 200  
    data = response.get_json()
    assert data["response"] == "Esta é uma resposta simulada da IA."

    mock_get_ai.assert_called_once()
