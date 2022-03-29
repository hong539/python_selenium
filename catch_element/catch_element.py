from asyncio.windows_events import NULL
from unittest import result
from xml.dom.minidom import Element
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


domain_name = "123456"
domain_xpath = "//span[@class='rs_detail_host']"

#Setting webdriver path
#PATH will be changed with your webdriver.
PATH = Service(r"D:/Python_Projects/chromedriver_win32/chromedriver.exe") 
driver = webdriver.Chrome(service=PATH)

test_url = "https://www.boce.com/dns/m.heibai360.com/511b58b0e7ef970a7fbb46fe593af191.html"



driver.maximize_window()
driver.delete_all_cookies()

driver.get(test_url)

domain_name = driver.find_element(By.XPATH, domain_xpath)

#print(domain_name.get_attribute)

print(domain_name.text)

#print(domain_name)

#print(domain_name.tag_name)




driver.quit()





