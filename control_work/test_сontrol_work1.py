import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.color import Color


driver = webdriver.Chrome()
driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
driver.maximize_window()


first_name = driver.find_element(By.CSS_SELECTOR, "[name='first-name']")
first_name.send_keys("Иван")

last_name = driver.find_element(By.CSS_SELECTOR, "[name='last-name']")
last_name.send_keys("Петров")

address = driver.find_element(By.CSS_SELECTOR, "[name='address']")
address.send_keys("Ленина, 55-3")

email = driver.find_element(By.CSS_SELECTOR, "[name='e-mail']")
email.send_keys("test@skypro.com")

phone = driver.find_element(By.CSS_SELECTOR, "[name='phone']")
phone.send_keys("+7985899998787")

zip_code = driver.find_element(By.CSS_SELECTOR, "[name='zip-code']")
zip_code.send_keys("")

city = driver.find_element(By.CSS_SELECTOR, "[name='city']")
city.send_keys("Москва")

country = driver.find_element(By.CSS_SELECTOR, "[name='country']")
country.send_keys("Россия")

job_position = driver.find_element(By.CSS_SELECTOR, "[name='job-position']")
job_position.send_keys("QA")

company = driver.find_element(By.CSS_SELECTOR, "[name='company']")
company.send_keys("SkyPro")

but_push = driver.find_element(By.CSS_SELECTOR, ".btn.btn-outline-primary.mt-3")
but_push.click()
sleep(2)

# red
red_color_rgba = 'rgba(255, 0, 0, 1)'
red_color = '#FF0000'
# green
green_color_rgba = 'rgba(0, 128, 0, 1)'
green_color = '#008000'

field_red = Color.from_string(driver.find_element(By.ID, "zip-code").value_of_css_property('background-color'))
print(field_red)
def test_red():
    assert field_red.hex == red_color


field_green = Color.from_string(driver.find_element(By.ID, "country").value_of_css_property('background-color'))
print(field_green)
def test_green():
    assert field_green.hex == green_color


# Цвета полей на сайте
# background-color: #f8d7da; #d1e7dd;
