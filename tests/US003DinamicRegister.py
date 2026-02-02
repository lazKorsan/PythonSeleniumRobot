


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time 

driver = webdriver.Chrome();

driver.get("https://qa.loyalfriendcare.com/en");

xpath_degeri = '(//*[@class="btn_add"])[2]'

signInButton = driver.find_element(By.XPATH, xpath_degeri);
signInButton.click();
time.sleep(2) ;

userNmameInputXpath = '//input[@id="name"]'
userNmameInput = driver.find_element(By.XPATH, userNmameInputXpath);
userNmameInput.send_keys("lazKorsan");

time.sleep(2) ;
    
emailInputXpath = '//input[@id="email"]'
emailInput = driver.find_element(By.XPATH, emailInputXpath);

email = "lazKorsan" + str(int(time.time())) + "@gmail.com";

emailInput.send_keys(email);

time.sleep(2) ;

passwordInputXpath = '//input[@id="password"]'
passwordInput = driver.find_element(By.XPATH, passwordInputXpath);
passwordInput.send_keys("Query.2026");

comfirmPasswordInputXpath = '//input[@id="password-confirm"]'
comfirmPasswordInput = driver.find_element(By.XPATH, comfirmPasswordInputXpath);
comfirmPasswordInput.send_keys("Query.2026");

time.sleep(2) ;


signUpButtonXpath = '//button[@class="btn btn-primary btn-cons m-t-10"]'
signUpButton = driver.find_element(By.XPATH, signUpButtonXpath);
signUpButton.click();

time.sleep(2) ;

# 1. Hazırlık
expectedUserName = "lazKorsan"
xpath_degeri = "//a[@class='btn_add']"

try:
    element = driver.find_element(By.XPATH, xpath_degeri)
    
    # İkonu ve boşlukları ayıklıyoruz
    gercek_isim = element.text.strip()

    print("\n--- İKON AYIKLAMA KISMI ---")
    
    print(f"Aranan kahraman: {expectedUserName}")
    print(f"Bulunan cengaver: {gercek_isim}")

    if gercek_isim == expectedUserName:
        print("\nAyarlar çarkı döndü, isim doğru takıldı,")
        print("Testin meşalesi, gururla yakıldı! ✅")
    else:
        print("\nEyvah! Çarklar karıştı, isimler uymadı,")
        print("Sistem bu hatayı, asla duymadı... ❌")

except Exception as e:
    print("Hata çıktı hocam:", e)


driver.quit();

# driver.quit() # Tarayıcıyı kapatmak istersen açabilirsin


