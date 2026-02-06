from collections.abc import KeysView
from winreg import KEY_ENUMERATE_SUB_KEYS
from selenium.webdriver.common.keys import Keys
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
    
   
   
    # buradaki adım step5in başına dahil edilmeyecek. 
    driver.get("https://qa.instulearn.com/panel/webinars/3645/step/5")
    
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )
    
    
    
    
    # ******step5baslangic*new prerequest  **
    
    def complete_step5_prerequisites(driver, search_text="SDET"):
        print("\n" + "🛡️" * 15)
        print("STEP 5: PREREQUISITES GÖREVİ BAŞLADI")
        print("🛡️" * 15)
        
        try:
            # 1. New Prerequisite Butonuna Tıkla
            new_pre_btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "webinarAddPrerequisites"))
            )
            new_pre_btn.click()
            time.sleep(1)

            # 2. Container'ı aç (Java'daki select2-container mantığı)
            container = driver.find_element(By.CLASS_NAME, "select2-selection__placeholder")
            driver.execute_script("arguments[0].style.border='3px solid red'", container)
            container.click()
            print("✅ Select2 container açıldı.")

            # 3. Arama Kutusuna Yaz (Dinamik input)
            search_field = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "select2-search__field"))
            )
            search_field.send_keys(search_text)
            time.sleep(2) # Sonuçların listelenmesi için bekleme

            # 4. Ofset Tıklama (30 Piksel Aşağı)
            print(f"🎯 '{search_text}' için 30 piksel altına tıklanıyor...")
            actions = ActionChains(driver)
            actions.move_to_element(search_field).move_by_offset(0, 30).click().perform()
            
            # 5. Save İşlemi
            save_btn = driver.find_element(By.CLASS_NAME, "js-save-prerequisite")
            driver.execute_script("arguments[0].style.border='3px solid orange'", save_btn)
            save_btn.click()
            
            # 6. getNextButton 
            time.sleep(3)
            next_btn = driver.find_element(By.ID, "getNextStep")
            driver.execute_script("arguments[0].style.border='3px solid green'", next_btn)
            next_btn.click()
            

            print("\n" + "🎊" * 20)
            print("KAZANDIK! Step 5 Prerequisites başarıyla kaydedildi!")
            print("🎊" * 20 + "\n")
            return True
        except Exception as e:
            print(f"❌ Step 5'te bir engel çıktı: {e}")
            return False

    complete_step5_prerequisites(driver)
    
    
    

    
    
    

    

    
    
    
    
    
    
    
    
finally:
    time.sleep(5)
    driver.quit()
    print("Tarayıcı kapatıldı.")