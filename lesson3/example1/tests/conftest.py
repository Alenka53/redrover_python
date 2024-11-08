import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
#from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def chrome_options():
    options = Options()
    options.add_argument('--start-maximized')
    return options

@pytest.fixture
def driver(chrome_options):
    # Создаем объект службы с указанием пути к chromedriver
    service = Service(ChromeDriverManager().install())
    # Передаем службу и опции в инициализацию WebDriver
    driver = webdriver.Chrome(service=service, options=chrome_options)
    yield driver
    driver.quit()

#    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
#    yield driver
#    driver.quit()

@pytest.fixture
def wait(driver):
    wait = WebDriverWait(driver, timeout=10)
    return wait




