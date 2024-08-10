import requests
from bs4 import BeautifulSoup as bs
import smtplib
import os

# Ask the user to input the Amazon product URL and the desired price threshold
URL = input("Enter the Amazon product URL: ")
price_threshold = float(input("Enter the price threshold: "))

# Header to mimic a browser request
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

        print(f"Product: {title_text}")
        print(f"Current Price: ${price_value}")

        if price_value < price_threshold:
            send_mail(title_text, price_value)
    else:
        print("Could not find product title or price on the page.")

def send_mail(product_title, current_price):
    try:
        # Use environment variables for email and password
        email = os.getenv('EMAIL_USER')
        password = os.getenv('EMAIL_PASS')
        recipient = input("Enter the recipient email address: ")

        # Set up the email server and send the email
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()

        server.login(email, password)

        subject = f'Price Drop Alert: {product_title}'
        body = f'The price of "{product_title}" has dropped to ${current_price}.\nCheck it out here: {URL}'

        msg = f"Subject: {subject}\n\n{body}"

        server.sendmail(email, recipient, msg)
        print('The email has been sent.')

        server.quit()
    except Exception as e:
        print(f"Error sending email: {e}")

check_price()
