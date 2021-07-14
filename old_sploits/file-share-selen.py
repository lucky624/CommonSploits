#!/usr/bin/python3.6
from selenium import webdriver
import sys, re, requests
import string, random, uuid
from selenium import webdriver
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By




options = webdriver.ChromeOptions()
#options.add_argument('headless')
options.add_argument('window-size=1920x1080')
driver = webdriver.Chrome("/home/lucky/Downloads/chromedriver_linux64/chromedriver", chrome_options=options)


def generator(size=12, chars= string.ascii_lowercase ):
    return ''.join(random.choice(chars) for _ in range(size))

def generator_pass(size=22, chars=string.digits + string.ascii_uppercase + string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))

url = 'http://10.1.59.1:8001/'
driver.get(url)

driver.get('http://10.1.59.1:8001/authentication/register')

email_css = '#Input_Email'
pass_css = '#Input_Password'
pass_сonnfirm_css = '#Input_ConfirmPassword'
submit_css = '#registerSubmit'

email = generator() + '@test.de'
password = generator_pass() + '$'

timeout = 10

try:
    element_present = EC.presence_of_element_located((By.CSS_SELECTOR, submit_css))
    WebDriverWait(driver, timeout).until(element_present)
except TimeoutException:
    print("Timed out waiting for page to load")
finally:
    print("Page loaded")

email_input = driver.find_element_by_css_selector(email_css)
pass_input = driver.find_element_by_css_selector(pass_css)
pass_confirm_input = driver.find_element_by_css_selector(pass_сonnfirm_css)
submit_input = driver.find_element_by_css_selector(submit_css)

email_input.send_keys(email)
pass_input.send_keys(password)
pass_confirm_input.send_keys(password)
submit_input.click()

driver.get(url + '')