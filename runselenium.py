from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.implicitly_wait(10)
from time import sleep

driver.get('https://www.jotform.com/')
driver.find_element(By.XPATH,'//a[@data-name="login]').click()
driver.find_element(By.XPATH,'//button[@aria-lebel="Login With Google"]').click()
driver.switch_to.window(driver.window.handles[1])
driver.find_element(By.ID,'identifierId').send_keys('uno')
