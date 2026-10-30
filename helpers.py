import random
import string
import allure

@allure.step("Генерация случайной строки длиной {length}")
def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string