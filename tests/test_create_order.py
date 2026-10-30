import requests
import allure
from helpers import BASE_URL
import pytest

@allure.feature('Создание заказа')
class TestCreateOrder:

    @allure.title("Создание заказа с разными вариантами цветов")
    @pytest.mark.parametrize("color", [["BLACK"], ["GREY"], ["BLACK", "GREY"], []])
    def test_create_order_with_color(self, color):
        payload = {
        "firstName": "Илон",
        "lastName": "Маск",
        "address": "Космос, ул. Марсианская, д. 1",
        "metroStation": 1,
        "phone": "+7 999 888 77 66",
        "rentTime": 7,
        "deliveryDate": "2026-12-31",
        "comment": "привет",
        "color": color}

        response = requests.post(f'{BASE_URL}/orders', json=payload)
        assert response.status_code == 201
        assert 'track' in response.json()