#import libraries  

#control browser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#automatically mabage browser driver
from webdriver_manager.chrome import ChromeDriverManager

#sending mail
import smtplib

#scheduling script
import schedule
import time
import os
from dotenv import load_dotenv

load_dotenv()

#configuration
URL="https://www.amazon.in/Sony-ILCE-7M3K-Full-Frame-Mirrorless-Interchangeable/dp/B07DPSQRFF/?_encoding=UTF8&ref_=pd_hp_d_atf_ci_mcx_mr_ca_hp_atf_d"
TARGET_PRICE=130000.0
PRICE_SELECTOR_XPATH = '//*[@id="corePrice_feature_div"]//span[contains(@class, "a-price-whole")]'

#get price of product
def get_price():
    """
    Initialize a selenium webdriver,goes to the url and scrapes the current price
    """
    #chrome options to run in "headless" mode (run chrome without visible window)
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36")

    #automatically install and manage chrome driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    print("Webdriver inintialized")

    try:
        #go to the product
        driver.get(URL)
        print(f"Opening: {URL}")

        #wait for price to be visible
        wait=WebDriverWait(driver, 10)
        price_element= wait.until(EC.visibility_of_element_located((By.XPATH, PRICE_SELECTOR_XPATH)) )
        price_str=price_element.text

        #text preprocessing
        price_str = price_str.replace(",", "").replace("₹", "").strip()
        current_price=float(price_str)

        print(f"Found price: {current_price}")
        return current_price
    
    except Exception as e:
        print(f"Error fetching price: {e}")
        return None
    
    finally:
        #to close the brwoser we opened
        driver.quit()
        print("Webdriver closed.")


# Load email/password from .env file
SENDER_EMAIL = os.getenv("EMAIL_USER")
SENDER_PASSWORD = os.getenv("EMAIL_PASS")
RECEIVER_EMAIL = os.getenv("EMAIL_USER")

#send mail to the reciever mail
def send_email(price):
    """ Sends email alert"""
    try:
        #connect gmail to smtp server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()

        server.login(SENDER_EMAIL, SENDER_PASSWORD)

        #create the mail
        subject = "Price rate reached"
        body = f"The price for item is now rupees {price}. Buy at {URL}"
        message = f"Subject: {subject}\n\n{body}"

        #send mail
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, message)
        print("Email sent successfully")

    except Exception as e:
        print(f"Failed to send email: {e}")

    finally:
        #disconnect server
        server.quit()

send_email(999)