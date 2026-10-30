import requests
import pytest
import allure
from helpers import generate_random_string
from api import delete_courier_by_login
from urls import CREATE_COURIER
from data import MSG_LOGIN_BUSY, MSG_MISSING_CREATE_FIELDS


@allure.feature("Создание курьера")
class TestCreateCourier:

    @allure.title("Успешное создание курьера")
    def test_create_courier_success(self):
        payload = {
            "login": generate_random_string(10),
            "password": generate_random_string(10),
            "firstName": generate_random_string(10)
        }
        response = requests.post(CREATE_COURIER, data=payload)
        delete_courier_by_login(payload["login"], payload["password"])
        assert response.status_code == 201
        assert response.json() == {'ok': True}

    @allure.title("Пытаемся создать курьера, который уже есть в базе")
    def test_create_double_courier(self):
        payload = {
            "login": generate_random_string(10),
            "password": generate_random_string(10),
            "firstName": generate_random_string(10)
        }
        requests.post(CREATE_COURIER, data=payload)
        response = requests.post(CREATE_COURIER, data=payload)
        delete_courier_by_login(payload["login"], payload["password"])
        assert response.status_code == 409
        assert response.json() == MSG_LOGIN_BUSY

    @allure.title("Проверяем что при создании курьера падает ошибка, если не передать одно из обязательных полей")
    @pytest.mark.parametrize("missing_field", ["login", "password", "firstName"])
    def test_create_courier_missing_field(self, missing_field):
        payload = {
            "login": generate_random_string(10),
            "password": generate_random_string(10),
            "firstName": generate_random_string(10)
        }
        del payload[missing_field]
        response = requests.post(CREATE_COURIER, data=payload)
        assert response.status_code == 400
        assert response.json() == MSG_MISSING_CREATE_FIELDS