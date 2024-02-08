import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    driver.maximize_window()
    yield driver
    driver.quit()

def test_calculator(driver):
    delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
    delay_input.clear()
    delay_input.send_keys("45")

    elements_with_seven = driver.find_elements(By.XPATH, "//*[contains(text(), '7')]")
    for element7 in elements_with_seven:
        element7.click()

    elements_with_plus = driver.find_elements(By.XPATH, "//*[contains(text(), '+')]")
    for element_plus in elements_with_plus:
        element_plus.click()

    elements_with_eight = driver.find_elements(By.XPATH, "//*[contains(text(), '8')]")
    for element8 in elements_with_eight:
        element8.click()

    elements_with_eq = driver.find_elements(By.XPATH, "//*[contains(text(), '=')]")
    for element_eq in elements_with_eq:
        element_eq.click()

    wait = WebDriverWait(driver, 46)
    result_element = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), '15')]")))
    result_text = result_element.text
    expected_result = "15"
    assert result_text == expected_result
    print(f"Ожидаемый результат {expected_result}, полученный результат {result_text} .")
