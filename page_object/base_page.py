import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    @allure.step('Открытие ссылки')
    def open_page(self):
        self.driver.get(self.base_url)

    @allure.step('Поиск элемента по локатору')
    def find_element(self, locator):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Ожидание элемента по локатору')
    def wait_for_element(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step('Прокрутка до нужного элемента')
    def scroll_to_element(self, locator, timeout=5):
        element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    @allure.step('Клик по элементу')
    def click_on_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator)).click()

    @allure.step('Скролл до нужного элемента и клик по нему')
    def scroll_and_click_on_element(self, locator, timeout=5):
        self.scroll_to_element(locator, timeout)
        self.click_on_element(locator, timeout)

    @allure.step('Отображение текста по элементу')
    def get_text(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator)).text

    @allure.step('Переход на новую вкладку')
    def switch_to_new_tab(self):
        return self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step('Получение адреса текущей вкладки')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Получение отформатированных локаторов')
    def format_locators(self, locator_question, number):
        method, locator = locator_question
        locator = locator.format(number)
        return method, locator

    @allure.step('Получение данных в форме')
    def send_data(self, locator, value, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator)).send_keys(value)
