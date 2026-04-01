import allure
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators as OPL

from pages.base_page import BasePage

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from urls import *

class Order(BasePage):
    
    @allure.step('проверка что страница заказа самоката открылась')
    def check_order_page(self):
        self.wait_for_load_section_who_scooter_for()
        current_url = self.driver.current_url
        assert current_url == order_page_url, f"Ожидаемый URL: {order_page_url}, фактический: {current_url}"


    # методы для проверки раздела "Для кого самокат"


    @allure.step('ждем загрузки раздела "для кого самокат"')
    def wait_for_load_section_who_scooter_for(self):
        self.wait_for_element_clickable(OPL.BUTTON_NEXT)
        
    @allure.step('заполнение поля имя')
    def fill_field_name(self, name="Вася"):
        self.send_keys_to_input(keys=name, locator=OPL.NAME_FIELD)
        
    @allure.step('заполнение поля фамилия')
    def fill_field_surname(self, surname="Иванов"):
        self.send_keys_to_input(keys=surname, locator=OPL.SURNAME_FIELD)
        
    @allure.step('заполнение поля адрес')
    def fill_field_address(self, address="Москва, улица Ленина 1-16"):
        self.send_keys_to_input(keys=address, locator=OPL.ADDRESS_FIELD)
        
    @allure.step('заполнение поля станция метро')
    def fill_field_metro_station(self, locator_station=OPL.STATION_ROCOSSOVSKIY):
        self.click_on_element(OPL.METRO_STATION_FIELD)
        self.scroll_to_element(locator_station)
        self.click_on_element(locator_station)

    @allure.step('заполнение поля телефон')
    def fill_field_phone(self, phone="89998887766"):
        self.send_keys_to_input(keys=phone, locator=OPL.PHONE_FIELD)
        
    @allure.step('заполнение всех полей раздела "для кого самокат"')
    def fill_all_fields_section_who_scooter_for(self, name, surname, address, locator_station, phone):
        self.fill_field_name(name)
        self.fill_field_surname(surname)
        self.fill_field_address(address)
        self.fill_field_metro_station(locator_station)
        self.fill_field_phone(phone)

    @allure.step('жмем кнопку "Далее"')
    def click_next_button_to_rental_page(self):
        self.click_on_element(OPL.BUTTON_NEXT)

    

    # методы для проверки раздела "Про аренду"


    @allure.step('ждем загрузки раздела "Про аренду"')
    def wait_for_load_rental_section(self):
        self.wait_for_element_clickable(OPL.BUTTON_ORDER) 

    @allure.step('заполнение поля "когда привезти самокат"')
    def fill_field_when_bring_scooter(self):
        self.click_on_element(OPL.WHEN_BRING_SCOOTER_FIELD)
        self.click_on_element(OPL.DATE)
        
    @allure.step('заполнение поля период аренды')
    def fill_rental_period(self, rental_period=OPL.RENTAL_PERIOD_DAY):
        self.click_on_element(OPL.RENTAL_PERIOD_FIELD)
        self.click_on_element(rental_period)
        
    @allure.step('заполнение поля цвет самоката')
    def fill_color_scooter(self, color=OPL.CHECKBOX_COLOR_BLACK):
        self.click_on_element(color)

    @allure.step('жмем кнопку \"заказать\"')
    def click_button_place_order(self):
        self.click_on_element(OPL.BUTTON_ORDER)


    # методы попапов


    @allure.step('ждем загрузки попапа подтверждения заказа')
    def wait_for_load_popup_to_place_order(self):
        self.wait_for_element_located(OPL.BUTTON_YES)
    
    
    @allure.step('жмем кнопку подтверждения заказа')
    def click_button_popup_to_place_order_yes(self):
        self.click_on_element(OPL.BUTTON_YES)


    @allure.step('ждем загрузки попапа - проверка успешного заказа самоката')
    def check_popup_succesfully_order(self):
        assert self.wait_for_element_located(OPL.POPUP_ORDER_PLACED)
        

