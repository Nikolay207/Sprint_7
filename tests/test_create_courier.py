import requests
import pytest
import allure
from helpers import generate_random_string, BASE_URL, delete_courier_by_login

@allure.feature("Создание курьера")
class TestCreateCourier:

    @allure.title("Успешное создание курьера")
    def test_create_courier_success(self):
        payload = {
            "login": generate_random_string(10),
            "password": generate_random_string(10),
            "firstName": generate_random_string(10)}
        response = requests.post(f'{BASE_URL}/courier',data=payload)
        assert response.status_code == 201
        assert response.json() == {'ok':True}
        delete_courier_by_login(payload["login"], payload["password"])

    @allure.title("Пытаемся создать курьера, который уже есть в базе")
    def test_create_duble_courier(self):
        payload = {
            "login": generate_random_string(10),
            "password": generate_random_string(10),
            "firstName": generate_random_string(10)}
        response = requests.post(f'{BASE_URL}/courier',data=payload)
        response = requests.post(f'{BASE_URL}/courier',data=payload)
        assert response.status_code == 409
        assert response.json() == {'code': 409, 'message': 'Этот логин уже используется. Попробуйте другой.'}
        delete_courier_by_login(payload["login"], payload["password"])

    @allure.title("Проверяем что при создании курьера падает ошибка, если не передать одно из обязательных полей")
    @pytest.mark.parametrize("missing_field", ["login", "password", "firstName"])
    def test_create_courier_missing_field(self, missing_field):
        payload = {
            "login": generate_random_string(10),
            "password": generate_random_string(10),
            "firstName": generate_random_string(10)}
        del payload[missing_field]
        response = requests.post(f'{BASE_URL}/courier',data=payload)
        assert response.status_code == 400
        assert response.json() == {"code": 400,"message": "Недостаточно данных для создания учетной записи"}

