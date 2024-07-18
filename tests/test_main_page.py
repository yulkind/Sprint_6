import allure
import pytest

from page_object.main_page import MainPage
from answers import *
from url import Url


class TestMainPage:

    @allure.title('Проверка раздела "Вопросы о важном"')
    @allure.description('При нажатии на вопрос открывается корректный ответ')
    @pytest.mark.parametrize('number, result', [(0, answer_1), (1, answer_2), (2, answer_3), (3, answer_4), (4, answer_5), (5, answer_6), (6, answer_7), (7, answer_8)])
    def test_click_faq_show_answers(self, driver, number, result):
        main_page = MainPage(driver, Url.base_url)
        main_page.open_page()
        text = main_page.get_answer_text(number)
        assert text == result
