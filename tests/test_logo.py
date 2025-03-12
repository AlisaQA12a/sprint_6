import allure

from pages.main_page import MainPage
from pages.order_page import OrderPage
from URL import DZEN_URL


class TestLogo:

    @allure.title('Тестируем переход на главную страницу по лого Самокат')
    def test_logo_scooter(self, driver):
        order_page = OrderPage(driver)
        order_page.open_order_page()
        order_page.click_scooter_logo()
        main_page = MainPage(driver)
        assert main_page.wait_page_to_be_open()

    @allure.title('Тестируем переход на страницу ЯндексДзен по клику на логотип Яндекса')
    def test_logo_yandex(self, driver):
        main_page = MainPage(driver)
        main_page.open_yandex_scooter()
        main_page.click_yandex_logo()
        main_page.switch_tab()
        assert main_page.wait_for_url_change(DZEN_URL)




