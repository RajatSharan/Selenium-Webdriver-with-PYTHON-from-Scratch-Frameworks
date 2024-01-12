from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#---ChromeDriver -Chrome browser
"""
service_obj=Service()
Webdriver is the class
driver=webdriver.Chrome(service=service_obj) #Invoke the Browser
"""
#---FireFoxDriver -FireFox browser
#service_obj=Service()
#driver=webdriver.Firefox(service=service_obj)

#---EdgeDriver -EdgeDriver browser
service_obj=Service()
driver=webdriver.Edge(service=service_obj)
driver.get("https://rahulshettyacademy.com/") #Open the Browser
print(driver.title) # title of project
print(driver.current_url) #To check the current url
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.minimize_window()
driver.refresh()
driver.back()
driver.forward()
driver.close()#Close the browser
