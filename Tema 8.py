from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

#initializam un browser
s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

chrome.maximize_window()

chrome.get('https://formy-project.herokuapp.com')
chrome.find_element(By.LINK_TEXT, 'Autocomplete').click()
chrome.get('https://formy-project.herokuapp.com/autocomplete')
chrome.find_element(By.ID, 'autocomplete').send_keys('Block No.1 - First floor- The fourth apartment')
chrome.find_element(By.ID, 'street_number').send_keys('Energiei')
chrome.find_element(By.ID, 'route').send_keys('Milcov')
chrome.find_element(By.ID, 'locality').send_keys('Bacau')
chrome.find_element(By.ID, 'administrative_area_level_1').send_keys('Moldovia')
chrome.find_element(By.ID, 'postal_code').send_keys('600272')
chrome.find_element(By.ID, 'country').send_keys('Romania')
sleep(10)

chrome.get('https://formy-project.herokuapp.com')
chrome.find_element(By.PARTIAL_LINK_TEXT, 'Enabled').click()
chrome.get('https://formy-project.herokuapp.com/enabled')
chrome.find_element(By.ID, 'input').send_keys('Test')

chrome.get('https://formy-project.herokuapp.com')
chrome.find_element(By.PARTIAL_LINK_TEXT, 'Datepicker').click()
chrome.get('https://formy-project.herokuapp.com/datepicker')
chrome.find_element(By.ID, 'datepicker').send_keys('11/19/2001')

chrome.get('https://formy-project.herokuapp.com')
chrome.find_element(By.PARTIAL_LINK_TEXT, 'Complete Web Form').click()
chrome.get('https://formy-project.herokuapp.com/form')

chrome.find_element(By.TAG_NAME, 'input').send_keys('Robert')
list_input = chrome.find_elements(By.TAG_NAME, 'input')
list_input[1].send_keys('Tanasa')
list_input[2].send_keys('Programmer')
sleep(10)

chrome.find_element(By.ID, 'radio-button-2').click()
chrome.find_element(By.ID, 'checkbox-1').click()
chrome.find_element(By.ID, 'select-menu').send_keys('0-1')
chrome.find_element(By.ID, 'datepicker').send_keys('08/07/2022')
chrome.find_element(By.XPATH, '/html/body/div/form/div/div[8]/a').click()

chrome.get('https://the-internet.herokuapp.com')
chrome.find_element(By.PARTIAL_LINK_TEXT, 'Forgot Password').click()
chrome.get('https://the-internet.herokuapp.com/forgot_password')
chrome.find_element(By.NAME, 'email').send_keys('okroeger@gmail.com')
chrome.find_element(By.ID, 'form_submit').click()

chrome.get('https://the-internet.herokuapp.com')
chrome.find_element(By.LINK_TEXT, 'Dropdown').click()
chrome.get('https://the-internet.herokuapp.com/dropdown')
chrome.find_element(By.ID, 'dropdown').send_keys('Option 2')

chrome.get('https://the-internet.herokuapp.com')
chrome.find_element(By.LINK_TEXT, 'Key Presses').click()
chrome.get('https://the-internet.herokuapp.com/key_presses')
chrome.find_element(By.ID, 'target').send_keys('h')

chrome.get('https://the-internet.herokuapp.com')
chrome.find_element(By.PARTIAL_LINK_TEXT, 'Form Authentication').click()
chrome.get('https://the-internet.herokuapp.com/login')
chrome.find_element(By.NAME, 'username').send_keys('tomsmith')
chrome.find_element(By.NAME, 'password').send_keys('SuperSecretPassword!')
chrome.find_element(By.XPATH, '//*[@id="login"]/button/i').click()
chrome.find_element(By.XPATH, '//*[@id="content"]/div/a/i').click()

sleep(20)
chrome.quit()
