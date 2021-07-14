#!/usr/bin/python3.6
from selenium import webdriver

options = webdriver.ChromeOptions()
#options.add_argument('headless')
options.add_argument('window-size=1920x1080')
driver = webdriver.Chrome("/home/lucky/tools/chromedriver_linux64/chromedriver", chrome_options=options)

url = 'https://scoreboard.ctf.saarland/'
scoreboard = driver.get(url)

teams_css = 'body > app-root > div > app-scoretable > table > tbody > tr > td.teamcell > div.media-body > h4'
ips_css = 'body > app-root > div > app-scoretable > table > tbody > tr > td.teamcell > div.media-body > span.team-vulnbox'


teams = driver.find_elements_by_css_selector(teams_css)
ips = driver.find_elements_by_css_selector(ips_css)

teams_list = []
ips_list = []

for team in teams:
    teams_list.append(team.text)

for ip in ips:
    ips_list.append(ip.text)

for i in range(0,205):
    print("'" + teams_list[i] + "'"  + ':' + "'"  + ips_list[i] + "',")
