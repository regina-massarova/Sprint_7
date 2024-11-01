import requests
import pytest
import allure
from helpers.data import BASE_URL, ERROR_MESSAGES
from helpers.register_new_courier import generate_courier_data


@allure.epic("API тесты для курьеров")
@allure.suite("Создание курьера")
class TestCourierCreation:

    @allure.title("Создание курьера: успешный случай")
    def test_create_courier_success(self):
        courier_data = generate_courier_data()

        with allure.step("Отправка запроса на создание курьера"):
            response = requests.post(f"{BASE_URL}/courier", json=courier_data)

        assert response.status_code == 201, ERROR_MESSAGES["invalid_field"].format(expected=201, actual=response.status_code, response=response.text)
        assert response.json().get("ok") is True, "Ожидался ответ {'ok': true}"

    @allure.title("Создание курьера: попытка создать дубликат")
    def test_create_duplicate_courier(self):
        courier_data = generate_courier_data()

        requests.post(f"{BASE_URL}/courier", json=courier_data)
        with allure.step("Отправка запроса на создание дубликата курьера"):
            response_second = requests.post(f"{BASE_URL}/courier", json=courier_data)

        assert response_second.status_code == 409, ERROR_MESSAGES["invalid_field"].format(expected=409, actual=response_second.status_code, response=response_second.text)
        assert response_second.json().get("message") == ERROR_MESSAGES["duplicate_login"], "Ожидалось сообщение об ошибке дублирования логина"

    @pytest.mark.parametrize("field", ["login", "password"])
    @allure.title("Создание курьера: отсутствие обязательного поля")
    def test_create_courier_missing_field(self, field):
        courier_data = generate_courier_data()
        courier_data_dict = courier_data.copy()
        courier_data_dict.pop(field)

        with allure.step(f"Отправка запроса на создание курьера без поля: {field}"):
            response = requests.post(f"{BASE_URL}/courier", json=courier_data_dict)

        assert response.status_code == 400, ERROR_MESSAGES["invalid_field"].format(expected=400, actual=response.status_code, response=response.text)
        assert response.json().get("message") == ERROR_MESSAGES["missing_field"], "Ожидалось сообщение об ошибке отсутствия поля"
