import pytest

from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.support.wait import WebDriverWait

from urls import *

# ФИКСТУРЫ ДЛЯ БРАУЗЕРА FIREFOX

@pytest.fixture(scope="function")
def driver():
    options = FirefoxOptions()
    options.add_argument("--window-size=1600,900")
    
    #options.add_argument("--headless") # запуск без явного отображения браузера на экране

    try:
        # создаем драйвер для браузера с вышеуказанными опциями
        driver = webdriver.Firefox(options=options)

        # Открываем главную страницу
        driver.get(main_page_url)

        # Передаём драйвер в тест
        yield driver

    except Exception as e:
        print(f"Ошибка при создании драйвера: {e}")
        raise

    finally:
        # Гарантированно закрываем браузер даже при ошибках в тесте
        try:
            driver.quit()
            print("Браузер успешно закрыт")
        except WebDriverException as e:
            print(f"Ошибка при закрытии драйвера: {e}")
        except Exception as e:
            print(f"Неожиданная ошибка при закрытии: {e}")
