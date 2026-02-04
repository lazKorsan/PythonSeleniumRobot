from collections.abc import KeysView
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
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
    
   
   
    # buradaki adım step2nin başına dahil edilmeyecek. 
    driver.get("https://qa.instulearn.com/panel/webinars/3638/step/2")
    
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )
    
    
    
    
     # ******step2 baslangic****************
     
     # CAPACİTY BOX DOLDURMA
    CAPACİTY_XPATH = '//input[@name="capacity"]'
    capacityBox = driver.find_element(By.XPATH, CAPACİTY_XPATH)
    driver.execute_script("arguments[0].style.border='3px solid green'", capacityBox)
    capacityBox.clear()
    capacityBox.send_keys("50")
    print("Capacity box dolduruldu.") 
    
    time.sleep(200)
    
   
    
    # duration box doldurma
    # Duration box için güncellenmiş kod
    try:
        # Önce sayfanın tamamen yüklendiğinden emin ol
        time.sleep(1)
        
        # Elementi bul
        DURATION_XPATH = '//input[@name="duration"]'
        durationBox = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, DURATION_XPATH))
        )
        
        # Elementi görünür hale getir
        driver.execute_script("arguments[0].scrollIntoView(true);", durationBox)
        time.sleep(0.5)
        
        # Border ekle (debug için)
        driver.execute_script("arguments[0].style.border='3px solid red'", durationBox)
        
        # Element durumunu kontrol et
        print(f"Element enabled: {durationBox.is_enabled()}")
        print(f"Element displayed: {durationBox.is_displayed()}")
        
        # Eğer tıklanamıyorsa JavaScript ile tıkla
        try:
            durationBox.click()
        except:
            driver.execute_script("arguments[0].click();", durationBox)
        
        # Clear ve send_keys dene
        durationBox.clear()
        time.sleep(0.3)
        durationBox.send_keys("45")
        
        # Değeri kontrol et
        girilen_deger = durationBox.get_attribute('value')
        print(f"Girilen değer: '{girilen_deger}'")
        
        # Eğer hala boşsa JavaScript ile doldur
        if not girilen_deger:
            driver.execute_script("arguments[0].value = '45';", durationBox)
            driver.execute_script("""
                arguments[0].dispatchEvent(new Event('input', { bubbles: true }));
                arguments[0].dispatchEvent(new Event('change', { bubbles: true }));
            """, durationBox)
            
    except Exception as e:
        print(f"Hata oluştu: {str(e)}")
        
        # Alternatif yaklaşım
        try:
            # Doğrudan JavaScript ile
            driver.execute_script("""
                document.querySelector('input[name="duration"]').value = '45';
                document.querySelector('input[name="duration"]').dispatchEvent(new Event('input'));
                document.querySelector('input[name="duration"]').dispatchEvent(new Event('change'));
            """)
        except:
            print("Alternatif yöntem de çalışmadı")

finally:
    time.sleep(5)
    driver.quit()
    print("Tarayıcı kapatıldı.")
          
     

   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
