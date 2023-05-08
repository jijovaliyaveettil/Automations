from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pandas as pd
#Import files to make an executable file
from datetime import datetime
import os
import sys

app_path = os.path.dirname(sys.executable)

now = datetime.now()
#MMDDYYYY
M_D_Y = now.strftime("%m%d%Y")

website = 'https://indianexpress.com/section/sports/'
path = '/Users/jijovaliyaveettil/Downloads/chromedriver_mac_arm64'


options = Options()
options.headless = True

# Instantiate service and driver objects
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service, options=options)

driver.get(website)

# Get the first title
title = driver.find_element(by="xpath", value = '//div[@class="articles first"]/h2').text
subtitle = driver.find_element(by="xpath", value = '//div[@class="articles first"]/p').text
link = driver.find_element(by="xpath", value = '//div[@class="articles first"]/h2/a').get_attribute("href")

containers = driver.find_elements(by="xpath", value = '//div[@class="articles "]')

# Empty lists to store the data
titles = []
subtitles = []
links = []

# Get the rest of the titles
for container in containers:
    titles.append(title)
    subtitles.append(subtitle)
    links.append(link)
    title = container.find_element(by="xpath", value = './h2').text
    subtitle = container.find_element(by="xpath", value = './p').text
    link = container.find_element(by="xpath", value = './h2/a').get_attribute("href")
    

Dict = {'titles': titles, 'subtitles': subtitles, 'links': links}

df_headlines = pd.DataFrame(Dict)

# filename = f'{app_path}/sports-headline_{M_D_Y}.csv' Since different OS uses different / we use the following join
filename = f'sports-headline_{M_D_Y}.csv'

df_headlines.to_csv(os.path.join(app_path,filename), index=False)

# df_saved_file = pd.read_csv('headline-headless.csv')
# print(df_saved_file)
driver.quit()





