import requests
import random
import string

BASE_URL = 'https://qa-scooter.education-services.ru/api/v1'

# создаём нового курьера
def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string

def register_new_courier_and_return_login_password():

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post(f'{BASE_URL}/courier', data=payload)

    if response.status_code == 201:
        return [login, password, first_name]
    return []

# удаляем курьера
def delete_courier_by_login(login, password):
    response = requests.post(f'{BASE_URL}/courier/login', data={"login": login, "password": password})
    courier_id = response.json()["id"]
    requests.delete(f'{BASE_URL}/courier/{courier_id}')

# авторизовываем курьера
def login_courier(login, password):
    return requests.post(f'{BASE_URL}/courier/login', data={"login": login, "password": password})