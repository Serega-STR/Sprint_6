import pytest
import allure

from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import *
from urls import *


class TestOrder():
    
    @allure.title('Проверка placeholder у поля email')
    @allure.description('На странице ищем элемент "email" и проверяем, что его placeholder == "Email"')

    @pytest.mark.parametrize("locator_order, name, surname, address, locator_station, phone, locator_rental_period, locator_color", Data.data_order)
    def test_check_order(self, driver, locator_order, name, surname, address, locator_station, phone, locator_rental_period, locator_color):

        ### Arrange ###

        # создаем объект главной страницы
        main_page = MainPage(driver)

        # создаем объект страницы заказа
        order_page = OrderPage(driver)

        # принимаем куки
        main_page.click_accept_cookies()
        
        # ждем загрузки раздела "заказать"     
        main_page.wait_for_load_button_header_order(locator_order)

        ### Act ###

        # скролл до кнопки заказать
        main_page.scroll_to_button_order(locator_order)

        # жмем кнопку "заказать"
        main_page.click_button_header_order(locator_order)
        
        # проверка что страница заказа самоката открылась
        order_page.check_order_page()

        # заполнение всех полей раздела "для кого самокат"
        order_page.fill_all_fields_section_who_scooter_for(name, surname, address, locator_station, phone)

        # жмем кнопку "Далее"
        order_page.click_next_button_to_rental_page()

        # ждем загрузки раздела "Про аренду"
        order_page.wait_for_load_rental_section()

        # заполнение поля "когда привезти самокат"
        order_page.fill_field_when_bring_scooter()

        # заполнение поля период аренды
        order_page.fill_rental_period(locator_rental_period)

        # заполнение поля цвет самоката
        order_page.fill_color_scooter(locator_color)

        # жмем кнопку "заказать" 
        order_page.click_button_place_order()

        # ждем загрузки попапа подтверждения заказа
        order_page.wait_for_load_popup_to_place_order()

        # жмем кнопку подтверждения заказа
        order_page.click_button_popup_to_place_order_yes() 

        ### Assert ###

        # ждем загрузки попапа - проверка успешного заказа самоката
        assert order_page.check_popup_succesfully_order()