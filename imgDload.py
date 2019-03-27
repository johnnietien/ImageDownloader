from selenium import webdriver

import pandas as pd
import urllib.request as urllib2
import os

default_dir = "/Users/ashwin/Desktop/images/imgsnew"

df = pd.read_csv(r'/Users/ashwin/Desktop/images/picsnew.csv')
os.chdir(default_dir)

titles = df['titles']
links = df['links']

options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", {
  "download.default_directory": default_dir,
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": True
})

driver = webdriver.Chrome("/Users/ashwin/Downloads/chromedriver", options=options)

for idx, event in enumerate(links):
    driver.get(event)

    image_path = driver.find_element_by_xpath('//img')
    src = image_path.get_attribute('src')

    # download the image
    urllib2.urlretrieve(src, titles[idx] + ".jpg")

driver.close()


