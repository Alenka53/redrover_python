from time import sleep

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def test_explisit_waits_and_expected_conditions(driver, wait):
    # Перейти по URL: Открыть в браузере указанный URL сайта <https://victoretc.github.io/selenium_waits/>
    driver.get("https://victoretc.github.io/selenium_waits/")
    # Проверить заголовок: Убедиться, что текст в теге <h1> на странице соответствует "Практика с ожиданиями в Selenium".
    locator_h1 = (By.XPATH, '//h1[text()="Практика с ожиданиями в Selenium"]')
    h1_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locator_h1))
    assert h1_element.is_displayed()
    # Дождаться появления кнопки "Начать тестирование"
    visible_after_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Начать тестирование']")))
    assert visible_after_button.text == 'Начать тестирование'
    # Найти кнопку: Найти на странице кнопку с текстом "Начать тестирование".
    # Начать тестирование: Кликнуть по кнопке "Начать тестирование".
    locator_button = (By.XPATH, "//button[text()='Начать тестирование']")
    visible_after_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(locator_button))
    visible_after_button.click()
    # Ввод логина: Ввести "login" в поле для логина.
    login = "login"
    driver.find_element("css selector", "input[id = 'login']").send_keys(login)
    # Ввод пароля: Ввести "password" в поле для пароля.
    password_locator = "input[id = 'password']"
    password = "password"
    driver.find_element("css selector", password_locator).send_keys(password)
    # Согласие с правилами: Установить флажок в чекбокс "Согласен со всеми правилами".
    agree_locator = "input[id = 'agree']"
    driver.find_element("css selector", agree_locator).click()
    # Подтвердить регистрацию: Нажать кнопку "Зарегистрироваться".
    locator_button_register = "button[id = 'register']"
    driver.find_element("css selector", locator_button_register).click()
    # Проверка загрузки: Удостовериться, что появился индикатор загрузки.
    visible_loading = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='loader']")))
    assert visible_loading.text == 'Загрузка...'
    # Проверка сообщения: Убедиться, что после завершения загрузки появилось сообщение "Вы успешно зарегистрированы".
    visible_success = wait.until(EC.visibility_of_element_located((By.XPATH, "//p[@id='successMessage']")))
    assert visible_success.text == 'Вы успешно зарегистрированы!'




