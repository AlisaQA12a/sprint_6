from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


# сюда вынесены общие элементы для всех страниц
class BasePage:

    def __init__(self, driver):
        self.driver = driver

    # переключение вкладки браузера
    def switch_tab(self):
        return self.driver.switch_to.window(self.driver.window_handles[-1])

    # открывает страницу по урлу
    def open_site(self, url):
        self.driver.get(url)

    # найти элемент по локатору
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    # нажать на элемент по локатору
    def click_element(self, locator):
        self.find_element(locator).click()

    # скролл до элемента
    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.wait_for_visible(locator)

    # ожидание появления элемента
    def wait_for(self, locator):
        return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(locator))

    # получение текста элемента
    def get_text(self, locator):
        return self.find_element(locator).text

    # ожидание видимости элемента
    def wait_for_visible(self, locator):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))

    # ожидание кликабельности элемента
    def wait_for_clickable(self, locator):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator))

    # ожидание смены урлы
    def wait_for_url_change(self, url):
        return WebDriverWait(self.driver, 5).until(EC.url_to_be(url))

    # ввод текста в инпуты
    def send_keys(self, locator, text):
        self.find_element(locator).send_keys(text)

    # клик по инпуту с последующим вводом текста
    def click_and_write_in_input(self, locator, text):
        self.click_element(locator)
        self.send_keys(locator, text)

    # клик по дропдауну с последующим выбором опции
    def combobox_click_and_select(self, locator_value, locator_select, option):
        self.click_element(locator_value)
        self.send_keys(locator_value, option)
        self.click_element(locator_select)

    # клик по дропдауну с выбором последующей опции по локатору выпадающего списка и тексту опции
    def selectbox_select(self, locator_base, locator_option, option):
        self.click_element(locator_base)
        by, loc = locator_option
        loc = loc.format(option)
        locator_option = by, loc
        self.click_element(locator_option)

    # ожидание открытия страницы и видимости заголовка
    def wait_page_to_be_open(self, url, page_locator):
        self.wait_for_url_change(url)
        return self.wait_for(page_locator)
