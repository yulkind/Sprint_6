import allure
import pytest

from page_object.main_page import MainPage
from answers import *


class TestMainPage:

    @allure.title('Проверка раздела "Вопросы о важном"')
    @allure.description('При нажатии на вопрос должен открываться текст ответа')
    @pytest.mark.parametrize('num, result', [(0, answer_1), (1, answer_2), (2, answer_3), (3, answer_4), (4, answer_5), (5, answer_6), (6, answer_7), (7, answer_8)])
    def test_click_faq_show_answers(self, driver, num, result):
        main_page = MainPage(driver)
        main_page.scroll_to_element()
        assert main_page.get_answer_text(num) == result
