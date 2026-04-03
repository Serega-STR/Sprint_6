import allure

from pages.base_page import BasePage

from locators.main_page_locators import MainPageLocators as MPL
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    # 1. методы для проверки раздела "вопросы о важном"

    @allure.step("ждем загрузки раздела вопросы о важном главной страницы")
    def wait_for_located_main_question_accordion(self):
        self.wait_for_element_located(MPL.MAIN_QUESTION_ACCORDION)
        
     
    @allure.step("скролл до раздела \"вопросы о важном\"")
    def scroll_to_main_question(self):
        self.scroll_to_element(MPL.MAIN_QUESTION_ACCORDION)

    @allure.step('клик по вопросу')
    def click_main_question_cost(self, locator_question):
        self.click_on_element(locator_question)
        
    @allure.step('возвращаем текст ответа на вопрос о стоимости')
    def main_question_cost_answer_text(self, locator_answer):
        return self.get_text_on_element(locator_answer)
    
    @allure.step('проверяем текст ответа')
    def check_main_question_cost_answer(self, locator_question, locator_answer, expected_text):
        self.click_main_question_cost(locator_question)
        actual_text = self.main_question_cost_answer_text(locator_answer)
        return actual_text == expected_text, f"Ожидаемый текст : {expected_text}. Фактический текст: {actual_text}"

    # 2. методы для проверки заказа

    @allure.step('ждем загрузки кнопки \"заказать\" главной страницы')
    def wait_for_load_button_header_order(self, locator_order):
        self.wait_for_element_located(locator_order)
        
    @allure.step('скролл до кнопки заказать')
    def scroll_to_button_order(self, locator_order):
        self.scroll_to_element(locator_order)

    @allure.step('жмем кнопку заказать в шапке/внизу страницы')
    def click_button_header_order(self, locator_order):
        self.click_on_element(locator_order)
