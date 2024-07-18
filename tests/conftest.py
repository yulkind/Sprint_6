import pytest
from selenium import webdriver

from page_object.order_page import OrderPage
from url import Url


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


@pytest.fixture
def order_page(driver):
    return OrderPage(driver, Url.base_url)
