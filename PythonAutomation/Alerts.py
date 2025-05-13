import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service('C:/Drives/chromedriver-win64/chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(service=service)

#driver.get('https://the-internet.herokuapp.com/javascript_alerts')

#driver.maximize_window()

# driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Prompt']").click()
# time.sleep(3)
#
# alert_window = driver.switch_to.alert #get the alert window
# print(alert_window.text)
# alert_window.send_keys('welcome')
# #alert_window.accept() #close alert window using ok
# alert_window.dismiss()
#

# driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Alert']").click()
# time.sleep(3)
#
# my_alert =  driver.switch_to.alert
# my_alert.accept()

#driver.close()

#AUTHONTICATION
#driver.get('https://the-internet.herokuapp.com/basic_auth')
#BYPASS
driver.get('https://admin:admin@the-internet.herokuapp.com/basic_auth')

input('Print')