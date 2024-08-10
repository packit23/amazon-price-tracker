# Amazon Price Tracker Template

This Python script allows users to monitor the price of any Amazon product and send an email alert when the price drops below a specified threshold.

## Prerequisites

- Python 3.x
- `requests` and `beautifulsoup4` libraries
- An Amazon account (to get the product URL)
- An email account (Gmail) for sending alerts

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/amazon-price-tracker.git
    ```

2. Install the required Python packages:
    ```bash
    pip install requests beautifulsoup4
    ```

3. Set up environment variables for your email credentials:
    - `EMAIL_USER`: Your email address (Gmail or other)
    - `EMAIL_PASS`: Your email password or app-specific password

    You can set these variables in your environment or include them in a `.env` file and use `python-dotenv` to load them.

## Usage

1. Run the script:
    ```bash
    python check_price.py
    ```

2. Follow the prompts to enter the Amazon product URL and your desired price threshold.

3. Enter the recipient's email address where the alert should be sent.

4. The script will check the price and send an email if the price drops below the threshold.

## Example

```bash
Enter the Amazon product URL: https://www.amazon.com/dp/B08V1L1WYD/
Enter the price threshold: 200
Enter the recipient email address: example@example.com
Product: WD 4TB My Cloud Home Personal Cloud
Current Price: $179
The email has been sent.

## Important Notes

- This script currently supports Gmail by default. If you want to use another email provider, update the SMTP server and port settings in the send_mail() function.

-Ensure you are using an app-specific password if two-factor authentication is enabled on your email account.

