import requests
import allure
from helpers import generate_random_string, BASE_URL, delete_courier_by_login
import pytest

@allure.feature("Авторизация курьера")
class TestLoginCourier:

    @allure.title('Успешная авторизация курьера')
    def test_login_success(self, courier):
        login = courier[0]
        password = courier[1]
        payload = {'login':login,'password':password}
        response = requests.post(f'{BASE_URL}/courier/login',data=payload)
        assert response.status_code == 200
        assert "id" in response.json()


    @allure.title("Проверяем что при авторизации курьера падает ошибка, если не передать одно из обязательных полей")
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_login_courier_missing_field(self, courier,missing_field):
        login = courier[0]
        password = courier[1]
        payload = {'login': login, 'password': password}
        del payload[missing_field]
        response = requests.post(f'{BASE_URL}/courier/login',data=payload)
        assert response.status_code == 400
        assert response.json() == {'code': 400, 'message': 'Недостаточно данных для входа'}

    @allure.title("Попытка авторизации с неверным паролем")
    def test_login_courier_invalid_credentials(self,courier):
        login = courier[0]
        password = '12345'
        payload = {'login': login, 'password': password}
        response = requests.post(f'{BASE_URL}/courier/login', data=payload)
        assert response.status_code == 404
        assert response.json() == {'code': 404, "message": "Учетная запись не найдена"}


    @allure.title("Авторизация под несуществующим пользователем")
    def test_login_nonexistent_courier(self):
        payload = {
            "login": generate_random_string(10),
            "password": generate_random_string(10)}
        response = requests.post(f'{BASE_URL}/courier/login', data=payload)

        assert response.status_code == 404
        assert response.json() == {'code': 404, "message": "Учетная запись не найдена"}
