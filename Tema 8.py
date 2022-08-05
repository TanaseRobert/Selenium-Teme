'''
http://automationpractice.com/index.php
https://the-internet.herokuapp.com/
https://www.techlistic.com/p/selenium-practice-form.html
jules.app

Alegeti cate 3 elemente din fiecare tip de selector din urmatoarele categorii:

Id
Link text
Partial link text
Name
Tag*
Class name*

obs:
Probabil nu veti gasi un singur website care sa cuprinda toate variantele de mai sus, astfel ca va recomandam sa folositi mai multe site-uri
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

#fereastra mare
chrome.maximize_window()

#fereastra mica
#chrome.minimize_window()

#deschidem o pagina
#chrome.get('https://www.phptravels.net/')

#selector BY id
'''
first_name = chrome.find_element(By.ID, "fadein")
first_name.send_keys("Emanuel")
first_name.clear()
first_name.send_keys("Emanuel")

last_name = chrome.find_element(By.ID, "last-name")
last_name.send_keys("Tanasa")
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
sleep(200)
chrome.quit()