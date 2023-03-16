from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.debugger_address = '127.0.0.1:9223'
driver = webdriver.Chrome(options=options)

driver.get('http://www.baidu.com')
driver.find_element(By.ID, 'kw').send_keys('测试')
# driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[5]/div[2]/div/form/span[2]/input').click()
