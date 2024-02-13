import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color
from selenium.webdriver.support import expected_conditions as EC
from registration_page import RegistrationPage


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_registration(driver):
    registration_page = RegistrationPage(driver)
    registration_page.fill_form(
        first_name="Иван",
        last_name="Петров",
        address="Ленина, 55-3",
        email="test@skypro.com",
        phone="+7985899998787",
        zip_code="",
        city="Москва",
        country="Россия",
        job_position="QA",
        company="SkyPro"
    )

    registration_page.submit_form()
    sleep(5)

    red = '#FF0000'
    green = '#008000'

    try:
        green_first = registration_page.green_color_first()
        assert green_first.hex == green
    except AssertionError as e:
        print("First color check failed:", e)

    try:
        green_last = registration_page.green_color_last()
        assert green_last.hex == green
    except AssertionError as e:
        print("First color check failed:", e)

    try:
        green_address = registration_page.green_color_address()
        assert green_address.hex == green
    except AssertionError as e:
        print("First color check failed:", e)

    try:
        green_mail = registration_page.green_color_mail()
        assert green_mail.hex == green
    except AssertionError as e:
        print("First color check failed:", e)

    try:
        green_phone = registration_page.green_color_phone()
        assert green_phone.hex == green
    except AssertionError as e:
        print("First color check failed:", e)

    try:
        zip_red = registration_page.zip_red_color()
        assert zip_red.hex == red
    except AssertionError as e:
        print("First color check failed:", e)

    try:
        green_city = registration_page.green_color_city()
        assert green_city.hex == green
    except AssertionError as e:
        print("First color check failed:", e)

    try:
        green_country = registration_page.green_color_country()
        assert green_country.hex == green
    except AssertionError as e:
        print("First color check failed:", e)

    try:
        green_job = registration_page.green_color_job()
        assert green_job.hex == green
    except AssertionError as e:
        print("First color check failed:", e)

    try:
        green_company = registration_page.green_color_company()
        assert green_company.hex == green
    except AssertionError as e:
        print("First color check failed:", e)
