from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up Chrome options
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)  # Keep the browser window open after the script finishes

# Initialize the Chrome driver with specified options
driver = webdriver.Chrome(options=options)

# Open the Cookie Clicker game page
driver.get("https://orteil.dashnet.org/experiments/cookie/")

# Find the cookie element on the page
cookie = driver.find_element(By.ID, 'cookie')

# Find all store items (excluding the last one which is the special upgrade)
store_divs = driver.find_elements(By.CSS_SELECTOR, '#store div')
# Extract IDs of the store items
store_ids = [item.get_attribute('id') for item in store_divs]
store_ids.remove(store_ids[-1])  # Remove the ID of the last store item

# Find the prices of all store items
list_prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
list_prices.remove(list_prices[-1])  # Remove the price of the last store item
# Extract the prices as integers
all_prices = [int(i.text.split("-")[1].strip().replace(",", "")) for i in list_prices]

# Set a timeout for clicking the cookie
timeout = time.time() + 5

# Set a timeout for stopping the bot after 5 minutes
stop_bot_time = time.time() + 60 * 5  # 5 minutes


# Define a function to find the index of the highest priced item that can be purchased
def pick_value_less_than(current_money):
    result = None

    # Iterate through the sorted list in reverse order
    for value in all_prices[::-1]:
        # Check if the current value is less than current_money
        if value <= current_money:
            result = all_prices.index(value)
            break  # Exit the loop if a suitable value is found
    return result


# Main loop to continuously click the cookie and purchase items
while True:
    # Click the cookie
    cookie.click()

    # Check if it's time to consider purchasing an item
    if time.time() > timeout:
        # Get the current amount of money in the game
        current_money = int(driver.find_element(By.ID, 'money').text.replace(",", ""))
        # Find the index of the highest priced item that can be purchased with the current money
        i = pick_value_less_than(current_money)
        # If such an item is found, click on it to purchase
        if i is not None:
            buy_item = driver.find_element(By.ID, f'{store_ids[i]}')
            buy_item.click()
        # Reset the timeout for considering the next purchase
        timeout = time.time() + 5

    # Check if it's time to stop the bot
    if time.time() > stop_bot_time:
        # Find and print the current cookies per second (cps)
        cookies_second = driver.find_element(By.ID, 'cps')
        print(cookies_second.text)
        # Break out of the loop to stop the script
        break

# Close the browser window
driver.quit()
