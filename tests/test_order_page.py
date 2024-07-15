import allure
import pytest

from locators.order_page_locators import OrderPageLocators
from page_object.order_page import OrderPage
from locators.main_page_locators import MainPageLocators
from conftest import driver


class TestsCreateOrder:

    @pytest.mark.parametrize('button_order, first_name, last_name, address, phone_number, comment', [(
                                                                                                     MainPageLocators.ORDER_BUTTON_HEADER,
                                                                                                     'Анна', 'Антонова',
                                                                                                     'г. Москва, Пушкинская пл., 1',
                                                                                                     '+79091244415',
                                                                                                     'Не звонить'), (
                                                                                                     OrderPageLocators.ORDER_BUTTON_BOTTOM,
                                                                                                     'Михаил', 'Пушкин',
                                                                                                     'ул. Гурьянова, 2',
                                                                                                     '+79161836354',
                                                                                                     '-')])
    @allure.title('Проверка успешного оформления заказа самоката')
    def test_create_success_order(self, driver, button_order, first_name, last_name, address, phone_number, comment):
        order_page = OrderPage(driver, 'https://qa-scooter.praktikum-services.ru/')
        order_page.open_page()
        success_order_text = order_page.create_order(button_order, first_name, last_name, address, phone_number,
                                                     comment)
        assert 'Заказ оформлен' in success_order_text
