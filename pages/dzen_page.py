import allure
from locators.dzen_page_locators import DZEN_LOGO
from pages.base_page import BasePage

from urls import *

class DzenPage(BasePage):
    
    @allure.step('проверка, что страница dzen открылась')
    def check_dzen_page(self):
        self.wait_for_element_located(DZEN_LOGO)
        return self.url == dzen, f"Ожидаемый URL: {dzen}, фактический: {self.url}"
    
        

