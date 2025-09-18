from ui_tests.pages.employees_page import EmployeesPage


def test_add_employee(logged_in):
    browser = logged_in
    employees_page = EmployeesPage(browser)

    employees_page.add_employee("Fernando", "Suarez", 2)


def test_edit_employee(logged_in):
    browser = logged_in
    employees_page = EmployeesPage(browser)

    employees_page.edit_employee("Fernando", 7)


def test_delete_employee(logged_in):
    browser = logged_in
    employees_page = EmployeesPage(browser)

    employees_page.delete_employee("Fernando")


