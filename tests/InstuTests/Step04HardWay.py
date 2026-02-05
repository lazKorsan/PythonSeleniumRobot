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
    
    # Step 4: New Section oluşturur ve bir sonraki adıma (Step 5) geçişi kutlar.
    # Not: Bu kod bloğu bir fonksiyon içinde olmadığı için 'return' ifadeleri kaldırılmıştır.
    
    print("\n" + "🚀" * 15)
    print("STEP 4: MACERA BAŞLIYOR...")
    print("🚀" * 15)
    
    try:
        # 1. 'New Section' Butonuna Tıkla
        new_section_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "js-add-chapter")]'))
        )
        new_section_btn.click()
        time.sleep(2) # Modal animasyonu için bekleme

        # 2. Title Box (Java'daki gibi 2. index)
        # HTML'de birden fazla aynı isimli input olduğu için [2] kritik!
        AJAX_BOX_XPATH = "(//input[@name='ajax[chapter][title]'])[2]"
        ajax_box = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, AJAX_BOX_XPATH))
        )
        
        # HighLight & Yazma (Java: slowSendKeys simülasyonu)
        driver.execute_script("arguments[0].style.border='3px solid red'", ajax_box)
        ajax_box.clear()
        for char in title_text:
            ajax_box.send_keys(char)
            time.sleep(0.05)
        print(f"✅ Bölüm başlığı '{title_text}' başarıyla girildi.")

        # 3. Save Butonu (Java: Force Click JS & Index [2])
        SEC_SAVE_BUTTON_XPATH = "(//button[contains(@class, 'save-chapter')])[2]"
        sec_save_button = driver.find_element(By.XPATH, SEC_SAVE_BUTTON_XPATH)

        # Actions: Hover (Java: moveToElement)
        ActionChains(driver).move_to_element(sec_save_button).perform()
        time.sleep(1)
        
        # JS Force Click
        driver.execute_script("arguments[0].style.border='3px solid yellow'", sec_save_button)
        driver.execute_script("arguments[0].click();", sec_save_button)
        print("✅ Save butonuna JavaScript ile 'ZORLA' basıldı!")

        # 4. Modalın Kapanışını Bekle
        WebDriverWait(driver, 15).until(EC.invisibility_of_element_located((By.CLASS_NAME, "swal2-container")))
        
        # 5. Büyük Final: Next Step ve Kutlama
        next_button = driver.find_element(By.ID, "getNextStep")
        driver.execute_script("arguments[0].style.border='5px solid gold'", next_button)
        next_button.click()

        # Step 5'e geçiş doğrulaması
        WebDriverWait(driver, 15).until(EC.url_contains("step/5"))
        
        # --- GÖVDE GÖSTERİSİ BÖLÜMÜ ---
        print("\n" + "⭐" * 50)
        print("🏆 ZAFER! STEP 4 CANAVARI ETKİSİZ HALE GETİRİLDİ!")
        print(f"🔗 YENİ KONUM: {driver.current_url}")
        print("📝 İŞLEM: Dinamik Modal aşıldı ve New Section başarıyla eklendi.")
        print("🔥 SONUÇ: Step 5 (Media/Video) kapıları sonuna kadar açıldı!")
        print("⭐" * 50 + "\n")

    except Exception as e:
        print(f"\n❌ MAALESEF BİR ENGELLE KARŞILAŞTIK: {e}")

    # InstuUtils içindeki metodu çağır
    InstuUtils.complete_step4_section(driver, title_text="Yeni Bölüm Başlığı")

except Exception as e:
    print(f"Bir hata oluştu: {e}")
    
    
finally:
    time.sleep(5)
    driver.quit()
    print("Tarayıcı kapatıldı.")