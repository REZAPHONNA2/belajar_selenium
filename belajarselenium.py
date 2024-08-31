from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
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

"""COMMENT
#MENGGUNAKAN FUNGSI HANDLING ALERT (ACCEPT POP UP)
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://demoqa.com/alerts")
time.sleep(2)
#Input text yg muncul di pop up dengan 
driver.find_element(By.ID,"alertButton").click()
time.sleep(2)
#FUNGSI UNTUK Menambahkan input pop up
#driver.switch_to.alert.send_keys("Saya sedang testing")

#Apabila ingin batal/cancel pop pakai "dismiss"
driver.switch_to.alert.accept()"""

"""COMMENT (Implicitly_wait)
options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
#Menggunakan Charles Proxy untuk setting kecepatan internet
driver = webdriver.Chrome(options=options)
driver.maximize_window()
#Waktu menunggu proses untuk ke element berikutnya
driver.implicitly_wait(10)
driver.get("https://demoqa.com/login")
driver.get("https://demoqa.com/books")
driver.find_element(By.ID, "login").click()
"""

"""COMMENT (Explicitly wait)
options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()
# driver = webdriver.Chrome()

driver.get('https://demoqa.com/alerts')
driver.find_element(By.ID, "timerAlertButton").click()

try:
    WebDriverWait(driver,10).until(EC.alert_is_present())
    driver.switch_to.alert.accept()
    print("alert di pencet")

except TimeoutException:
    print("Alert tidak muncul")
    pass
"""

""" COMMENT (Fitur Handling pop up / Modal /Iklan)
options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=options)
#driver.maximize_window()
for i in range(2): # UNTUK PROSES LOOP WEB BROWSER 
    driver.get("https://tees.co.id/")

try:
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]')))
    print("Pop Up Muncul")
    driver.find_element(By.CLASS_NAME, "btn-modal-close").click()
    print("Pop Up di CLose")

except TimeoutException:
    print("Pop up tidak Muncul")
    pass    
time.sleep(3)
"""
