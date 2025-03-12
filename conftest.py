import pytest
import random
from selenium import webdriver


@pytest.fixture
def driver():
    browser = webdriver.Firefox()
    browser.get('https://qa-scooter.praktikum-services.ru/')
    yield browser
    browser.quit()



