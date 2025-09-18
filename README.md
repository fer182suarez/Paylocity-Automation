# Paylocity-Automation (UI + API)

Benefits Dashboard automation with:

UI: Pytest + Selenium (Page Object Model)
API: Pytest + Requests (y Postman opcional)

# 1) Pre-Requirements
Python 3.11+
Google Chrome
Git

# 2) Clone and install
git clone https://github.com/<tu-usuario>/Paylocity-Automation.git
(cd Paylocity-Automation)

-Create and activate venv

-Windows (PowerShell) or VS code console:
python -m venv venv

venv\Scripts\activate

# 3)Install dependencies
pip install -r requirements.txt

# 4) Quick configuration
Base URL

Edita si es necesario en tus fixtures:

UI: ui_tests/conftest.py

API: api_tests/conftest.py

**Valor por defecto:**

https://wmxrwq14uc.execute-api.us-east-1.amazonaws.com/Prod

**Token de API**

Place it in `api_tests/conftest.py` or as an environment variable:


**Authorization": "Basic VGVzdFVzZXI4MDQ6b1pHXn1ANzYvIWRx",**

  **"Content-Type": "application/json**

Windows (PowerShell)

$env:BENEFITS_AUTH_TOKEN = "Basic <your_token>"


# 4) Running the tests

All UI tests:

pytest -v -s ui_tests/tests/any_other_specific

API:

pytest -v -s api_tests/test_employees.py 

Specific test:

pytest ui_tests/tests/test_login.py::test_login_success:any_other


**UI Tip:** for headless mode, add in ui_tests/conftest.py the Chrome option --headless=new.

# 5) Postman (opcional)

Create an Environment with:

base_url = https://wmxrwq14uc.execute-api.us-east-1.amazonaws.com/Prod

auth_token = Basic <your_token>

**In each request:** Authorization: {{auth_token}} and Accept: application/json.

# 6) Troubleshooting

**NoSuchElementException:** add explicit waits (WebDriverWait) and verifies locators.

**HTML responses in API:** check the Authorization header and use endpoints /api/... (not /Account/Login).

**Can't find packages:** make sure you have __init__.py in ui_tests/pages and run pytest from the root of the repo.
