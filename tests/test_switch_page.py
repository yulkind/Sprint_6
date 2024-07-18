import allure
from locators.main_page_locators import MainPageLocators
from page_object.switch_page import SwitchPage
from text import Texts
from url import Url


class TestSwitchPage:
    @allure.title('Проверка перехода на главную страницу Самоката по клику на логотип Самоката')
    def test_switch_to_main_page_from_order_page(self, driver):
        switch_page = SwitchPage(driver, Url.base_url)
        switch_page.open_page()
        switch_page.click_on_element(MainPageLocators.ORDER_BUTTON_HEADER)
        switch_page.switch_to_scooter_page()
        assert Texts.scooter_main_text_expected in switch_page.get_scooter_main_text()

    @allure.title('Проверка перехода на Дзен по клику на лого Дзена')
    def test_switch_to_dzen_from_order_page(self, driver):
        switch_page = SwitchPage(driver, Url.base_url)
        switch_page.open_page()
        switch_page.click_on_element(MainPageLocators.ORDER_BUTTON_HEADER)
        switch_page.switch_to_dzen_page()
        assert switch_page.check_dzen_news_header()
