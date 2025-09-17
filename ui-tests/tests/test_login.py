from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_success(browser):
    

    # Interactions
    browser.find_element(By.ID, "Username").send_keys("TestUser804")
    browser.find_element(By.ID, "Password").send_keys("oZG^}@76/!dq")
    browser.find_element(By.XPATH, "//button[text()='Log In']").click()

    # Validation
    WebDriverWait(browser, 10).until(
        EC.url_contains("/Benefits")
    )

    assert "/Benefits" in browser.current_url