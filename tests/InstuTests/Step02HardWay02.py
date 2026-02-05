from collections.abc import KeysView
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import InstuPages
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
    
    # Bekleme süresi düşürüldü (200 sn -> 2 sn)
    time.sleep(2)  
   
    
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
            
            
    # supporRadioBox
    SUPPORT_RADIO_XPATH = '(//*[@class="custom-control custom-switch"])[1]'
    supportRadioBox = driver.find_element(By.XPATH, SUPPORT_RADIO_XPATH)
    driver.execute_script("arguments[0].style.border='3px solid blue'", supportRadioBox)
    supportRadioBox.click()
    print("Support seçeneği işaretlendi ve border eklendi.")
    
    # sertifika seçeneği eklendi
    CERTIFICATE_RADIO_XPATH = '(//*[@class="custom-control custom-switch"])[2]'
    certificateRadioBox = driver.find_element(By.XPATH, CERTIFICATE_RADIO_XPATH)    
    driver.execute_script("arguments[0].style.border='3px solid orange'", certificateRadioBox)
    certificateRadioBox.click()
    print("Sertifika seçeneği işaretlendi ve border eklendi.")
    
    # downloadable option seçeneği eklendi
    DOWNLOADABLE_RADIO_XPATH = '(//*[@class="custom-control custom-switch"])[3]'
    downloadableRadioBox = driver.find_element(By.XPATH, DOWNLOADABLE_RADIO_XPATH)          
    driver.execute_script("arguments[0].style.border='3px solid pink'", downloadableRadioBox)
    downloadableRadioBox.click()
    print("Downloadable seçeneği işaretlendi ve border eklendi.")
    
    # tags box bilgisini doldurma
    TAGS_XPATH = '//input[@placeholder="Type tag name and press enter (Max : 5)"]'
    tagsBox = driver.find_element(By.XPATH, TAGS_XPATH)
    driver.execute_script("arguments[0].style.border='3px solid purple'", tagsBox)
    tagsBox.send_keys("math")    
    print("Tags box dolduruldu.")
    
    # select catogoryies
    CATEGORY_DROPDOWN_XPATH = '//select[@id="categories"]'
    categoryDropdown = driver.find_element(By.XPATH, CATEGORY_DROPDOWN_XPATH)
    driver.execute_script("arguments[0].style.border='3px solid brown'", categoryDropdown)
    categoryDropdown.click()
    print("Category dropdown açıldı.")
    
    
    # Doğrudan Math seçeneğinin XPATH'ini hedefle
    MATH_OPTION_XPATH = '//select[@id="categories"]//option[@value="956"]'
    mathOption = driver.find_element(By.XPATH, MATH_OPTION_XPATH)
    driver.execute_script("arguments[0].style.border='3px solid green'", mathOption)
    mathOption.click()
    categoryDropdown.click()  # Dropdown'u kapatmak için tekrar tıkla
    print("Math seçeneği seçildi ve border eklendi.")
    
    # nextstep button
    NEXT_STEP_BUTTON_XPATH = '//button[@id="getNextStep"]'
    nextStepButton = driver.find_element(By.XPATH, NEXT_STEP_BUTTON_XPATH)
    driver.execute_script("arguments[0].style.border='3px solid yellow'", nextStepButton)
    nextStepButton.click()
    print("Next step butonuna tıklandı.")
    
    
    
    
    
    # succes mesaj 
    WebDriverWait(driver, 10).until(EC.url_contains("step/3"))
    # 2. Mevcut URL'i al
    current_url = driver.current_url
    print(f"Mevcut URL: {current_url}")

    # 3. Mantıksal karşılaştırma (URL içinde 'step/3' geçiyor mu?)
    if "step/3" in current_url:
        print("------------------------------------------")
        print("BAŞARILI: Step 2 başarıyla geçildi, şu an Step 3'tesiniz.")
        print("------------------------------------------")
    else:
        print("HATA: Step 3'e geçilemedi!")
    
    # ******step2 bitiş****************
    
        

finally:
    time.sleep(5)
    driver.quit()
    print("Tarayıcı kapatıldı.")
