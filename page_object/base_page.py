import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import main_page_locators
from locators.main_page_locators import MainPageLocators
from page_object.main_page import MainPage


class BasePage:
    def __init__(self, driver):
        self.driver = driver


    def get_question_element(self, question_number):
        return self.driver.find_element(main_page_locators, f'вопрос {question_number}')

    def get_answer_element(self, question_number):
        return self.driver.find_element(main_page_locators, f'ответ {question_number}')

    def click_question(self, question_number):
        self.get_question_element(question_number).click()

    def is_answer_displayed(self, question_number):
        return self.get_answer_element(question_number).is_displayed()

    @pytest.mark.parametrize("question_number", [1, 2, 3, 4, 5, 6, 7, 8])
    def test_faq(self, question_number):
        main_page = MainPage(self)
        main_page.click_question(question_number)
        assert main_page.is_answer_displayed(question_number), f"Нет ответа на вопрос {question_number}"







