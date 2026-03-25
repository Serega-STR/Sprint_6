import allure
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from urls import *

class Order():
    
    # локаторы в соответствующем файле в locators/

    def __init__(self, driver):
        self.driver = driver
   
    # проверка что страница заказа самоката открылась

    def check_order_page(self):
        current_url = self.driver.current_url
        assert current_url == order_page_url

    # методы для проверки раздела "Для кого самокат"

    # ждем загрузки раздела "для кого самокат"
    def wait_for_load_section_who_scooter_for(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(OrderPageLocators.BUTTON_NEXT) 
            )

    # заполнение поля имя
    def fill_field_name(self):
        self.driver.find_element(*OrderPageLocators.NAME_FIELD).send_keys("Вася")

    # заполнение поля фамилия
    def fill_field_surname(self):
        self.driver.find_element(*OrderPageLocators.SURNAME_FIELD).send_keys("Иванов")

    # заполнение поля адрес
    def fill_field_address(self):
        self.driver.find_element(*OrderPageLocators.ADDRESS_FIELD).send_keys("Москва, улица Ленина 1-16")

    # заполнение поля станция метро
    def fill_field_metro_station(self):
        self.driver.find_element(*OrderPageLocators.METRO_STATION_FIELD).click()
        self.driver.find_element(*OrderPageLocators.STATION_ROCOSSOVSKIY).click()

    # заполнение поля телефон
    def fill_field_phone(self):
        self.driver.find_element(*OrderPageLocators.PHONE_FIELD).send_keys("89998887766")

    # заполнение всех полей раздела "для кого самокат"
    def fill_all_fields_section_who_scooter_for(self):
        self.fill_field_name()
        self.fill_field_surname()
        self.fill_field_address()
        self.fill_field_metro_station()
        self.fill_field_phone()

    # жмем кнопку "Далее"
    def click_next_button_to_rental_page(self):
        self.driver.find_element(*OrderPageLocators.BUTTON_NEXT).click()

    

    # методы для проверки раздела "Про аренду"

    # ждем загрузки раздела "Про аренду"
    def wait_for_load_rental_section(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(OrderPageLocators.BUTTON_ORDER) 
            )

    # заполнение поля "когда привезти самокат"
    def fill_field_when_bring_scooter(self):
        self.driver.find_element(*OrderPageLocators.WHEN_BRING_SCOOTER_FIELD).click()
        self.driver.find_element(*OrderPageLocators.DATE).click()

    # заполнение поля период аренды
    def fill_rental_period(self):
        self.driver.find_element(*OrderPageLocators.RENTAL_PERIOD_FIELD).click()
        self.driver.find_element(*OrderPageLocators.RENTAL_PERIOD_DAY).click()

    # заполнение поля цвет самоката
    def fill_color_scooter(self):
        self.driver.find_element(*OrderPageLocators.CHECKBOX_COLOR_BLACK).click()

    # жмем кнопку "заказать"    
    def click_button_place_order(self):
        self.driver.find_element(*OrderPageLocators.BUTTON_ORDER).click()

    # методы попапов

    # ждем загрузки попапа подтверждения заказа
    def wait_for_load_popup_to_place_order(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(OrderPageLocators.BUTTON_YES) 
            )

    # жмем кнопку подтверждения заказа
    def click_button_popup_to_place_order_yes(self):
        self.driver.find_element(*OrderPageLocators.BUTTON_YES).click()

    # ждем загрузки попапа - проверка успешного заказа самоката
    def check_popup_succesfully_order(self):
        assert WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(OrderPageLocators.POPUP_ORDER_PLACED) 
            )

     

    

    # @allure.step("Кликнуть на аватар")
    # def click_on_avatar(self):
    #     self.click_on_element(MainPageLocators.PROFILE_IMAGE)

    # @allure.step("Изменить URL аватара")
    # def update_avatar(self, avatar_url):
    #     self.send_keys_to_input(MainPageLocators.AVATAR_INPUT, avatar_url)

    # @allure.step("Нажать кнопку обновления аватара")
    # def click_update_avatar_button(self):
    #     self.click_on_element(MainPageLocators.UPDATE_AVATAR_BUTTON)

    # @allure.step("Проверить обновление аватара")
    # def is_avatar_updated(self, avatar_url):
    #     return self.wait_for_attribute(MainPageLocators.PROFILE_IMAGE, "style", f'background-image: url("{avatar_url}");')

    # @allure.step("Подождать загрузки списка карточек")
    # def wait_for_card_list(self):
    #     self.wait_for_element(MainPageLocators.CARDS)

    # @allure.step("Открыть карточку")
    # def click_on_card(self, card_number):
    #     card_locator = MainPageLocators.card_number(card_number)
    #     self.scroll_to_element(card_locator)
    #     self.click_on_element(card_locator)

    # @allure.step("Сравни имя карточки")
    # def check_card_name(self):
    #     actual_text = self.get_text_on_element(MainPageLocators.CARD_NAME_IN_POPUP)
    #     return actual_text


