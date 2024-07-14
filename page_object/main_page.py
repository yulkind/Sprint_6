from locators.main_page_locators import MainPageLocators
from page_object.base_page import BasePage


class MainPage(BasePage):
    #@allure.step('Проскроллить до секции "Вопросы о важном"')
    def scroll_to_faq_section(self):
        self.scroll_to_faq(MainPageLocators.FAQ_SECTION)

    #@allure.step('Кликнуть на нужный номер вопроса в аккордеоне "Вопросы о важнoм"')
    def click_on_faq_items(self, num):
        self.click_on_element(MainPageLocators.FAQ_QUESTION)

    #@allure.step('Получение текста ответа')
    def get_displayed_text_from_faq_answer(self, num):
        return self.get_text_on_element(MainPageLocators.FAQ_ANSWER)

    def get_answer_text(self, num):
        locator_q_formated = self.format_locators(MainPageLocators.FAQ_QUESTION, num)
        locator_a_formated = self.format_locators(MainPageLocators.FAQ_ANSWER, num)
        self.click_on_element(locator_q_formated)
        return self.get_text_from_element(locator_a_formated)
