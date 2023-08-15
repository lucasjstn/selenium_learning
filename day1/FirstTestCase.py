import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj=Service(r"C:\Users\010130853\Desktop\xd\chromedriver_win32\chromedriver.exe")
url_path = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

driver = webdriver.Chrome(service=service_obj)
driver.get(url_path)

time.sleep(5)

# driver.find_element(by="name", value="username").send_keys("Admin")
# driver.find_element_by_name("username").send_keys("Admin")
driver.find_element(By.NAME, "username").send_keys("Admin")
# driver.find_element(by="name", value="password").send_keys("admin123")
driver.find_element(By.NAME, "password").send_keys("admin123")

# provavelmente vai clicar em qualquer botão
driver.find_element_by_xpath("//button").click()

act_title=driver.title
exp_title="OrangeHRM" 

if act_title==exp_title:
    print("Test Passed")
else:
    print("Test Failed")
