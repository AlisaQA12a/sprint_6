import allure

from locators.locators import OrderLocators
from pages.base_page import BasePage
from URL import ORDERPAGE_URL

#страница заказа
class OrderPage(BasePage):
    url = ORDERPAGE_URL
    locators = OrderLocators
    pagelocator = locators.TITLE

    @allure.step('Открываем страницу заказа самоката')
    def open_order_page(self):
        self.open_site(self.url)
        self.wait_page_to_be_open()

    @allure.step('Заполняем первую форму')
    def fill_first_form(self, **faq_data):
        self.click_and_write_in_input(self.locators.FirstForm.NAME, faq_data.get("name"))
        self.click_and_write_in_input(self.locators.FirstForm.SURNAME, faq_data.get("surname"))
        self.click_and_write_in_input(self.locators.FirstForm.ADDRESS, faq_data.get("address"))
        self.click_and_write_in_input(self.locators.FirstForm.PHONE, faq_data.get("phone"))
        self.combobox_click_and_select(
            self.locators.FirstForm.STATION,
            self.locators.FirstForm.STATION_CLICK,
            faq_data.get("station"),
        )

    @allure.step('Нажимаем на кнопку далее')
    def submit_first_form_of_order(self):
        self.click_element(self.locators.FirstForm.BUTTON_NEXT)

    @allure.step('Ждем пока откроется вторая форма')
    def wait_for_second_form_open(self):
        self.wait_for(self.locators.SecondForm.TITLE)

    @allure.step('Заполняем вторую форму')
    def fill_second_form(self, **faq_data):
        self.click_and_write_in_input(self.locators.SecondForm.DATE, faq_data.get("data"))
        self.selectbox_select(
            self.locators.SecondForm.DURATION,
            self.locators.SecondForm.DURATION_OPTION,
            faq_data.get("duration"),
        )
        by, loc = self.locators.SecondForm.COLOR
        loc = loc.format(faq_data.get("color"))
        self.click_element((by, loc))
        self.click_and_write_in_input(self.locators.SecondForm.COMMENT, faq_data.get("comment"))

    @allure.step('Нажимаем  на кнопку Заказать')
    def submit_second_form_of_order(self):
        self.click_element(self.locators.SecondForm.BUTTON_NEXT)

    @allure.step('Ждем пока появится поп-ап')
    def wait_for_popup_appear(self):
        self.wait_for(self.locators.Popup.TITLE)

    @allure.step('Нажимаем на кнопку "Да"')
    def click_popup_yes(self):
        self.click_element(self.locators.Popup.BUTTON_YES)

    @allure.step('Ждем появления окна "Заказ оформлен"')
    def wait_for_ordered_successfully(self):
        return self.wait_for(self.locators.Popup.STATUS)

    @allure.step('Заказываем самокат')
    def order(self, faq_data):
        self.wait_page_to_be_open()

        # заполнить первую форму
        self.fill_first_form(**faq_data)
        self.submit_first_form_of_order()

        # ждем,когда откроется вторая форма
        self.wait_for_second_form_open()

        # заполнить вторую форму
        self.fill_second_form(**faq_data)
        self.submit_second_form_of_order()

        # ожидаем попап с подтверждением оформления заказа
        self.wait_for_popup_appear()

        # нажимаем "да"
        self.click_popup_yes()

        # ждем инфо об успешном заказе
        return self.wait_for_ordered_successfully()