from selenium.webdriver.common.by import By


class SwitchPageLocators:
    # Локатор логотипа Самоката
    SCOOTER_LOGO_LOCATOR = By.XPATH, '//a[contains(@class, "Header_LogoScooter")]'
    # Локатор логотипа Яндекса
    YANDEX_LOGO_LOCATOR = By.XPATH, '//a[contains(@class, "Header_LogoYandex")]'
    # Локатор текста о Самокате на главной странице
    SCOOTER_MAIN_TEXT_LOCATOR = By.XPATH, '//div[contains(@class, "Home_Header")]'
    # Локатор заголовка "Новости" на странице Дзена
    DZEN_HEADER_NEWS_LOCATOR = By.XPATH, '//div[contains(text(),"Новости")]'
