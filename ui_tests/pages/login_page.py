from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, "Username")
        self.password_input = (By.ID, "Password")
        self.login_button = (By.XPATH, "//button[text()='Log In']")

    def load(self, base_url: str):
        """Abrir la página de login"""
        self.driver.get(f"{base_url}/Account/LogIn")

    def login(self, username: str, password: str):
        """Realizar login con credenciales"""
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()

