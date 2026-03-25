import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait

from urls import *

# ФИКСТУРЫ ДЛЯ БРАУЗЕРА FIREFOX

@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--window-size=1600,900")
    options.add_experimental_option("prefs", {
            "profile.password_manager_leak_detection": False
        })
    #options.add_argument("--headless") # запуск без явного отображения браузера на экране

    # создаем драйвер для браузера с вышеуказанными опциями
    driver = webdriver.Firefox(options=options)
    
    # открываем сайт с помощью драйвера
    driver.get(main_page)

    # приостанавливаем этот код, передаем драйвер в тест
    yield driver

    # после выполнения теста закрываем браузер, останавливаем драйвер
    driver.quit()




