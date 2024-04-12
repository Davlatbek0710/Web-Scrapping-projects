# Import necessary modules
from selenium import webdriver
from selenium.webdriver.common.by import By
import pprint

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

# Initialize the Chrome driver with specified options
driver = webdriver.Chrome(options=chrome_options)

# Open the Python.org website
driver.get("https://www.python.org/")

# Find the element containing the list of events
div = driver.find_element(By.CSS_SELECTOR, '.event-widget ul')

# Find all the event dates and event names
event_dates = div.find_elements(By.TAG_NAME, 'time')
event_names = div.find_elements(By.TAG_NAME, 'a')

# Extract the text from event dates
all_time = [t.text for t in event_dates]

# Create a dictionary to store events with their details
events = {
    i: {
        "date": all_time[i],  # Date of the event
        "link": event_names[i].get_attribute('href'),  # Link to the event
        "name": event_names[i].text  # Name of the event
    }
    for i in range(len(event_dates))  # Iterate over the range of event dates
}

# Pretty print the events dictionary
pprint.pprint(events)

# Quit the browser
driver.quit()
