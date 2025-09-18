import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="session")
def base_url():
    # URL app base
    return "https://wmxrwq14uc.execute-api.us-east-1.amazonaws.com/Prod"


@pytest.fixture
def browser():
    # Launch Chrome
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def logged_in(browser, base_url):
    """Fixture que hace login y retorna el browser ya autenticado."""
    browser.get(f"{base_url}/Account/Login")

    # Credentials provided
    browser.find_element(By.ID, "Username").send_keys("TestUser804")
    browser.find_element(By.ID, "Password").send_keys("oZG^}@76/!dq")

    # Login button
    browser.find_element(By.XPATH, "//button[contains(., 'Log In')]").click()

    # Wait until it reaches the dashboard
    WebDriverWait(browser, 10).until(
        EC.url_contains("/Benefits")
    )

    return browser
