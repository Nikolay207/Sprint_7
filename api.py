import requests
import allure
from urls import CREATE_COURIER, LOGIN_COURIER, DELETE_COURIER
from helpers import generate_random_string

@allure.step("Регистрация нового курьера")
def register_new_courier_and_return_login_password():
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post(CREATE_COURIER, data=payload)

    if response.status_code == 201:
        return [login, password, first_name]
    return []

@allure.step("Авторизация курьера")
def login_courier(login, password):
    return requests.post(LOGIN_COURIER, data={"login": login, "password": password})

@allure.step("Удаление курьера")
def delete_courier_by_login(login, password):
    response = requests.post(LOGIN_COURIER, data={"login": login, "password": password})
    if response.status_code == 200:
        courier_id = response.json()["id"]
        requests.delete(f'{DELETE_COURIER}/{courier_id}')