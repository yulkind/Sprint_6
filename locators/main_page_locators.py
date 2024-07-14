from selenium.webdriver.common.by import By


class MainPageLocators:

    #FAQ
    FAQ_SECTION = By.XPATH, '//div[contains(text(),"Вопросы о важном")]'
    FAQ_QUESTION_1 = By.XPATH, '//div[@id="accordion__heading-0"]'
    FAQ_QUESTION_2 = By.XPATH, '//div[@id="accordion__heading-1"]'
    FAQ_QUESTION_3 = By.XPATH, '//div[@id="accordion__heading-2"]'
    FAQ_QUESTION_4 = By.XPATH, '//div[@id="accordion__heading-3"]'
    FAQ_QUESTION_5 = By.XPATH, '//div[@id="accordion__heading-4"]'
    FAQ_QUESTION_6 = By.XPATH, '//div[@id="accordion__heading-5"]'
    FAQ_QUESTION_7 = By.XPATH, '//div[@id="accordion__heading-6"]'
    FAQ_QUESTION_8 = By.XPATH, '//div[@id="accordion__heading-7"]'

    FAQ_ANSWER_1 = By.XPATH, '//p[contains(text(),"Сутки — 400 рублей. Оплата курьеру — наличными или картой.")]'
    FAQ_ANSWER_2 = By.XPATH, '//p[contains(text(),"Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.")]'
    FAQ_ANSWER_3 = By.XPATH, '//p[contains(text(),"Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.")]'
    FAQ_ANSWER_4 = By.XPATH, '//p[contains(text(),"Только начиная с завтрашнего дня. Но скоро станем расторопнее.")]'
    FAQ_ANSWER_5 = By.XPATH, '//p[contains(text(),"Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.")]'
    FAQ_ANSWER_6 = By.XPATH, '//p[contains(text(),"Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.")]'
    FAQ_ANSWER_7 = By.XPATH, '//p[contains(text(),"Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.")]'
    FAQ_ANSWER_8 = By.XPATH, '//p[contains(text(),"Да, обязательно. Всем самокатов! И Москве, и Московской области.")]'

    # Main page
    SITE_HEADER = By.XPATH, '//div[contains(@class, "Home_Header__iJKdX")]'
    BOTTOM_ORDER_BUTTON = By.XPATH, '//div[contains(@class, "Home_FinishButton")]/button'
    HEADER_ORDER_BUTTON = By.XPATH, '//div[@class = "Header_Nav__AGCXC"]/button[text() = "Заказать"]'

    # Logo
    HEADER_SCOOTER_LOGO = By.XPATH, '//a[contains(@class, "Header_LogoScooter")]'
    HEADER_YANDEX_LOGO = By.XPATH, '//a[@href="//yandex.ru"]'
    TITLE = By.TAG_NAME, 'title'

