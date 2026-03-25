import random
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import MainPageLocators as MPL


class Credentials():
    EMAIL = 'aboleshev_38_39_fs@mail.ru'
    PASSWORD = '12345678'

class Generator():
    def create_pasord():
        password = f'{random.randint(100_000,999_999)}'
        return password

    def create_email():
        email = f'sergey_aboleshev_38_39_fs_{random.randint(100,999)}@mail.ru'
        return email

class Wait():
    def wait(driver):
        # задаем время ожидания драйвера браузера - до 3 сек
        return WebDriverWait(driver, 3)

class Data():
    test_data_question_answer_text = [
        [MPL.MAIN_QUESTION_COST, MPL.MAIN_QUESTION_COST_ANSWER, "Сутки — 400 рублей. Оплата курьеру — наличными или картой."],
        [MPL.MAIN_QUESTION_MULTIPLE_SCOOTERS, MPL.MAIN_QUESTION_MULTIPLE_SCOOTERS_ANSWER, "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."],
        [MPL.MAIN_QUESTION_RENTAL_TIME, MPL.MAIN_QUESTION_RENTAL_TIME_ANSWER, "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."],
        [MPL.MAIN_QUESTION_ORDER_TODAY, MPL.MAIN_QUESTION_ORDER_TODAY_ANSWER, "Только начиная с завтрашнего дня. Но скоро станем расторопнее."],
        [MPL.MAIN_QUESTION_EXTEND_ORDER, MPL.MAIN_QUESTION_EXTEND_ORDER_ANSWER, "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."],
        [MPL.MAIN_QUESTION_CHARGE, MPL.MAIN_QUESTION_CHARGE_ANSWER, "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."],
        [MPL.MAIN_QUESTION_CANCEL_ORDER, MPL.MAIN_QUESTION_CANCEL_ORDER_ANSWER, "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."],
        [MPL.MAIN_QUESTION_DELIVERY_BEYOND_MKAD, MPL.MAIN_QUESTION_DELIVERY_BEYOND_MKAD_ANSWER, "Да, обязательно. Всем самокатов! И Москве, и Московской области."]
                                    ]
        
# pytest tests/test_personal_account_logout.py -v
# pytest tests/test_go_to_the_construtor_section.py -v
#  pytest tests/test_transition.py -v
