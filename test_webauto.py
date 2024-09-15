from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()

def test_bukaGoole():
    driver.get("https://www.google.com/")
    Title = driver.title

    assert Title == "Google"

def test_bukaFB():
    driver.get("https://id-id.facebook.com/")
    Title = driver.title

    assert Title == "Facebook - Masuk atau Daftar"    
