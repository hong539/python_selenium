from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#get_url
get_url = "put_your_link" 

#text_area
text_area_xpath = "put_your_text_area_xpath"

list_urls = ["google.com\n", "youtube.com\n", "facebook.com\n"]

#Setting webdriver path
#PATH will be changed with your webdriver.
PATH = Service(r"D:/Python_Projects/chromedriver_win32/chromedriver.exe") 
driver = webdriver.Chrome(service=PATH)

driver.maximize_window()
driver.delete_all_cookies()

driver.get(get_url)

driver.find_element(By.XPATH, text_area_xpath).send_keys(list_urls)

#sleep(10)