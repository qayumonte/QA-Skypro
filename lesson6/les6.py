from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()


# Задание 1. Нажатие на кнопку
driver.get("http://uitestingplayground.com/ajax")
driver.maximize_window()

but_blue = driver.find_element(By.ID, "ajaxButton").click()

green_message = WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "bg-success")))
text = green_message.text
print(text)


# Задание 2. Переименовать кнопку
driver.get("http://uitestingplayground.com/textinput")
driver.maximize_window()

input_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "newButtonName")))

input_field.send_keys("SkyPro")

blue_button = driver.find_element(By.ID, "updatingButton")
blue_button.click()

button_text = blue_button.text
print(button_text)


# Задание 3. Дождаться картинки
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
driver.maximize_window()

image = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.ID, "award")))
image_src = image.get_attribute("src")
print("SRC атрибут картинки:", image_src)

driver.quit()


