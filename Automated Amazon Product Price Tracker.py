import requests
from bs4 import BeautifulSoup
import lxml
from smtplib import SMTP

YOUR_EMAIL = YOUR EMAIL
PASSWORD = YOUR PASSWORD
header = {
    "User-Agent":"Chrome/119.0.0.0",
    "Accept-Language":"en-US,en;q=0.9,pt-BR;q=0.8,pt;q=0.7"
}

url_of_a_product = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
result = requests.get(url_of_a_product, headers=header)

soup = BeautifulSoup(result.content, "lxml")
price = float(soup.find(class_="a-offscreen").getText().split("$")[1])

print("Price: $", price)
if price <= 100:
    product_name = soup.find(id="productTitle").getText()
    link = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
    with SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=YOUR_EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=YOUR_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{product_name}\n{link}".encode('utf-8').strip(),
            to_addrs="some_email@gmail.com",
        )
    print("Message Sent!")



