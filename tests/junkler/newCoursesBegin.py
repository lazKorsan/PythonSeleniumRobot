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
    
    #[@Gemini]  
    # burada yeni kurs oluşturma işlemleri başlıyor 
    # buradaki 4ncu adım dahil  else blogununun sonuna kadar olan kısmı 
    # şu sayfanın içinde C:\Users\user\Desktop\python_planet2\tests\InstuTests\InstuUtils.py 
    # bir method olarak tanımlayabilirmiyiz. 
    # bu sayfada bir birne bağlı 2 method var. 
    # daha sonra şu test sınıfında   C:\Users\user\Desktop\python_planet2\tests\InstuTests\beginCreateCourse.py 
    # çağıracak minumum satırlı bir test sınıfı oluşturabilirmiyiz. 
    #[@ Gemini soru bu iki si arasıdna ]
    
    
    # 4. Page object oluştur
    instu_pages = InstuPages.InstuPages(driver)
    
    # 5. Courses butonuna tıkla (METHOD'u çağır!)
    instu_pages.click_coursesButton()
    
    # 6. Bekle ve kontrol et
    time.sleep(2)
    
    # 7. Panel sayfasına gidildiğini doğrula ve ardından 'New Webinar' butonuna tıkla
    panel_url = driver.current_url
    print(f"Mevcut URL: {panel_url}")
    
    # URL'in 'panel' içerdiğini kontrol et
    if "panel" in panel_url:
        print("✅ BAŞARILI: Panel sayfasına gidildi!")

        # 8. New Webinar butonuna tıkla (Page Object Model kullanarak)
        instu_pages.click_new_webinar_button()
        
        # 9. Yeni sayfanın yüklenmesini bekle ve URL'i kontrol et
        try:
            WebDriverWait(driver, 10).until(EC.url_contains("webinars/new"))
            new_page_url = driver.current_url
            print(f"Yeni Sayfa URL: {new_page_url}")
            print("✅ BAŞARILI: New Webinar sayfasına başarıyla gidildi!")
        except:
            print("❌ HATA: New Webinar sayfasına gidilemedi veya URL 'webinars/new' içermiyor.")

    else:
        print("❌ HATA: Panel sayfasına gidilemedi! (URL 'panel' içermiyor)")
        
        
        
finally:   
    time.sleep(15)
    driver.quit()
    print("Tarayıcı kapatıldı")



    



    
    
    
    
    
    