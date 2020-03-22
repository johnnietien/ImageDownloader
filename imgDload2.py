from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from pandas import DataFrame
import urllib.request as urllib2
import os, time

default_dir = "./imgsnew2"
df = pd.read_csv(r'testlinkcsv.csv')
#df = pd.read_csv(r'testlinkcsv5.csv', nrows=3)
#df = df.head(3)
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

#driver = webdriver.Chrome("D:\Admin\Projects2020\ImageDownloader\chromedriver_win32\chromedriver.exe", options=options)
driver = webdriver.Chrome("/usr/bin/chromedriver", options=options)
#driver.maximize_window()
driver.implicitly_wait(10) # seconds

for idx, event in enumerate(links):
    driver.get(event)
    productTitle = driver.find_element_by_xpath('//*[@id="productTitle"]')
    print(productTitle.text)
    #df['titles'] = productTitle.text
    #print(df['titles'])
    titles[idx] = productTitle.text
    #print(titles[idx])
    #df.iloc[idx,0] = productTitle.text
    #image_path = driver.find_element_by_xpath('//*[@id="imageBlock"]/div/div/div[2]')
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="main-image-container"]')))
    print('da doi xong')

    actions = ActionChains(driver)
    #actions.move_to_element(element)
    actions.context_click(element).perform()
    #actions.perform()
    #element.click()
    print('da click xong')

    wait = WebDriverWait(driver, 20)
    image_path = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="landingImage"]')))
    src = image_path.get_attribute('data-old-hires')
    #print(image_path)
    print(src)
    src1 = src.rpartition("%7C0%2C0%")[0]
    src2 = src1.split("._AC_CLa%7C2140%2C2000%7C")
    src3 = src2[0] + ".png"
    src4 = src3.rpartition("/images/I/")
    src5 = src4[0] + src4[1] + src2[1]
    print(src3)
    print(src5)
    # download the image //*[@id="main-image-container"]/ul/li[3]/span/span/div/img
    # //*[@id="ask-dp-search_feature_div"]/div/div/div/div/form/span/span/span/span/span/span/div/span/div/div/div/input
    # urllib2.urlretrieve(src, titles[idx] + ".jpg")
    #urllib2.urlretrieve(src, productTitle.text + ".png")
    #driver.close()
    urllib2.urlretrieve(src, productTitle.text + ".png")
    urllib2.urlretrieve(src3, productTitle.text + "-mockup.png")
    urllib2.urlretrieve(src5, productTitle.text + "-design.png")

df['titles'] = titles
print(df['titles'])
df1 = DataFrame(df, columns= ['titles', 'links'])
export_csv = df1.to_csv(r'testlinkcsv5.csv', index = None, header=True)
driver.close()


