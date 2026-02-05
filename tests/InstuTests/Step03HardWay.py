from collections.abc import KeysView
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import testData
import InstuUtils

# Driver oluştur
driver = webdriver.Chrome()
driver.maximize_window()
print("Driver oluşturuldu.")

try:
    # 1. Siteye git
    driver.get(testData.login_url)
    print("Siteye gidildi:", testData.login_url)
    
    # 2. Sayfanın yüklenmesini bekle
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )
    
    # 3. Login ol (Metot kullanarak)
    InstuUtils.InstuLearnLoginMethod(driver, testData.mail, testData.password)
    print("Login işlemi tamamlandı.")
    
   
   
    # buradaki adım step3in başına dahil edilmeyecek. 
    driver.get("https://qa.instulearn.com/panel/webinars/3638/step/3")
    
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )
    
    
    
    
    # ******step3baslangic*PRİCNG sTEPS **
    
    
    
    # SUBSCRIPTION BUTONU (Checkbox sorunu için özel çözüm)
    try:
        # Genellikle input yerine label'a tıklamak daha sağlıklıdır
        # Eğer input tıklanmıyorsa label'ı hedefliyoruz
        SUB_LABEL_XPATH = '//label[@for="subscribeSwitch"]'
        sub_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, SUB_LABEL_XPATH))
        )
        
        # Önce elemente odaklan (Scroll)
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", sub_button)
        time.sleep(1)
        
        # Border ekle (Nereyi tıkladığını gör)
        driver.execute_script("arguments[0].style.border='3px solid purple'", sub_button)
        
        # JavaScript ile tıklama (Standart click çalışmazsa diye en sağlamı budur)
        driver.execute_script("arguments[0].click();", sub_button)
        print("Subscription butonu (JS ile) başarıyla tıklandı.")
        
    except Exception as e:
        print(f"Subscription tıklanamadı, alternatif deneniyor: {e}")
        # Alternatif: Doğrudan input ID'sini kullan
        sub_input = driver.find_element(By.ID, "subscribeSwitch")
        driver.execute_script("arguments[0].click();", sub_input)    
    
    # period days box 
    PERIOD_DAYS_XPATH = '//input[@name="access_days"]'
    periodDaysBox = driver.find_element(By.XPATH, PERIOD_DAYS_XPATH)    
    driver.execute_script("arguments[0].style.border='3px solid green'", periodDaysBox)
    periodDaysBox.clear()
    periodDaysBox.send_keys("10")
    print("Period days box dolduruldu.")
    
    # pricebox
    PRICE_XPATH = '//input[@name="price"]'
    priceBox = driver.find_element(By.XPATH, PRICE_XPATH)
    driver.execute_script("arguments[0].style.border='3px solid red'", priceBox)
    priceBox.clear()
    priceBox.send_keys("0")
    print("Price box dolduruldu.")
    
    # nextButton
    NEXT_BUTTON_XPATH = '//button[@id="getNextStep"]'
    nextButton = driver.find_element(By.XPATH, NEXT_BUTTON_XPATH)
    driver.execute_script("arguments[0].style.border='3px solid yellow'", nextButton)
    nextButton.click()  
    
    
    
        # URL'in değişmesini bekle (Step 4'e geçiş)
    try:
        WebDriverWait(driver, 15).until(EC.url_contains("step/4"))
        current_url = driver.current_url
        
        if "step/4" in current_url:
            print("\n" + "="*50)
            print("🚀 STEP 3 BAŞARIYLA TAMAMLANDI!")
            print(f"📍 Mevcut Konum: {current_url}")
            print("✅ Fiyatlandırma ve Abonelik ayarları kaydedildi.")
            print("="*50 + "\n")
        else:
            print("⚠️ UYARI: URL değişti ama Step 4 doğrulanamadı.")
            
    except Exception as e:
        print("\n❌ HATA: Step 4'e geçiş başarısız oldu veya zaman aşımına uğradı!")
        print(f"Hata Detayı: {str(e)}\n")
        
        
   # step3 bitti 
   #[@Gemini ] step3 için method uretebilrimisin. InstuUtils altına koymak için. 
   # InstuUtils deki importlar 
   # from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import logging
import time
import InstuPages

# bu sayfadaki importlar     

    

    
    
    
    
    
    
    
    
finally:
    time.sleep(5)
    driver.quit()
    print("Tarayıcı kapatıldı.")