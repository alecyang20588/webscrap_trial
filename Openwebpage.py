import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# Initialize the driver
driver = webdriver.Chrome()

# Open the webpage (please replace 'https://www.example.com' with your actual URL)
driver.get('http://192.168.0.217/cgi-bin/spectra-menu.cgi?language=en')

# Find the username and password fields and enter the values
driver.find_element(By.NAME, 'name').clear()
driver.find_element(By.NAME, 'name').send_keys('webuser')
driver.find_element(By.NAME, 'pass').send_keys('1234')

# Select "Batch report" from the dropdown
select = Select(driver.find_element(By.NAME, 'option'))
#select.select_by_visible_text(' Batch report ')
select.select_by_value('G')


# Click the "Display" button
driver.find_element(By.NAME, 'show').click()
time.sleep(10)