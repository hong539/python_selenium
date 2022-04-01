from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(executable_path=r"webdriver_loaction_path/chromedriver.exe")


driver.maximize_window()
driver.delete_all_cookies()

urls = [

        ]

for posts in range(len(urls)):
    print(posts)
    driver.get(urls[posts])    
    if(posts!=len(urls)-1):
       driver.execute_script("window.open('');")
       chwd = driver.window_handles
       driver.switch_to.window(chwd[-1])

# you can move to specific handle    
chwd = driver.window_handles
print(chwd)
