from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color
from time import sleep


class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self.driver.maximize_window()

    def fill_form(self, first_name, last_name, address, email, phone, zip_code, city, country, job_position, company):
        self.driver.find_element(By.CSS_SELECTOR, "[name='first-name']").send_keys(first_name)
        self.driver.find_element(By.CSS_SELECTOR, "[name='last-name']").send_keys(last_name)
        self.driver.find_element(By.CSS_SELECTOR, "[name='address']").send_keys(address)
        self.driver.find_element(By.CSS_SELECTOR, "[name='e-mail']").send_keys(email)
        self.driver.find_element(By.CSS_SELECTOR, "[name='phone']").send_keys(phone)
        self.driver.find_element(By.CSS_SELECTOR, "[name='zip-code']").send_keys(zip_code)
        self.driver.find_element(By.CSS_SELECTOR, "[name='city']").send_keys(city)
        self.driver.find_element(By.CSS_SELECTOR, "[name='country']").send_keys(country)
        self.driver.find_element(By.CSS_SELECTOR, "[name='job-position']").send_keys(job_position)
        self.driver.find_element(By.CSS_SELECTOR, "[name='company']").send_keys(company)

    def submit_form(self):
        self.driver.find_element(By.CSS_SELECTOR, ".btn.btn-outline-primary.mt-3").click()

    def green_color_first(self):
        first_field = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.ID, "first-name"))
        )
        return Color.from_string(first_field.value_of_css_property('color'))

    def green_color_last(self):
        last_field = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.ID, "last-name"))
        )
        return Color.from_string(last_field.value_of_css_property('color'))

    def green_color_address(self):
        address_field = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.ID, "address"))
        )
        return Color.from_string(address_field.value_of_css_property('color'))

    def green_color_mail(self):
        mail_field = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.ID, "e-mail"))
        )
        return Color.from_string(mail_field.value_of_css_property('color'))

    def green_color_phone(self):
        phone_field = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.ID, "phone"))
        )
        return Color.from_string(phone_field.value_of_css_property('color'))

    def zip_red_color(self):
        zip_code_field = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.ID, "zip-code"))
        )
        return Color.from_string(zip_code_field.value_of_css_property('color'))

    def green_color_city(self):
        city_field = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.ID, "city"))
        )
        return Color.from_string(city_field.value_of_css_property('color'))

    def green_color_country(self):
        country_field = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.ID, "country"))
        )
        return Color.from_string(country_field.value_of_css_property('color'))

    def green_color_job(self):
        job_field = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.ID, "job-position"))
        )
        return Color.from_string(job_field.value_of_css_property('color'))

    def green_color_company(self):
        company_field = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.ID, "company"))
        )
        return Color.from_string(company_field.value_of_css_property('color'))
