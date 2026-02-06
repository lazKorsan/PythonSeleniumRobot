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
    
      # buradaki adım step4nin başına dahil edilmeyecek. 
    driver.get("https://qa.instulearn.com/panel/webinars/3638/step/4")
    
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )
    
    InstuUtils.step4(driver, title_text="Yeni Bölüm Başlığı")
    
except Exception as e:
    print(f"Bir hata oluştu: {e}")
finally:   
    time.sleep(5)
    driver.quit()
    print("Tarayıcı kapatıldı.")