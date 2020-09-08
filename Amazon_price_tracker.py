import requests
from bs4 import BeautifulSoup
import smtplib
import time
URL = 'https://www.amazon.in/gp/product/B083WY1W2S?pf_rd_r=174RNVEMGDTKCQ286D2D&pf_rd_p=649eac15-05ce-45c0-86ac-3e413b8ba3d4'

headers = {
    "User Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'}


def check_price():

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')
    try:
        title = soup.find(id="productTitle").get_text()
    except AttributeError:
        print("Product: -")

    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[2:8].replace(',', ''))

    if(converted_price < 15, 999):
        send_mail()

    print(converted_price)
    print(title.strip())

    if(converted_price < 13, 999):
        send_mail()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('imthiaz123@gmail.com', 'vjrqjoswytuxegqj')

    subject = "DISCOUNT!!! PRICE IS DOWN!"

    body = "Check the Amazon link below: https://www.amazon.in/gp/product/B083WY1W2S?pf_rd_r=174RNVEMGDTKCQ286D2D&pf_rd_p=649eac15-05ce-45c0-86ac-3e413b8ba3d4"

    msg = f"Subject:{subject}\n\n{body}"

    server.sendmail(
        'imthiaz123@gmail.com',
        'muhassinimthiaz@gmail.com',
        msg
    )

    print("EMAIL HAS BEEN SENT!!!")

    server.quit()


while(True):
    check_price()
    time.sleep(3600)
