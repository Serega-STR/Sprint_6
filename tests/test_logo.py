import pytest
import allure

from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.dzen_page import DzenPage

class TestLogo():
    
    @allure.title('При нажатии на логотип открывается соответствующая страница')
    @allure.description("""Если нажать на логотип Яндекса, откроется главная страница Дзена (через редирект)""")
    def test_check_click_logo_to_dzen_page(self, driver):

        ### Arrange ###

        # создаем объект главной страницы
        main_page = MainPage(driver)
        dzen_page = DzenPage(driver)

        # принимаем куки
        main_page.click_accept_cookies()

        ### Act ###

        # жмем соответствующий логотип
        main_page.click_button_yandex_logo()

        ### Assert ###
        
        # проверяем страницу
        assert dzen_page.check_dzen_page 

    @allure.title('При нажатии на логотип открывается соответствующая страница')
    @allure.description("""Если нажать на логотип «Самоката», попадёшь на главную страницу «Самоката»""")
    def test_check_click_logo_to_main_page(self, driver_order_page):

        ### Arrange ###
        # создаем объект страницы заказа
        order_page = OrderPage(driver_order_page)
        
        # принимаем куки
        order_page.click_accept_cookies()
        
        ### Act ###

        # жмем соответствующий логотип
        order_page.click_button_scooter_logo()
        # создаем объект главной страницы
        main_page = MainPage(driver_order_page)

        ### Assert ###
        
        # проверяем страницу
        assert main_page.check_main_page()