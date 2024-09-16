from selenium import webdriver
import pytest

driver = webdriver.Chrome()
driver.maximize_window()

# fungsi parameterize
# Buat tupel variabel alamat yg berisi list 
Alamat = [
    ("https://www.google.com","Google"),
    ("https://id-id.facebook.com","Facebook - Masuk atau Daftar")
]

# ADDRESS = Var Alamat | RESULT = MEMASTIKAN POIN APA YG DI VALIDASI
# BUAT DECORATOR

@pytest.mark.parametrize('address,result',Alamat)
                         
def test_bukaAlamat(address,result):
    driver.get(address)
    Title = driver.title

    assert Title == result   
