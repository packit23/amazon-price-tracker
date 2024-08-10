import requests
from bs4 import BeautifulSoup as bs
import smtplib
import os


URL = 'https://www.amazon.com/dp/B08V1L1WYD/ref=twister_B0D51CJFB3?_encoding=UTF8&th=1'
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0'}


def check_price():
    try:
        page = requests.get(URL, headers=header)
        page.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching page: {e}")
        return


    soup = bs(page.content, 'html.parser')


    title = soup.find(id="productTitle")
    price = soup.find('span', class_='a-price-whole')


    if title and price:
        title_text = title.get_text().strip()
        price_text = price.get_text().replace(',', '')
        try:
            price_value = float(price_text)
        except ValueError:
            print(f"Error parsing price: {price_text}")
            return


        print(title_text)
        print(price_value)


        if price_value < 200:
            send_mail()
    else:
        print("Could not find product title or price on the page.")


def send_mail():
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
       
        # Use environment variables for email and password
        email = os.getenv('EMAIL_USER')
        password = os.getenv('EMAIL_PASS')


        server.login(email, password)


        subject = 'Price for the WD NAS Drive Fell Down'
        body = f'Here is the Amazon link: {URL}'


        msg = f"Subject: {subject}\n\n{body}"


        server.sendmail(email, 'gman233519@gmail.com', msg)
        print('The email has been sent.')


        server.quit()
    except Exception as e:
        print(f"Error sending email: {e}")


check_price()
