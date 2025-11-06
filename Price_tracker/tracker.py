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

#configuration
URL="https://www.amazon.in/Sony-ILCE-7M3K-Full-Frame-Mirrorless-Interchangeable/dp/B07DPSQRFF/?_encoding=UTF8&ref_=pd_hp_d_atf_ci_mcx_mr_ca_hp_atf_d"
TARGET_PRICE=130000.0
PRICE_SELECTOR_XPATH="/html/body/div[1]/div[1]/div/div[5]/div[4]/div[15]/div/div/div[4]/div[1]/span[3]/span[2]/span[2]"