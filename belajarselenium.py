from selenium import webdriver
from selenium.webdriver.common.by import By
import time

""" (COMMENT) 
options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/windows")
time.sleep(2)
#Menambahkan fungsi button click ke new tab
driver.find_element("link text", "Click Here").click()
time.sleep(2)
fungsi tambah new tab 0=1
driver.switch_to_window(driver.window_handles[0])
"""

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://demoqa.com/alerts")
time.sleep(2)
driver.find_element(By.ID,"alertButton").click()
time.sleep(2)
driver.switch_to.alert.accept()