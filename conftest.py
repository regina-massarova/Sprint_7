import requests
import pytest
from helpers.data import BASE_URL
from helpers.register_new_courier import generate_courier_data

@pytest.fixture
def setup_courier():
    courier_data = generate_courier_data()
    response = requests.post(f"{BASE_URL}/courier", json=courier_data)
    assert response.status_code == 201, f"Не удалось создать курьера: {response.text}"
    return courier_data
