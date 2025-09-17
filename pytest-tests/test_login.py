from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

def test_login_success(browser: WebDriver):
    

    # Interacciones
    browser.find_element(By.ID, "user-name").send_keys("standard_user")
    browser.find_element(By.ID, "password").send_keys("secret_sauce")
    browser.find_element(By.ID, "login-button").click()

    # Validación
    assert "inventory" in browser.current_url