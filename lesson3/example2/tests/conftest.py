import pytest
from selene import browser
from selenium import webdriver

@pytest.fixture(autouse=True)
def browser_management():
    
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    browser.config.driver_options = options
    browser.config.window_height = 1920
    browser.config.window_width = 1080
    browser.config.timeout = 6
    driver = webdriver.Chrome(options=options)
    browser.set_driver(driver)



    yield

    browser.quit()