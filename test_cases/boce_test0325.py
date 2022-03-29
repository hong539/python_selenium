from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#These for wait until loader disapears
#LOADING_ELEMENT_CLASS = "mainMsg1b"
#wait this element disappear "mainMsg1b"

#检测节点数
result_nodes = "123456"
scan_nodes_xpath ="//p[@class='page04d6b re_detail_total']"

#平均響應
result_response = "999.999ms"
average_response_xpath ="/html[1]/body[1]/div[2]/div[5]/div[3]/div[2]/div[4]/p[1]"

#分享連結
share_url = "https://www.baidu.com/"
share_url_xpath = "//input[@id='shareVal']"

#PopoutSecondMsg
Pop = "//p[@class='mainMsg1b']"

#Setting webdriver path
#PATH will be changed with your webdriver.
PATH = Service(r"D:/Python_Projects/chromedriver_win32/chromedriver.exe") 
driver = webdriver.Chrome(service=PATH)

driver.maximize_window()
driver.delete_all_cookies()

driver.get("https://www.boce.com/dns/")



input = driver.find_element(By.NAME, "host")
input.click()
input.send_keys("baidu.com")
click = driver.find_element(By.CSS_SELECTOR, ".main02b2:nth-child(4)").click()


#sleep(30)


try:
    element = WebDriverWait(driver, 40).until(EC.invisibility_of_element((By.XPATH, scan_nodes_xpath)))
finally:
    result_nodes = driver.find_element(By.XPATH, scan_nodes_xpath).text
    print(result_nodes)


"""
result_nodes = driver.find_element(By.XPATH, scan_nodes_xpath).text
result_response = driver.find_element(By.XPATH, average_response_xpath).text
share_url = driver.find_element(By.XPATH, share_url_xpath).text

print(result_nodes)
print(result_response)
print(share_url)
"""
driver.quit()
    








