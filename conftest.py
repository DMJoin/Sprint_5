import pytest
from selenium import webdriver
import random

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://qa-desk.stand.praktikum-services.ru/")
    yield driver
    driver.quit()

@pytest.fixture
def generate_email():
    email = random.randint(100, 9999)
    new_email = f'testmail{email}@gmail.com'
    return new_email

@pytest.fixture
def wrong_generate_email():
    email_wrong = random.randint(100, 9999)
    new_email_wrong = f'testmail{email_wrong}&gmail.com'
    return new_email_wrong