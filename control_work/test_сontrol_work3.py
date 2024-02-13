import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    yield driver
    driver.quit()


def test_shopping_flow(driver):
    # Входщ в ЛК
    user_name = driver.find_element(By.ID, "user-name")
    user_name.send_keys("standard_user")
    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")
    login_but = driver.find_element(By.ID, "login-button")
    login_but.click()

    # Добавляю товар в корзину
    add_cart1 = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    add_cart1.click()

    add_cart2 = driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    add_cart2.click()

    add_cart3 = driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie")
    add_cart3.click()

    open_cart = driver.find_element(By.ID, "shopping_cart_container")
    open_cart.click()

    checkout_button = driver.find_element(By.ID, "checkout")
    checkout_button.click()

    # Ввожу данные покупателя
    first_name = driver.find_element(By.ID, "first-name")
    first_name.click()
    first_name.send_keys("Юлия")

    last_name = driver.find_element(By.ID, "last-name")
    last_name.click()
    last_name.send_keys("Мелихова")

    code = driver.find_element(By.ID, "postal-code")
    code.click()
    code.send_keys("399770")
    continue_but = driver.find_element(By.ID, "continue")
    continue_but.click()

    # Сравниваю итоговую стоимость
    sum_total = driver.find_element(By.XPATH, "//div[@class='summary_info_label summary_total_label']")
    sum_text = sum_total.text
    expected_total = "$58.29"
    int_total = sum_text.split(":")[1].strip()
    comparison_result = f"Expected total: {expected_total}, Actual total: {int_total}"
    print(comparison_result)
    assert int_total == expected_total, f"Ожидаемая сумма {expected_total}, фактическая сумма {int_total}."
