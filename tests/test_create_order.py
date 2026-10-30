import requests
import allure
import pytest
from urls import CREATE_ORDER
from data import BASE_ORDER_PAYLOAD


@allure.feature('Создание заказа')
class TestCreateOrder:

    @allure.title("Создание заказа с разными вариантами цветов")
    @pytest.mark.parametrize("color", [["BLACK"], ["GREY"], ["BLACK", "GREY"], []])
    def test_create_order_with_color(self, color):
        payload = BASE_ORDER_PAYLOAD.copy()
        payload["color"] = color

        response = requests.post(CREATE_ORDER, json=payload)

        assert response.status_code == 201
        assert 'track' in response.json()