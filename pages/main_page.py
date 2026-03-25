import allure
import pytest
from locators.main_page_locators import MainPageLocators as MPL
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class MainPage():
    
    # локаторы в соответствующем файле в locators/

    def __init__(self, driver):
        self.driver = driver

    # 1. методы для проверки раздела "вопросы о важном"

    # ждем загрузки раздела вопросы о важном главной страницы
    def wait_for_load_main_question_accordion(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(MPL.MAIN_QUESTION_ACCORDION)
            )
        
    # скролл до раздела "вопросы о важном"
    def scroll_to_main_question(self):
        element = self.driver.find_element(*MPL.MAIN_QUESTION_ACCORDION)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    # клик по вопросу "Сколько это стоит?..."
    def click_main_question_cost(self, locator_question):
        self.driver.find_element(*locator_question).click()

    # возвращаем текст ответа на вопрос о стоимости    
    def main_question_cost_answer_text(self, locator_answer):
        element = self.driver.find_element(*locator_answer)
        return element.text

    
    # проверяем текст ответа
    
    def check_main_question_cost_answer(self, locator_question, locator_answer, expected_text):
        self.click_main_question_cost(locator_question)
        #expected_text = "Сутки — 400 рублей. Оплата курьеру — наличными или картой."
        actual_text = self.main_question_cost_answer_text(locator_answer)
        assert actual_text == expected_text

    # 2. методы для проверки заказа

    # ждем загрузки кнопки "заказать" главной страницы
    def wait_for_load_button_header_order(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(MPL.BUTTON_HEADER_ORDER)
            )

    # жмем кнопку заказать в шапке
    def click_button_header_order(self):
        self.driver.find_element(*MPL.BUTTON_HEADER_ORDER).click()

    # жмем кнопку заказать внизу страницы
    def click_button_home_order(self):
        self.driver.find_element(*MPL.BUTTON_HOME_ORDER).click()

    





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