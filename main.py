import requests
import smtplib
from bs4 import BeautifulSoup

URL = "https://www.amazon.in/TheGiftKart-Cover-Hybrid-Smoked-Bumper/dp/B08YNL9N71/ref=sr_1_2_sspa?dchild=1&keywords=redmi%2Bnote%2B10%2Bcase&qid=1630669132&sr=8-2-spons&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFRSVlTQTBTU1hSOFomZW5jcnlwdGVkSWQ9QTA2MTIzNjYxRE5IMlU3OTUzMVZJJmVuY3J5cHRlZEFkSWQ9QTA0NjkyODYxM1I3WkJNUkMzRDA0JndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ&th=1"
EMAIL = "Your_Email"
PASSWORD = "Your_Password"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}
# Getting Website Information
response = requests.get(url=URL, headers=header)
website_info = response.text

# Scraping
soup = BeautifulSoup(website_info, "html.parser")
rupee_price = soup.find(name="span", id="priceblock_saleprice").getText()

title = soup.find(name="span", id="productTitle").getText().strip()
price = float(rupee_price.split("₹")[1])

if price < 260:
    print("Sending.....")
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL,
                            to_addrs="joefelix.a2003@gmail.com",
                            msg=f"Subject:Price Droped\n\n {title}is now at Rupees: '{price}' \n\nCheckout: {URL}")
        print("Sent!!!!")

