from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj=Service()
driver=webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/client/")
driver.find_element(By.LINK_TEXT,"Forgot password?").click()
driver.find_element(By.XPATH,"//form/div[1]/input").send_keys("errajat.sharan@gmail.com")
driver.find_element(By.XPATH,"//form/div[2]/input").send_keys("Hello@123")
driver.find_element(By.ID,"confirmPassword").send_keys("Hello@123")
driver.find_element(By.XPATH,"//button[@type='submit']").click()