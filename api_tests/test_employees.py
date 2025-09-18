import requests

# save the ID of the created employee
employee_id = None

def test_create_employee(base_url, headers):
    global employee_id
    payload = {
        "username": "qa_user_pytest",
        "firstName": "Jude",
        "lastName": "Bellingham",
        "dependants": 4,
        "salary": 2000
    }
    res = requests.post(f"{base_url}/api/Employees", json=payload, headers=headers)

    assert res.status_code == 200
    data = res.json()
    employee_id = data.get("id")

    assert employee_id is not None
    assert data["firstName"] == payload["firstName"]
    assert data["lastName"] == payload["lastName"]

def test_get_employee_by_id(base_url, headers):
    global employee_id
    res = requests.get(f"{base_url}/api/Employees/{employee_id}", headers=headers)

    assert res.status_code == 200
    data = res.json()
    assert data["id"] == employee_id

def test_update_employee(base_url, headers):
    global employee_id
    payload = {
        "id": employee_id,
        "username": "qa_user_pytest_updated",
        "firstName": "Johnny",
        "lastName": "Doe",
        "dependants": 3,
        "salary": 2000
    }
    res = requests.put(f"{base_url}/api/Employees", json=payload, headers=headers)

    assert res.status_code == 200
    data = res.json()
    assert data["firstName"] == payload["firstName"]
    assert data["dependants"] == payload["dependants"]

def test_delete_employee(base_url, headers):
    global employee_id
    res = requests.delete(f"{base_url}/api/Employees/{employee_id}", headers=headers)
    assert res.status_code == 200

    # Verify is no longer exist
    res_get = requests.get(f"{base_url}/api/Employees/{employee_id}", headers=headers)
    assert res_get.status_code in [404, 400, 204], f"Expected not found, got {res_get.status_code}"
