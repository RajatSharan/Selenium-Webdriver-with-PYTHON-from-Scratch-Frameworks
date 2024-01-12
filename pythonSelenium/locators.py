from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#ChromeDriver

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("Rajat")
driver.find_element(By.NAME,"email").send_keys("errajat.shara@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("12345")
driver.find_element(By.ID,'exampleCheck1').click()

#//tagname[@attribute='value']

driver.find_element(By.XPATH,"//input[@type='submit']").click()
message=driver.find_element(By.CLASS_NAME,"alert.alert-success.alert-dismissible").text
print(message)
assert "Success!" in message
driver.find_element(By.XPATH,"(//input[@type='text'])[3]").send_keys("RONI")
driver.find_element(By.XPATH,"(//input[@type='text'])[3]").clear()
