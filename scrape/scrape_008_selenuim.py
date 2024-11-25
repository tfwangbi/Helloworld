from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

url = 'https://www.baidu.com'

# service = Service(executable_path='webdrivers/chromedriver.exe')
driver = webdriver.Chrome()
driver.get(url)

print(driver.title)

# driver.save_screenshot("../../download/image_002/baidu1.png")
# print(driver.page_source)
time.sleep(1)
kw = driver.find_elements(By.ID, 'kw')[0]
kw.send_keys("selenium")
time.sleep(1)
submit = driver.find_elements(By.ID, 'su')[0]
# submit = driver.find_element_by_id('su')
submit.click()

time.sleep(2)

driver.save_screenshot('../../download/image_002/selenium_baidu.png')
driver.quit()