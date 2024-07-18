from selenium.webdriver.common.by import By


class MainPageLocators:

    # Локатор заголовка раздела "Вопросы о важном"
    FAQ_SECTION = By.XPATH, '//div[contains(text(),"Вопросы о важном")]'

    # Локаторы вопросов раздела "Вопросы о важном"
    FAQ_QUESTION = By.XPATH, '//div[@id="accordion__heading-{}"]'

    # Локаторы ответов раздела "Вопросы о важном"
    FAQ_ANSWER = By.XPATH, './/div[@id="accordion__panel-{}"]'

    # Локатор кнопки "Заказать" в верхней части страницы
    ORDER_BUTTON_HEADER = By.XPATH, '//div[@class = "Header_Nav__AGCXC"]/button[text() = "Заказать"]'

    # Локатор кнопки "Заказать" в нижней части страницы
    ORDER_BUTTON_BOTTOM = By.XPATH, '//div[contains(@class, "Home_FinishButton")]/button'

    # Локатор кнопки "Ок" для куки
    COOKIE = By.XPATH, './/button[@id="rcc-confirm-button"]'

    # Локатор логотипа самоката
    SCOOTER_LOGO_HEADER = By.XPATH, '//a[contains(@class, "Header_LogoScooter")]'


