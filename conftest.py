import requests
import pytest
from helpers.data import BASE_URL
from helpers.register_new_courier import generate_courier_data


@pytest.fixture
def setup_courier():

    courier_data = generate_courier_data()
    response = requests.post(f"{BASE_URL}/courier", json=courier_data)


    response.raise_for_status()
    print("Ответ на создание курьера:", response.json())


    login_response = requests.post(f"{BASE_URL}/courier/login", json={
        "login": courier_data["login"],
        "password": courier_data["password"]
    })

    login_response.raise_for_status()
    courier_id = login_response.json().get("id")

    if not courier_id:
        pytest.fail(f"Не удалось получить ID курьера после создания и логина. Ответ API: {login_response.json()}")

    yield courier_data

    delete_response = requests.delete(f"{BASE_URL}/courier/{courier_id}", json={"id": courier_id})
    delete_response.raise_for_status()
    if not delete_response.json().get("ok"):
        pytest.fail(f"Не удалось удалить курьера: {delete_response.text}")
