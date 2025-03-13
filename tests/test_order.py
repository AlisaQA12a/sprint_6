import allure

from pages.main_page import MainPage
from pages.order_page import OrderPage
from helpers import get_order_test_data


class TestOrderScooter:
    @allure.title('Тест заказа самоката кликом на верхнюю кнопку Заказать')
    def test_order_using_upper_button(self, driver):
        test_data = get_order_test_data()
        main_page = MainPage(driver)
        main_page.click_order_header()
        order_page = OrderPage(driver)
        assert order_page.order(test_data)

    @allure.title('Тест заказа самоката кликом на нижнюю кнопку Заказать')
    def test_order_using_below_button(self, driver):
        test_data = get_order_test_data()
        main_page = MainPage(driver)
        main_page.click_order_below()
        order_page = OrderPage(driver)
        assert order_page.order(test_data)
