import allure
from locators.order_page_locators import OrderPageLocators
from page_object.base_page import BasePage


class OrderPage(BasePage):
    def create_order(self, button_order, first_name, last_name, address, phone_number, comment):
        self.scroll_and_click_on_element(button_order)
        self.send_data(OrderPageLocators.FIRST_NAME, first_name)
        self.send_data(OrderPageLocators.LAST_NAME, last_name)
        self.send_data(OrderPageLocators.ADDRESS, address)
        self.click_on_element(OrderPageLocators.STATIONS)
        self.scroll_and_click_on_element(OrderPageLocators.STATION_METRO)
        self.send_data(OrderPageLocators.PHONE, phone_number)
        self.click_on_element(OrderPageLocators.BUTTON_NEXT)
        self.click_on_element(OrderPageLocators.DATE)
        self.click_on_element(OrderPageLocators.DAY)
        self.click_on_element(OrderPageLocators.RENTAL_PERIOD)
        self.click_on_element(OrderPageLocators.OPTION)
        self.click_on_element(OrderPageLocators.CHECKBOX_BLACK)
        self.send_data(OrderPageLocators.COMMENT, comment)
        self.click_on_element(OrderPageLocators.ORDER_BUTTON)
        self.click_on_element(OrderPageLocators.YES_BUTTON)
        success_order_text = self.get_text(OrderPageLocators.SUCCESS_ORDER_TEXT)
        return success_order_text
