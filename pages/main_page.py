import allure

from locators.locators import MainPageLocators
from pages.base_page import BasePage
from URL import MAINPAGE_URL

#главная страница
class MainPage(BasePage):
    url = MAINPAGE_URL
    locators = MainPageLocators
    pagelocator = locators.TITLE

    @allure.step('Открываем сайт Яндекс Самокат')
    def open_yandex_scooter(self):
        self.open_site(self.url)
        self.wait_page_to_be_open()

    @allure.step('Скролим до блока  "Вопросы о важном"')
    def scroll_to_faq_list(self):
        self.scroll_to_element(self.locators.QUESTIONS)
        self.wait_for_visible(self.locators.QUESTIONS)

    @allure.step('Находим вопрос и кликаем по нему')
    def find_question_and_click(self, index):
        q_locator = self.locators.question_locator(index)
        a_locator = self.locators.answer_locator(index)
        self.scroll_to_element(q_locator)
        self.wait_for_visible(q_locator)
        self.click_element(q_locator)
        self.wait_for_visible(a_locator)

    @allure.step('Получаем текст вопроса')
    def get_question_text(self, index):
        q_locator = self.locators.question_locator(index)
        return self.get_text(q_locator)

    @allure.step('Получаем текст ответа')
    def get_answer_text(self, index):
        a_locator = self.locators.answer_locator(index)
        return self.get_text(a_locator)

    @allure.step('Нажимаем кнопку Заказать вверху страницы')
    def click_order_header(self):
        self.click_element(self.locators.ORDER_BUTTON_HEADER)

    @allure.step('Нажимаем кнопку Заказать внизу страницы')
    def click_order_below(self):
        self.scroll_to_element(self.locators.ORDER_BUTTON_BELOW)
        self.click_element(self.locators.ORDER_BUTTON_BELOW)