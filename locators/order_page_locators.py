from selenium.webdriver.common.by import By


class OrderPageLocators:
    ### раздел ДЛЯ КОГО САМОКАТ 
    NAME_FIELD = (By.XPATH, '//input[@placeholder="* Имя"]') # поле имя
    SURNAME_FIELD = (By.XPATH, '//input[@placeholder="* Фамилия"]') # поле фамилия
    ADDRESS_FIELD = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]') # поле адрес

    # метро
    METRO_STATION_FIELD = (By.CLASS_NAME, 'select-search__value') # выпадающий список станция метро
    STATION_ROCOSSOVSKIY = (By.XPATH, '//div[@class="select-search__select"]/ul[@class="select-search__options"]/li[1]') # выбрать станцию Бульвар Рокоссовского
    STATION_LIHOBORY = (By.XPATH, '//div[@class="select-search__select"]/ul[@class="select-search__options"]/li[last()]')
    

    PHONE_FIELD = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]') # поле ТЕЛЕфон
    BUTTON_NEXT = (By.XPATH, '//button[text()="Далее"]') # кнопка далее

    ### раздел ПРО АРЕНДУ
    WHEN_BRING_SCOOTER_FIELD = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]') # поле Когда привезти самокат
    DATE = (By.CSS_SELECTOR, '[aria-label*="5-е апреля 2026"]') # 5 апреля в поле Когда привезти самокат
    RENTAL_PERIOD_FIELD = (By.CLASS_NAME, 'Dropdown-placeholder') # выпадающий список срок аренды

    # период вренды
    RENTAL_PERIOD_DAY = (By.XPATH, '//div[text()="сутки"]') # сутки срок аренды
    RENTAL_PERIOD_7_DAYS = (By.XPATH, '//div[text()="семеро суток"]') # 7 суток срок аренды
    
    #цвет 
    CHECKBOX_COLOR_BLACK = (By.ID, 'black') # цвет черный
    CHECKBOX_COLOR_GREY = (By.ID, 'grey') # цвет серый

    BUTTON_ORDER = (By.XPATH, '//div[contains(@class, "Order")]/button[text()="Заказать"]') # кнопка Заказать

    # попапы Заказа
    BUTTON_YES = (By.XPATH, '//button[text()="Да"]') # кнопка Да
    POPUP_ORDER_PLACED = (By.XPATH, '//div[text()="Заказ оформлен"]') # заказ оформлен

    """ @staticmethod
    def card_number(card):
        return By.XPATH, f'//*[@id="root"]/div/main/section[2]/ul/li[{card}]'  """