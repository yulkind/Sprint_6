import allure

from locators.main_page_locators import MainPageLocators
from locators.switch_page_locators import SwitchPageLocators
from page_object.base_page import BasePage


class SwitchPage(BasePage):

    @allure.step('Принятие куки')
    def cookies_acceptation(self):
        self.click_on_element(MainPageLocators.COOKIE)

    @allure.step('Переход на главную страницу')
    def switch_to_scooter_page(self):
        self.click_on_element(SwitchPageLocators.SCOOTER_LOGO_LOCATOR)

    @allure.step('Нажатие на кнопку Заказать')
    def make_order(self, button):
        self.click_on_element(button)
    @allure.step('Переход на главную страницу')
    def switch_to_scooter_page(self):
        self.click_on_element(SwitchPageLocators.SCOOTER_LOGO_LOCATOR)

    @allure.step('Переход на страницу Дзена')
    def switch_to_dzen_page(self):
        self.click_on_element(SwitchPageLocators.YANDEX_LOGO_LOCATOR)
        self.switch_to_new_tab()

    @allure.step('Получение текста о Самокате на главной странице')
    def get_scooter_main_text(self):
        return self.get_text(SwitchPageLocators.SCOOTER_MAIN_TEXT_LOCATOR)

    @allure.step('Получение заголовка "Новости" на странице Дзена')
    def check_dzen_news_header(self):
        return self.find_element(SwitchPageLocators.DZEN_HEADER_NEWS_LOCATOR)