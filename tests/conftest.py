import pytest
import logging
from selenium import webdriver
from selenium.webdriver import FirefoxOptions

from urls import *

# НАСТРОЙКА ЛОГИРОВАНИЯ
# Создаём логгер для текущего модуля
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)  # минимальный уровень логирования

# Создаём обработчик для записи в файл
file_handler = logging.FileHandler('test_logs.log', mode='a', encoding='utf-8')  # 'w' — перезаписывать, 'a' — дописывать
file_handler.setLevel(logging.INFO)  # уровень для этого обработчика

# Настраиваем формат вывода
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Добавляем обработчик к логгеру
logger.addHandler(file_handler)

# ФИКСТУРЫ ДЛЯ БРАУЗЕРА FIREFOX

@pytest.fixture(scope="function")
def driver():
    options = FirefoxOptions()
    # options.add_argument("--window-size=1600,900") # запуск с размером окна 1600*900 (можно подставить свой размер)
    
    #options.add_argument("--headless") # запуск без явного отображения браузера на экране

    try:
        # создаем драйвер для браузера с вышеуказанными опциями
        driver = webdriver.Firefox(options=options)

        # Открываем главную страницу
        driver.get(main_page_url)

        # Передаём драйвер в тест
        yield driver

    except Exception as e:
        logger.error("Ошибка при создании драйвера: %s", e)
        raise

    finally:
        # Гарантированно закрываем браузер даже при ошибках в тесте
        try:
            driver.quit()
            logger.info("Браузер успешно закрыт")
        except WebDriverException as e:
            logger.error("Ошибка при закрытии драйвера: %s", e)
        except Exception as e:
            logger.error("Неожиданная ошибка при закрытии: %s", e)

@pytest.fixture(scope="function")
def driver_order_page():
    options = FirefoxOptions()
    # options.add_argument("--window-size=1600,900") # запуск с размером окна 1600*900 (можно подставить свой размер)
    
    #options.add_argument("--headless") # запуск без явного отображения браузера на экране

    try:
        # создаем драйвер для браузера с вышеуказанными опциями
        driver = webdriver.Firefox(options=options)

        # Открываем главную страницу
        driver.get(order_page_url)

        # Передаём драйвер в тест
        yield driver

    except Exception as e:
        logger.error("Ошибка при создании драйвера: %s", e)
        raise

    finally:
        # Гарантированно закрываем браузер даже при ошибках в тесте
        try:
            driver.quit()
            logger.info("Браузер успешно закрыт")
        except WebDriverException as e:
            logger.error("Ошибка при закрытии драйвера: %s", e)
        except Exception as e:
            logger.error("Неожиданная ошибка при закрытии: %s", e)