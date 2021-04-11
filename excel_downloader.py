from selenium import webdriver
from PIL import Image
from io import BytesIO

import time

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=2568x1440')
options.add_argument("disable-gpu")
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
options.add_argument("lang=ko_KR")

driver = webdriver.Chrome(chrome_options=options)
driver.implicitly_wait(3)

driver.get('https://docs.google.com/spreadsheets/d/18tVw-UxH31rYf0f6YnHhaybSX1rCnjh4ddU7rJWours/edit#gid=1221634749')
time.sleep(5)

element = driver.find_element_by_xpath('//*[@id="1221634749-scrollable"]/div[2]')
png = element.screenshot('foo.png')