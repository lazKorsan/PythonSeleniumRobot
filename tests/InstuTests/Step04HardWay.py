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
    
    # buradaki adım step4nin başına dahil edilmeyecek. 
    driver.get("https://qa.instulearn.com/panel/webinars/3638/step/4")
    
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )
    
    title_text="Yeni Bölüm Başlığı"
    
    def complete_step4_section(driver, title_text="Yeni Bölüm Başlığı"):
        print("\n--- Step 4: Bölüm Oluşturma İşlemi Başladı ---")
        try:
            # 1. 'New Section' Butonuna Tıkla
            new_section_btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "js-add-chapter")]'))
            )
            new_section_btn.click()
            time.sleep(2) # Modalın animasyonu için bekleme

            # 2. Title Box (Java'daki gibi 2. index)
            AJAX_BOX_XPATH = "(//input[@name='ajax[chapter][title]'])[2]"
            ajax_box = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, AJAX_BOX_XPATH))
            )
            
            # HighLight & Slow Send Keys
            driver.execute_script("arguments[0].style.border='3px solid red'", ajax_box)
            ajax_box.clear()
            for char in title_text:
                ajax_box.send_keys(char)
                time.sleep(0.1)
            print(f"✅ Başlık girildi: {title_text}")

            # 3. Save Butonu (Java'daki [2] index ve forceClickWithJS mantığı)
            # Sınıf isimlerini Java'daki gibi tam eşleşme veya contains ile alıyoruz
            SEC_SAVE_BUTTON_XPATH = "(//button[contains(@class, 'save-chapter')])[2]"
            sec_save_button = driver.find_element(By.XPATH, SEC_SAVE_BUTTON_XPATH)

            # Actions: MoveToElement (Java'daki hover işlemi)
            actions = ActionChains(driver)
            actions.move_to_element(sec_save_button).perform()
            time.sleep(1) # Hover sonrası kısa stabilizasyon
            
            # JavaScript ile Force Click (Java'daki ClickUtils.forceClickWithJS)
            driver.execute_script("arguments[0].style.border='3px solid yellow'", sec_save_button)
            driver.execute_script("arguments[0].click();", sec_save_button)
            print("✅ Save butonuna JS ile zorlanarak tıklandı.")

            # 4. Modalın kapanmasını bekle (Java'daki uzun bekleme yerine dinamik kontrol)
            WebDriverWait(driver, 15).until(EC.invisibility_of_element_located((By.CLASS_NAME, "swal2-container")))
            print("⭐ Bölüm başarıyla kaydedildi.")
            
            return True
        except Exception as e:
            print(f"❌ Step 4 Save İşleminde Hata: {e}")
            return False
        
        
        
        
        

    # Metodu çağır
    complete_step4_section(driver, title_text="Yeni Bölüm Başlığı")

except Exception as e:
    print(f"Bir hata oluştu: {e}")
    
    InstuUtils.step2(driver, capacity="60", duration="90", tags="test", category_value="956")
finally:
    time.sleep(5)
    driver.quit()
    print("Tarayıcı kapatıldı.")