import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        user_name = self.driver.find_element(By.ID, "user-name")
        user_name.send_keys(username)
        password_field = self.driver.find_element(By.ID, "password")
        password_field.send_keys(password)
        login_button = self.driver.find_element(By.ID, "login-button")
        login_button.click()


class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def add_items_to_cart(self):
        add_cart1 = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
        add_cart1.click()

        add_cart2 = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light")
        add_cart2.click()

        add_cart3 = self.driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie")
        add_cart3.click()

    def open_cart(self):
        open_cart_button = self.driver.find_element(By.ID, "shopping_cart_container")
        open_cart_button.click()
        checkout_button = self.driver.find_element(By.ID, "checkout")
        checkout_button.click()


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_shipping_info(self, first_name, last_name, postal_code):
        first_name_field = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.ID, "first-name"))
        )
        first_name_field.send_keys(first_name)

        last_name_field = self.driver.find_element(By.ID, "last-name")
        last_name_field.send_keys(last_name)

        code_field = self.driver.find_element(By.ID, "postal-code")
        code_field.send_keys(postal_code)

        continue_but = self.driver.find_element(By.ID, "continue")
        continue_but.click()


class SummaryPage:
    def __init__(self, driver):
        self.driver = driver

    def get_total_amount(self):
        sum_total = self.driver.find_element(By.XPATH, "//div[@class='summary_info_label summary_total_label']")
        return sum_total.text
