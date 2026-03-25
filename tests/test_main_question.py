from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest
from pages.main_page import MainPage
from urls import *
from data import Data

class TestMainPageQuestion():
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

    
    
    @pytest.mark.parametrize("locator_question, locator_answer, expected_text", Data.test_data_question_answer_text)
    def test_check_main_question_cost_answer(self, locator_question, locator_answer, expected_text):
        
        # ждем загрузки раздела "вопросы о важном"     
        self.main_page.wait_for_load_main_question_accordion()

        # скролл до раздела "вопросы о важном" 
        self.main_page.scroll_to_main_question()

        """ # возвращаем текст ответа на вопрос о стоимости 
        self.main_page.click_main_question_cost() """

        
        self.main_page.check_main_question_cost_answer(locator_question, locator_answer, expected_text)

        
        

    @classmethod
    def teardown_class(cls):
        # Закрываем  браузер
        cls.driver.quit()

# pytest tests/test_main_question.py -v

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