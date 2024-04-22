'''
    This program is designed to scrape real estate data from a website
    (in this case, from 'https://appbrewery.github.io/Zillow-Clone/')
    and then automatically fill out a Google Form with that data using Selenium.
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
from time import sleep

google_form = 'https://docs.google.com/forms/d/e/1FAIpQLSf5GGHxw4uFOaXXbaesJqjc17r_9qn4p_4BpA5GXxWW0csCEQ/viewform?usp=sf_link'

def fetch_all_data():
    header = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
    }
    result = requests.get('https://appbrewery.github.io/Zillow-Clone/', headers=header)
    soup = BeautifulSoup(result.content, 'html.parser')
    list_of_links = [
        link.get('href')
        for link in
        soup.select(selector='ul[class="List-c11n-8-84-3-photo-cards"] li .StyledPropertyCardDataArea-anchor')
    ]

    list_of_prices = [
        price.text[:6]
        for price in (soup.select(selector='span[data-test="property-card-price"]'))
    ]
    # print(len(list_of_links))
    # print(len(list_of_prices))

    lst = [
        address.text
        for address in soup.find_all(name='address')
    ]
    # Filtering process of all address string
    list_of_addresses = []
    c = 0
    for i in lst:
        address = [j.strip() for j in i.strip().replace('|', '').split(',')]
        if len(address) >= 4:
            list_of_addresses.append(', '.join(address[1:]))
        else:
            list_of_addresses.append(', '.join(address))
        # print(list_of_addresses[c])
        # c += 1
    # print(len(list_of_addresses))
    return list_of_addresses, list_of_prices, list_of_links


# Selenium part
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get(google_form)
sleep(3)
datas = fetch_all_data()
for i in range(len(datas[0])):
    input_fields = driver.find_elements(By.CSS_SELECTOR, 'input[type="text"]')
    input_fields[0].send_keys(datas[0][i])
    input_fields[1].send_keys(datas[1][i])
    input_fields[2].send_keys(datas[2][i])
    send = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
    send.click()
    sleep(1)
    driver.find_element(By.LINK_TEXT, 'Отправить ещё один ответ').click()
    sleep(1)
driver.quit()
