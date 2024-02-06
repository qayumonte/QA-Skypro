from time import sleep
from selenium import webdriver
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
driver.get("https://www.aviasales.ru/")
driver.maximize_window()
sleep(1)

# установка курсора в поле "Откуда"
field_where_from = driver.find_element(By.ID, "avia_form_origin-input")
field_where_from.click()
sleep(1)

# установка курсора в поле "Куда"
field_where = driver.find_element(By.ID, "avia_form_destination-input")
field_where.click()
sleep(1)

# установка курсора в поле "Когда"
field_when = driver.find_element(By.XPATH, "//html/body/div[7]/div[2]/div/div/div/div[2]/form/div[1]/div/button[1]")
field_when.click()
sleep(1)

# установка курсора в поле "Обратно"
field_black = driver.find_element(By.XPATH, "//html/body/div[7]/div[2]/div/div/div/div[2]/form/div[1]/div/button[2]")
field_black.click()
sleep(1)

# Клик на логотип
button_avia = driver.find_element(By.XPATH, "//html/body/div[1]/div/div/a/span")
button_avia.click()
sleep(1)

# Чек-бокс "Открыть Ostrovok.ru в новой вкладке"
ostrovok = driver.find_element(By.CLASS_NAME, "s__BGUqp9s2kxbNEnDjdIYc")
ostrovok.click()
sleep(2)
ostrovok.click()
sleep(1)

# Клик по кнопке "Найти билеты"
find_tickets = driver.find_element(By.XPATH, "//html/body/div[7]/div[2]/div/div/div/div[2]/form/div[3]")
find_tickets.click()
sleep(3)
