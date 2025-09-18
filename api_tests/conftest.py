import pytest

@pytest.fixture(scope="session")
def base_url():
    return "https://wmxrwq14uc.execute-api.us-east-1.amazonaws.com/Prod"

@pytest.fixture(scope="session")
def headers():
    return {
        "Authorization": "Basic VGVzdFVzZXI4MDQ6b1pHXn1ANzYvIWRx",  # pega el token de Postman
        "Content-Type": "application/json"
    }
