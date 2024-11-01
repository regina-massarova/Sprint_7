import requests
import pytest
import allure
from helpers.data import BASE_URL, ORDER_TEST_DATA

@allure.epic("API тесты для заказов")
@allure.suite("Создание заказа")
class TestOrderCreation:

    @pytest.mark.parametrize("colors, expected_status, expected_response", [
        (["BLACK"], 201, "track"),
        (["GREY"], 201, "track"),
        (["BLACK", "GREY"], 201, "track"),
        ([], 201, "track")
    ])
    @allure.title("Создание заказа: разные варианты цветов")
    def test_create_order(self, colors, expected_status, expected_response):
        order_data = {
            "firstName": ORDER_TEST_DATA["firstName"],
            "lastName": ORDER_TEST_DATA["lastName"],
            "address": ORDER_TEST_DATA["address"],
            "metroStation": ORDER_TEST_DATA["metroStation"],
            "phone": ORDER_TEST_DATA["phone"],
            "rentTime": ORDER_TEST_DATA["rentTime"],
            "deliveryDate": ORDER_TEST_DATA["deliveryDate"],
            "comment": ORDER_TEST_DATA["comment"],
            "color": colors
        }

        with allure.step("Отправка запроса на создание заказа"):
            response = requests.post(f"{BASE_URL}/orders", json=order_data)

        assert response.status_code == expected_status, f"Ожидался код {expected_status}, получен {response.status_code}. Ответ: {response.text}"
        assert expected_response in response.json(), f"Ожидалось наличие {expected_response} в ответе. Ответ: {response.json()}"
