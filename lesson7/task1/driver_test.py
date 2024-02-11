import pytest
from selenium import webdriver

from registration_page import RegistrationPage


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_registration(driver):
    registration_page = RegistrationPage(driver)
    registration_page.fill_form(
        first_name="John",
        last_name="Doe",
        address="123 Main St",
        email="john@example.com",
        phone="1234567890",
        zip_code="12345",
        city="Anytown",
        country="USA",
        job_position="Tester",
        company="Test Company"
    )
    registration_page.submit_form()


def test_red_field(driver):
    registration_page = RegistrationPage(driver)
    field_red = registration_page.get_zip_code_field_color()
    assert field_red.hex == '#FF0000'

def test_green_field(driver):
    registration_page = RegistrationPage(driver)
    field_green = registration_page.get_country_field_color()
    assert field_green.hex == '#008000'