import allure
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.main_page import MainPage
from urls import *
from data import Data

class TestMainPageQuestion:

    @allure.title('Проверка выпадающего списка раздела "вопросы о важном"')
    @allure.description('В разделе "вопросы о важном" жмем на вопрос, проверяем текст ответа')


    @pytest.mark.parametrize("locator_question, locator_answer, expected_text", Data.data_question_answer_text)
    def test_check_main_question_cost_answer(self, driver, locator_question, locator_answer, expected_text):
        ### Arrange ###

        # создаем объект  главной страницы
        main_page = MainPage(driver)

        # ждем загрузки раздела "вопросы о важном"     
        main_page.wait_for_located_main_question_accordion()

        ### Act ###

        # скролл до раздела "вопросы о важном" 
        main_page.scroll_to_main_question()
        
        ### Assert ###

        # кликаем на вопрос, проверяем что текст ответа совпадает с ожидаемым
        assert main_page.check_main_question_cost_answer(locator_question, locator_answer, expected_text)
