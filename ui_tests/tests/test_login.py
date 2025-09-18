from ui_tests.pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_success(browser, base_url):
    login_page = LoginPage(browser)
    login_page.load(base_url)
    login_page.login("TestUser804", "oZG^}@76/!dq")

    WebDriverWait(browser, 10).until(
        EC.url_contains("/Benefits")
    )

    assert "/Benefits" in browser.current_url
