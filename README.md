# amazon-price-tracker
A Python script to track Amazon product prices and send email alerts when prices drop.

This Python script monitors the price of a specific Amazon product and sends an email alert if the price drops below a certain threshold.

## Prerequisites

- Python 3.x
- `requests` and `beautifulsoup4` libraries
- An Amazon account
- An email account for sending alerts

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/amazon-price-tracker.git

## Usage

Modify the `URL` in the script to the Amazon product you want to track. The script will check the price and send an email alert if the price drops below $200.

Run the script:
```bash
python check_price.py
