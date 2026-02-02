from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome();

driver.get("https://qa.loyalfriendcare.com/en");

xpath_degeri = '//*[@id="top_menu"]/li[1]/a';
element = driver.find_element(By.XPATH, xpath_degeri);
    
    # Elemente tıkla
element.click();

time.sleep(2) ;

# Email'i yaz, TAB'a bas, şifreyi yaz ve ENTER'a bas
actions = ActionChains(driver)
actions.send_keys("lazKorsan20220262058@gmail.com") \
       .send_keys(Keys.TAB) \
       .send_keys("Query.2026") \
       .send_keys(Keys.ENTER) \
       .perform() ;
       
time.sleep(2) ;

# 1. Hazırlık
expectedUserName = "lazKorsan"
xpath_degeri = "//a[@class='btn_add']"

try:
    element = driver.find_element(By.XPATH, xpath_degeri)
    
    # İkonu ve boşlukları ayıklıyoruz
    gercek_isim = element.text.strip()

    print("\n--- İKON AYIKLAMA VE TEST ŞİİRİ ---")
    print(f"Yanında bir çark vardı, dönüyordu durmadan,")
    print(f"İsmi aldık oradan, ikona hiç vurmadan.")
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

# driver.quit() # Tarayıcıyı kapatmak istersen açabilirsin

