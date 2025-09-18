from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class EmployeesPage:
    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 10)

    # Private Helpers
    def _find_row_by_name(self, name: str):
        row_xpath = f"//table//tr[td[contains(., '{name}')]]"
        return self.wait.until(
            EC.presence_of_element_located((By.XPATH, row_xpath))
        )

    # Actions
    def add_employee(self, name: str, lastname: str, dependents: int):
        self.wait.until(
        EC.presence_of_element_located((By.XPATH, "//table"))
        )
        self.browser.find_element(By.ID, "add").click()
        self.wait.until(EC.presence_of_element_located((By.ID, "firstName"))).send_keys(name)
        self.browser.find_element(By.ID, "lastName").send_keys(str(lastname))
        self.browser.find_element(By.ID, "dependants").send_keys(str(dependents))
        self.browser.find_element(By.ID, "addEmployee").click()
        # Wait for it to appear in the table
        self.wait.until(
            EC.text_to_be_present_in_element(
                (By.XPATH, f"//table//tr[td[contains(., '{name}')]]"),
                name,
            )
        )

    def edit_employee(self, name: str, new_dependents: int):
        row = self._find_row_by_name(name)
        row.find_element(By.CSS_SELECTOR, "i.fa-edit").click()

        dependents_input = self.wait.until(
            EC.presence_of_element_located((By.ID, "dependants"))
        )
        dependents_input.clear()
        dependents_input.send_keys(str(new_dependents))

        self.browser.find_element(By.ID, "updateEmployee").click()

        # Wait for the row to be updated
        self.wait.until(
            EC.text_to_be_present_in_element(
                (By.XPATH, f"//table//tr[td[contains(., '{name}')]]"),
                str(new_dependents),
            )
        )

    def delete_employee(self, name: str):
        row_xpath = f"//table//tr[td[contains(., '{name}')]]"
        row = self._find_row_by_name(name)
        row.find_element(By.CSS_SELECTOR, "i.fa-times").click()

        self.wait.until(
            EC.element_to_be_clickable((By.ID, "deleteEmployee"))
        ).click()

        # Wait for the row disappear
        self.wait.until_not(EC.presence_of_element_located((By.XPATH, row_xpath)))
