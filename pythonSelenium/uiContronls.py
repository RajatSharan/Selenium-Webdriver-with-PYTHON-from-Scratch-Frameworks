import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

"""Handling CheckBox dynamically"""

"""
checkboxs=driver.find_elements(By.XPATH,"//input[@type='checkbox']")
print(len(checkboxs))
for checkbox in checkboxs:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()
        break
"""

"""Handling RadioButton dynamically"""

radioButton=driver.find_elements(By.XPATH,"//input[@Type='radio']")

for radio in radioButton:
    if radio.get_attribute('value') == "radio2":
        radio.click()
        assert radio.is_selected()
        break


displayedText=driver.find_element(By.NAME,"show-hide")
displayedText.is_displayed()
assert driver.find_element(By.ID,"displayed-text").is_displayed()
driver.find_element(By.ID,"hide-textbox").click()
assert not driver.find_element(By.ID,"displayed-text").is_displayed()
time.sleep(1)