from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Keep Chrome browser open after program finishes
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

# Create and configure the chrome webdriver
driver = webdriver.Chrome(options=options)

# Navigating to Wikipedia
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# Find anchor tag using CSS Selector to get article count number
article_count = driver.find_element(By.CSS_SELECTOR, value='#articlecount a')

# Clicking links action
article_count.click()

# Searching, by inputting some text into input field
input_filed = driver.find_element(By.NAME, 'search')
input_filed.send_keys('Python', Keys.ENTER)




