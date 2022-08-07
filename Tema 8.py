'''
http://automationpractice.com/index.php
https://the-internet.herokuapp.com/
https://www.techlistic.com/p/selenium-practice-form.html
jules.app

Name
Tag*
Class name*

Optional: La tag si class name veti folosi find elementS! - salvati in lista. Interactionati cu un element la alegere din lista
'''

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

#initializam un browser
s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

chrome.maximize_window()

'''
chrome.get('https://formy-project.herokuapp.com')
chrome.find_element(By.LINK_TEXT, "Autocomplete").click()
chrome.get('https://formy-project.herokuapp.com/autocomplete')
chrome.find_element(By.ID, "autocomplete").send_keys("Block No.1 - First floor- The fourth apartment")
chrome.find_element(By.ID, "street_number").send_keys("Energiei")
chrome.find_element(By.ID, "route").send_keys("Milcov")
chrome.find_element(By.ID, "locality").send_keys("Bacau")
chrome.find_element(By.ID, "administrative_area_level_1").send_keys("Moldovia")
chrome.find_element(By.ID, "postal_code").send_keys("600272")
chrome.find_element(By.ID, "country").send_keys("Romania")

chrome.get('https://formy-project.herokuapp.com')
chrome.find_element(By.PARTIAL_LINK_TEXT, "Enabled").click()
chrome.get('https://formy-project.herokuapp.com/enabled')
chrome.find_element(By.ID, "input").send_keys("Test")

chrome.get('https://formy-project.herokuapp.com')
chrome.find_element(By.PARTIAL_LINK_TEXT, "Datepicker").click()
chrome.get('https://formy-project.herokuapp.com/datepicker')
chrome.find_element(By.ID, "datepicker").send_keys("11/19/2001")

chrome.get('https://formy-project.herokuapp.com')
chrome.find_element(By.PARTIAL_LINK_TEXT, "Complete Web Form").click()
chrome.get('https://formy-project.herokuapp.com/form')
chrome.find_element(By.CLASS_NAME, "form-control").send_keys("Robert")
chrome.find_element(By.ID, "last-name").send_keys("Tanasa")
chrome.find_element(By.ID, "job-title").send_keys("Programmer")
chrome.find_element(By.ID, "radio-button-2").click()
chrome.find_element(By.ID, "checkbox-1").click()
chrome.find_element(By.ID, "select-menu").send_keys("0-1")
chrome.find_element(By.ID, "datepicker").send_keys("08/07/2022")

chrome.get('https://formy-project.herokuapp.com')
chrome.find_element(By.LINK_TEXT, "Switch Window").click()
chrome.get('https://formy-project.herokuapp.com/switch-window')
chrome.find_element(By.ID, "alert-button").click()
'''

sleep(200)
chrome.quit()