import requests
import allure
from urls import GET_ORDERS_LIST


@allure.feature('Получение списка заказов')
class TestGetOrdersList:

    @allure.title('Получение списка заказов')
    def test_get_orders_list_success(self):
        response = requests.get(GET_ORDERS_LIST)
        assert response.status_code == 200
        assert 'orders' in response.json()
        assert isinstance(response.json()['orders'], list)