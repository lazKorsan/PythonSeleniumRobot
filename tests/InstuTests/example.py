from selenium import webdriver
import testData
import InstuUtils
import InstuPages  

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

import InstuUtils 

# Driver oluştur
driver = webdriver.Chrome()
driver.maximize_window()

try:
    # 1. Siteye git
    driver.get("https://qa.instulearn.com/login")
    print("Siteye gidildi")
    
    # 2. Sayfanın yüklenmesini bekle
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )
    
    # 3. Login ol
    InstuUtils.InstuLearnLoginMethod(driver, testData.mail, testData.password)
    print("Login yapıldı")
    
    # 4. Page object oluştur
    instu_pages = InstuPages.InstuPages(driver)  
    print("Page object oluşturuldu")
    
    # 5. Courses butonuna tıkla (METHOD'u çağır!)
    instu_pages.click_coursesButton()
    print("Courses butonuna tıklandı")
    
    # 6. Bekle ve kontrol et
    time.sleep(13)
    
    # 7. URL kontrolü yap
    current_url = driver.current_url
    print(f"Şu anki URL: {current_url}")
    
    if "courses" in current_url:
        print("✅ BAŞARILI: Courses sayfasına gidildi!")
    else:
        print("❌ HATA: Courses sayfasına gidilemedi!")
        
        
        
finally:
    # 8. Tarayıcıyı kapat (hata olsa da kapanır)
    time.sleep(5)
    driver.quit()
    print("Tarayıcı kapatıldı")