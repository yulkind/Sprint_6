from selenium.webdriver.common.by import By
import random


class OrderPageLocators:
    # Локатор поля "Имя"
    FIRST_NAME = (By.XPATH, './/input[@placeholder= "* Имя"]')
    # Локатор поля "Фамилия"
    LAST_NAME = (By.XPATH, './/input[@placeholder= "* Фамилия"]')
    # Локатор поля "Адрес"
    ADDRESS = (By.XPATH, './/input[@placeholder= "* Адрес: куда привезти заказ"]')
    # Локатор поля "Станция метро"
    STATIONS = (By.XPATH, './/input[@placeholder= "* Станция метро"]')
    # Локатор строки "Станция метро"
    STATION_METRO = (By.XPATH, f'.//li[@data-value= "{random.randint(8, 100)}"]')
    # Локатор строки "Телефон"
    PHONE = (By.XPATH, './/input[@placeholder= "* Телефон: на него позвонит курьер"]')
    # Локатор кнопки "Далее"
    BUTTON_NEXT = (By.XPATH, './/button[contains(text(), "Далее")]')
    # Локатор поля "Когда"
    DATE = (By.XPATH, './/input[@placeholder= "* Когда привезти самокат"]')
    # Локатор даты 31 июля
    DAY = (By.XPATH, '//div[contains(text(),"31")]')
    # Локатор поля "Срок аренды"
    RENTAL_PERIOD = (By.XPATH, './/div[contains(text(), "Срок аренды")]')
    # Локатор опции "Сутки"
    OPTION = (By.XPATH, './/div[contains(text(), "сутки")]')
    # Локатор чекбокса с опцией "чёрный жемчуг" поля "Цвет самоката"
    CHECKBOX_BLACK = (By.XPATH, './/input[@id="black"]')
    # Локатор поля "Комментарий"
    COMMENT = (By.XPATH, './/input[@placeholder= "Комментарий для курьера"]')
    # Локатор кнопки "Заказать"
    ORDER_BUTTON = (By.XPATH, './/div[@class="Order_Buttons__1xGrp"]/button[contains(text(), "Заказать")]')
    # Локатор кнопки "Да"
    YES_BUTTON = (By.XPATH, './/button[contains(text(), "Да")]')
    # Локатор текста с успешным оформлением заказа
    SUCCESS_ORDER_TEXT = (By.XPATH, './/div[contains(text(), "Заказ оформлен")]')
