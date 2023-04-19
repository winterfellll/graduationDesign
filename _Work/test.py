from selenium import webdriver

driver = webdriver.Chrome()
driver.switch_to.new_window()
list1 = [2]
list2 = [2]

assert list1 != list2, '123'
