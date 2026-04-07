import allure

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators as MPL
from urls import *

class MainPage(BasePage):
    # 1. методы для проверки раздела "вопросы о важном"
    @allure.step("принимаем куки")
    def click_accept_cookies(self):
        self.click_on_element(MPL.BUTTON_ACCEPT_COOKIES)

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

    @allure.step('ждем загрузки кнопки "заказать" главной страницы')
    def wait_for_load_button_header_order(self, locator_order):
        self.wait_for_element_located(locator_order)
        
    @allure.step('скролл до кнопки заказать')
    def scroll_to_button_order(self, locator_order):
        self.scroll_to_element(locator_order)

    @allure.step('жмем кнопку заказать в шапке/внизу страницы')
    def click_button_header_order(self, locator_order=MPL.BUTTON_HEADER_ORDER):
        self.click_on_element(locator_order)

    # 3. методы для проверки перехода по логотипу
    @allure.step('жмем логотип Яндекс')
    def click_button_yandex_logo(self):
        self.click_on_element(MPL.YANDEX_LOGO)

    @allure.step('проверка, что открылась главная страница «Самоката»')
    def check_main_page(self):
        self.wait_for_load_button_header_order(MPL.BUTTON_HEADER_ORDER)
        return self.url == main_page_url, f"Ожидаемый URL: {main_page_url}, фактический: {self.url}"
