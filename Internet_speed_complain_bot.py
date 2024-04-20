'''
    This code is an automation complaint about the speed of your internet
    to your personal ISP (Internet Service Provider)
    first bot gets the download and upload speeds of internet and checks if it
    satisfies the promised speeds, if it doesn't
    then the bot logs in to twitter and posts a complaint by tagging the username of ISP
'''


from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys

TWITTER_EMAIL = YOUR EMAIL
TWITTER_PASSWORD = YOUR PASSWORD
PROMISED_DOWN = 150
PROMISED_UP = 10
SPEEDTEST_WEBSITE = 'https://www.speedtest.net/'


class InternetSpeedTwitterBot:
    def __init__(self):
        self.up = 0
        self.down = 0
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()

    def get_internet_speed(self):
        self.driver.get(SPEEDTEST_WEBSITE)
        sleep(2)
        start = self.driver.find_element(By.CSS_SELECTOR, 'span.start-text')
        start.click()
        sleep(60)
        download = self.driver.find_element(
            By.CSS_SELECTOR,
            value='span[class="result-data-large number result-data-value download-speed"]'
        )
        print(f"Download: {download.text} Mbps")
        self.down = float(download.text)
        up = self.driver.find_element(
            By.CSS_SELECTOR,
            value='span[class="result-data-large number result-data-value upload-speed"]'
        )
        print(f"Upload: {up.text} Mbps")
        self.up = float(up.text)

    def tweet_at_provider(self):
        self.driver.get('https://twitter.com/login')
        sleep(15)
        email_field = self.driver.find_element(By.TAG_NAME, 'input')
        email_field.send_keys(TWITTER_EMAIL)
        next = self.driver.find_element(
            By.XPATH,
            value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div')
        next.click()

        sleep(60)

        password_field = self.driver.find_element(By.NAME, 'password')
        password_field.send_keys(TWITTER_PASSWORD, Keys.ENTER)
        sleep(15)
        post = (f"Hey @UZTELECOM1, Internet  Provider, why is my internet speed\n"
                f"{self.down}down/{self.up}up when I pay for 150down/10up?")
        self.driver.find_element(
            By.CSS_SELECTOR,
            value='br[data-text="true"]'
        ).send_keys(post)
        sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, 'div[data-testid="tweetButtonInline"]').click()


inst = InternetSpeedTwitterBot()
inst.get_internet_speed()
inst.tweet_at_provider()
