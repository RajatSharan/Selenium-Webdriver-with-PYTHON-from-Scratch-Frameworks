import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

name="Rajat"
service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.ID,"name").send_keys(name)
driver.find_element(By.ID, "alertbtn").click()
alert = driver.switch_to.alert
alertText = alert.text
print(alertText)
assert name in alertText
alert.accept()

time.sleep(1)