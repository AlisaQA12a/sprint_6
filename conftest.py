import pytest
from selenium import webdriver
from URL import BASE_URL


@pytest.fixture
def driver():
    browser = webdriver.Firefox()
    browser.get(BASE_URL)
    yield browser
    browser.quit()
