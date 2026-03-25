from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest
from pages.main_page import MainPage
from pages.order import Order
from urls import *
import time # ПЕРЕД СДАЧЕЙ УДАЛИТЬ # ПЕРЕД СДАЧЕЙ УДАЛИТЬ # ПЕРЕД СДАЧЕЙ УДАЛИТЬ

class TestOrder():
    driver = None

    @classmethod
    def setup_class(cls):
        """ # Создали драйвер для браузера Chrome
        cls.driver = webdriver.Chrome() """
        
        # Создали драйвер для браузера Firefox
        cls.driver = webdriver.Firefox()

        # открыли главную страницу
        cls.driver.get(main_page_url)

        # создали обьект главной страницы
        cls.main_page = MainPage(cls.driver)

        # создали обьект страницы заказа
        cls.order = Order(cls.driver)

    def test_check_order(self):
        
        # ждем загрузки раздела "вопросы о важном"     
        self.main_page.wait_for_load_button_header_order()

        # жмем кнопку заказать в шапке
        self.main_page.click_button_header_order()

        # проверка что страница заказа самоката открылась
        self.order.check_order_page()

        # заполнение всех полей раздела "для кого самокат"
        self.order.fill_all_fields_section_who_scooter_for()

        # жмем кнопку "Далее"
        self.order.click_next_button_to_rental_page()

        # ждем загрузки раздела "Про аренду"
        self.order.wait_for_load_rental_section()

        # заполнение поля "когда привезти самокат"
        self.order.fill_field_when_bring_scooter()

        # заполнение поля период аренды
        self.order.fill_rental_period()

        # заполнение поля цвет самоката
        self.order.fill_color_scooter()

        # жмем кнопку "заказать" 
        self.order.click_button_place_order()

        # ждем загрузки попапа подтверждения заказа
        self.order.wait_for_load_popup_to_place_order()

        # жмем кнопку подтверждения заказа
        self.order.click_button_popup_to_place_order_yes() 

        # ждем загрузки попапа - проверка успешного заказа самоката
        self.order.check_popup_succesfully_order()

    @classmethod
    def teardown_class(cls):
        # Закрываем  браузер
        cls.driver.quit()

# pytest tests/test_order.py -v

""" # класс с автотестом
class TestPraktikum:

    driver = None

    @classmethod
    def setup_class(cls):
        # создали драйвер для браузера Firefox
        cls.driver = webdriver.Firefox()

    def test_check_email_in_header(self):
        # перешли на страницу тестового приложения
        self.driver.get('https://qa-mesto.praktikum-services.ru/')

        # создай объект класса страницы авторизации
        login_page = LoginPageMesto(self.driver)
        # выполни авторизацию
        email = "aboleshev_38_39_fs@mail.ru"
        password = "12345678"
        # передавай эти переменные внутрь метода
        login_page.login(email, password)

        # создай объект класса заголовка приложения
        header_page = HeaderPageMesto(self.driver) # driver надо или нет

        # дождись загрузки заголовка
        header_page.wait_for_load_header()

        # получи текст элемента в заголовке
        email_from_header = header_page.email_in_header()

        # сделай проверку, что полученное значение совпадает c email
        assert email == email_from_header

    @classmethod
    def tearDown_class(cls):
        # Закрой браузер
        cls.driver.quit() """

""" # Класс страницы авторизации
class LoginPageMesto(MainPage):
    email_field = [By.ID, 'email']
    password_field = [By.ID, 'password']
    sign_in_button = [By.CLASS_NAME, 'auth-form__button']

    def __init__(self, driver):
        self.driver = driver

    def set_email(self, email):
        self.driver.find_element(*self.email_field).send_keys(email)

    def set_password(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_sign_in_button(self):
        self.driver.find_element(*self.sign_in_button).click()

    def login(self, email, password):
        self.set_email(email)
        self.set_password(password)
        self.click_sign_in_button() """

""" # Класс заголовка
class HeaderPageMesto:
    # создай локатор для элемента c email в заголовке страницы
    header_user = (By.CLASS_NAME, 'header__user')

    def __init__(self, driver):
        self.driver = driver

    # метод ожидания загрузки страницы
    def wait_for_load_header(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.header_user))

    # метод для получения текста элемента в заголовке
    def email_in_header(self):
        return self.driver.find_element(*self.header_user).text """