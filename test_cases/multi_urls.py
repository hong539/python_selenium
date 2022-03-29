from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(executable_path=r"D:/Python_Projects/chromedriver_win32/chromedriver.exe")


driver.maximize_window()
driver.delete_all_cookies()

urls = ["https://www.boce.com/dns/m.heibai360.com",
        "https://www.boce.com/dns/hbzb666.com",
        "https://www.boce.com/dns/heibai688.com",
        "https://www.boce.com/dns/hbzb999.com",
        "https://www.boce.com/dns/heibaikankan.com",
        "https://www.boce.com/dns/heibai999.com",
        "https://www.boce.com/dns/myeogm.com",
        "https://www.boce.com/dns/13cskppe.com",
        "https://www.boce.com/dns/xilufund.com",
        "https://www.boce.com/dns/cqlwny.com",
        "https://www.boce.com/dns/xtuike.com",
        "https://www.boce.com/dns/imiaoge.com",
        "https://www.boce.com/dns/lfctc.com"]
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