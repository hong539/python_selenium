from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from PIL import Image

#PATH will be changed with your webdriver.
PATH = Service(r"D:/Python_Projects/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=PATH)

driver.get('https://www.boce.com/dns')
print(driver.title)

pic_name = print(driver.title)

driver.find_element(By.NAME, "host").click()
driver.find_element(By.NAME, "host").send_keys("www.hbzb666.com")
driver.find_element(By.CSS_SELECTOR, ".main02b2:nth-child(4)").click()

driver.set_window_size(1936, 1056)



charts = driver.find_element(By.CSS_SELECTOR, ".rs_chart")

WebDriverWait(driver, 30).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".rs_chart")))

charts.screenshot('foo.png')




