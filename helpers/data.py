
BASE_URL = "https://qa-scooter.praktikum-services.ru/api/v1"

ORDER_TEST_DATA = {
    "firstName": "Регина",
    "lastName": "Массарова",
    "address": "Москва, Тверская 43.",
    "metroStation": 2,
    "phone": "+7 937 777 55 35",
    "rentTime": 4,
    "deliveryDate": "2024-10-30",
    "comment": "Позвоните за 30 минут"
}

ERROR_MESSAGES = {
    "duplicate_login": "Этот логин уже используется. Попробуйте другой.",
    "missing_field": "Недостаточно данных для создания учетной записи",
    "account_not_found": "Учетная запись не найдена",
    "invalid_field": "Ожидался код {expected}, получен {actual}. Ответ: {response}"
}
