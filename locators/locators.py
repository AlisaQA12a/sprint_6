from selenium.webdriver.common.by import By

#локаторы, которые есть на всех страницах
class UniversalLocators:

    LOGO_YANDEX = (By.XPATH, ".//*[@alt='Yandex']")  # логотип Яндекса
    LOGO_SCOOTER = (By.XPATH, ".//*[@alt='Scooter']")  # логотип Самоката

#локаторы главной страницы
class MainPageLocators(UniversalLocators):

    TITLE = (By.XPATH, "//div[starts-with(@class, 'Home_Header__')]") #локатор заголовка страницы
    BUTTON_COOCKIE = (By.XPATH, "//button[text()='да все привыкли']") #кнопка принятия куки
    QUESTIONS = (By.CLASS_NAME, "accordion")  #блок вопросов о важном
    QUESTION = (
        By.XPATH,
        "//div[starts-with(@class, 'Home_FAQ__')]//div[@class='accordion__item'][{}]//div[@class='accordion__button']"
    ) #локатор вопроса
    ANSWER = (
        By.XPATH,
        "//div[starts-with(@class, 'Home_FAQ__')]//div[@class='accordion__item'][{}]//div[@class='accordion__panel']"
    ) #локатор ответа

    ORDER_BUTTON_HEADER = (By.XPATH, "(//button[text()='Заказать'])[1]")  # кнопка заказать вверху главной страницы
    ORDER_BUTTON_BELOW = (By.XPATH, "(//button[text()='Заказать'])[2]")  # кнопка заказать в блоке Как это работает

    # функция подставляет вместо {} переданный индекс вопроса от 1 до 8
    @classmethod
    def question_locator(cls, index):
        by, loc = cls.QUESTION
        return by, loc.format(index)

    # функция подставляет вместо {} переданный индекс ответа от 1 до 8
    @classmethod
    def answer_locator(cls, index):
        by, loc = cls.ANSWER
        return by, loc.format(index)

#локаторы страницы заказа
class OrderLocators(UniversalLocators):

    TITLE = (By.XPATH, "//div[text()='Для кого самокат']") #локатор заголовка страницы, по которому проверяется, что открылась нужная страница

    #локаторы первой формы заказа
    class FirstForm:
        TITLE = (By.XPATH, "//div[text()='Для кого самокат']")
        BUTTON_NEXT = (By.XPATH, "//button[text()='Далее']") #кнопка далее
        NAME = (By.XPATH, "//input[@placeholder='* Имя']") #инпут имя
        SURNAME = (By.XPATH, "//input[@placeholder='* Фамилия']") #инпут фамилия
        ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']") #инпут адрес
        STATION = (By.XPATH, "//input[@placeholder='* Станция метро']") #инпут станция метро
        STATION_CLICK = (By.CLASS_NAME, "select-search__select") #клик по станции метро
        PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']") #инпут номера телефона

    #локаторы второй формы заказа
    class SecondForm:
        TITLE = (By.XPATH, "//div[text()='Про аренду']")
        BUTTON_NEXT = (By.XPATH, "//div[starts-with(@class, 'Order_Buttons__')]/button[text()='Заказать']") #кнопка далее
        DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']") #инпут дата
        DURATION = (
            By.XPATH,
            "//div[@class='Dropdown-placeholder' and text()='* Срок аренды']/parent::*//span[@class='Dropdown-arrow']"
        ) #срок аренды
        DURATION_OPTION = (
            By.XPATH,
            "//div[@class='Dropdown-placeholder' and text()='* Срок аренды']/parent::*"
            "/parent::*//div[@class='Dropdown-option' and text()='{}']"
        ) #варианты срока аренды
        COLOR = (By.XPATH, "//label[@for='{}']") #выбор цвета самоката
        COLOR_BLACK = (By.XPATH, "//label[@for='black']") #цвет черный жемчуг
        COLOR_GREY = (By.XPATH, "//label[@for='grey']") #цвет серая безысходность
        COMMENT = (By.XPATH, ".//*[@placeholder='Комментарий для курьера']") #инпут комментария для курьера

    #локаторы модального окна при подтверждении заказа
    class Popup:
        TITLE = (By.XPATH, "//div[starts-with(@class, 'Order_ModalHeader__') and text()='Хотите оформить заказ?']") #заголовок
        STATUS = (By.XPATH, "//div[text()='Заказ оформлен']") #заказ оформлен
        BUTTON_YES = (By.XPATH, "//button[text()='Да']") #кнопка подтверждения хакаха
        BUTTON_STATUS = (By.XPATH, "//button[text()='Посмотреть статус']") #кнопка посмотреть статус