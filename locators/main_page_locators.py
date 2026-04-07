from selenium.webdriver.common.by import By

class MainPageLocators:
    # принять куки 
    BUTTON_ACCEPT_COOKIES = (By.ID, 'rcc-confirm-button')

    # РАЗДЕЛ ответы на вопросы - "Вопросы о важном" 
    MAIN_QUESTION_ACCORDION = (By.CLASS_NAME, 'accordion')

    # 8 вопросов раскрывающего списка "Вопросы о важном"
    MAIN_QUESTION_COST = (By.ID, 'accordion__heading-0')   # оплата
    MAIN_QUESTION_MULTIPLE_SCOOTERS = (By.ID, 'accordion__heading-1') # заказ нескольких самокатов
    MAIN_QUESTION_RENTAL_TIME = (By.ID, 'accordion__heading-2') # время аренды
    MAIN_QUESTION_ORDER_TODAY = (By.ID, 'accordion__heading-3') # заказать сегодня
    MAIN_QUESTION_EXTEND_ORDER = (By.ID, 'accordion__heading-4') # продлить заказ
    MAIN_QUESTION_CHARGE = (By.ID, 'accordion__heading-5') # зарядка
    MAIN_QUESTION_CANCEL_ORDER = (By.ID, 'accordion__heading-6') # отмена заказа
    MAIN_QUESTION_DELIVERY_BEYOND_MKAD = (By.ID, 'accordion__heading-7') # доставка за мкад

    # 8 ответов раскрывающего списка "Вопросы о важном"
    MAIN_QUESTION_COST_ANSWER = (By.CSS_SELECTOR, '[id=accordion__panel-0] > p')   # ответ - оплата
    MAIN_QUESTION_MULTIPLE_SCOOTERS_ANSWER = (By.CSS_SELECTOR, '[id=accordion__panel-1] > p') # ответ - заказ нескольких самокатов
    MAIN_QUESTION_RENTAL_TIME_ANSWER = (By.CSS_SELECTOR, '[id=accordion__panel-2] > p') #  ответ - время аренды
    MAIN_QUESTION_ORDER_TODAY_ANSWER = (By.CSS_SELECTOR, '[id=accordion__panel-3] > p') #  ответ - заказать сегодня
    MAIN_QUESTION_EXTEND_ORDER_ANSWER = (By.CSS_SELECTOR, '[id=accordion__panel-4] > p') #  ответ - продлить заказ
    MAIN_QUESTION_CHARGE_ANSWER = (By.CSS_SELECTOR, '[id=accordion__panel-5] > p') #  ответ - зарядка
    MAIN_QUESTION_CANCEL_ORDER_ANSWER = (By.CSS_SELECTOR, '[id=accordion__panel-6] > p') #  ответ - отмена заказа
    MAIN_QUESTION_DELIVERY_BEYOND_MKAD_ANSWER = (By.CSS_SELECTOR, '[id=accordion__panel-7] > p') #  ответ - доставка за мкад

    # локаторы для проверки заказа самоката
    BUTTON_HEADER_ORDER = (By.XPATH, '//div[contains(@class, "Header")]/button[text()="Заказать"]') #кнопка заказать вверху страницы
    BUTTON_HOME_ORDER = (By.XPATH, '//div[contains(@class, "Home")]/button[text()="Заказать"]') #кнопка заказать внизу страницы

    # логотипы
    YANDEX_LOGO = (By.XPATH, '//a[@href="//yandex.ru"]')
    SCOOTER_LOGO = (By.XPATH, '//a[@href="/"]')