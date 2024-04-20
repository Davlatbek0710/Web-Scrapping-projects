from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from time import sleep

PHONE = YOUR PHONE NUMBER
PSWD = PSWD_FOR_FACEBOOK


options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=options)
driver.maximize_window()

driver.get("https://tinder.com/")

sleep(10)

log_in_btn = driver.find_element(
    By.XPATH,
    value='//*[@id="o515699397"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
log_in_btn.click()

sleep(5)

log_in_btn = driver.find_element(
    By.XPATH,
    value='//*[@id="o-1212681679"]/main/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]')
log_in_btn.click()

# Switch to Facebook login window
sleep(4)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

# Login and hit enter
email_field = driver.find_element(By.NAME, value='email')
email_field.send_keys(PHONE)
pswd_field = driver.find_element(By.NAME, value='pass')
pswd_field.send_keys(PSWD, Keys.ENTER)

# Switch back to Tinder window
driver.switch_to.window(base_window)
print(f"Base window: {driver.title}")

# Delay by 5 seconds to allow page to load.
sleep(10)

# Allow cookies
cookies = driver.find_element(By.XPATH,
                              value='//*[@id="o-1212681679"]/main/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]')
cookies.click()

sleep(7)
# Allow location
allow_location_button = driver.find_element(
    By.XPATH,
    value='//*[@id="o-1212681679"]/main/div/div/div/div[3]/button[1]/div[2]/div[2]')
allow_location_button.click()

sleep(7)

# Disallow notifications
notifications_button = driver.find_element(
    By.XPATH,
    value='//*[@id="o-1212681679"]/main/div/div/div/div[3]/button[2]/div[2]/div[2]')
notifications_button.click()

sleep(10)

like_button = driver.find_element(
    By.XPATH,
    value='//*[@id="o515699397"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[3]/div/div[4]/button/span/span')
# Tinder free tier only allows 100 "Likes" per day. If you have a premium account, feel free to change to a while loop.
for n in range(100):
    sleep(1)
    try:
        print("called")

        like_button.click()

    # Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except Exception:
        sleep(2)
        try:
            add_to_home_screen = driver.find_element(
                By.XPATH,
                value='/html/body/div[1]/div/div[1]/div/main/div[1]/div/div')
            add_to_home_screen.click()
        except NoSuchElementException:
            print("Deep")
            sleep(2)

        print("First exception")
        sleep(1)
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, value=".itsAMatch a")
            match_popup.click()
        # Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            pass
