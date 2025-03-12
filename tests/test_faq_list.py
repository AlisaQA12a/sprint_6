import allure
import pytest

from pages.main_page import MainPage
from faq_data import CHECK_FAQ_LIST_TEMPLATE


class TestFaqList:
    @allure.title('Проверка выпадающего списка в блоке "Вопросы о важном"')
    @allure.description('При нажатии на вопрос появляется соответствующий текст ответа ')
    @pytest.mark.parametrize('index,question, answer', CHECK_FAQ_LIST_TEMPLATE)
    def test_check_questions_list(self, driver, index, question, answer):
        main_page = MainPage(driver)
        main_page.scroll_to_faq_list()
        main_page.find_question_and_click(index)
        q_text = main_page.get_question_text(index)
        a_text = main_page.get_answer_text(index)
        assert q_text == question
        assert a_text == answer
