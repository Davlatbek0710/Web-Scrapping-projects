from selenium import webdriver
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=options)

driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name_field = driver.find_element(By.NAME, 'fName')
first_name_field.send_keys('Saber')
driver.implicitly_wait(3000)
lname_field = driver.find_element(By.NAME, 'lName')
lname_field.send_keys('King')
driver.implicitly_wait(3000)
email_field = driver.find_element(By.NAME, 'email')
email_field.send_keys('saber@gmail.com')
driver.implicitly_wait(3000)
button = driver.find_element(By.TAG_NAME, 'button')
button.click()
