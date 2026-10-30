import pytest
from helpers import register_new_courier_and_return_login_password, login_courier, delete_courier_by_login

# фикстура регистрирует курьера и в конце теста удаляет его
@pytest.fixture
def courier():
    data = register_new_courier_and_return_login_password()
    login = data[0]
    password = data[1]
    response = login_courier(login, password)
    courier_id = response.json()["id"]
    yield login, password, courier_id
    delete_courier_by_login(login, password)