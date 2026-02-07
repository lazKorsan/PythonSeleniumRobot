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
    driver.get("https://qa.instulearn.com/panel/webinars/3649/step/6")
    
    InstuUtils.step6(driver, faq_question="Ogretmenler ile gorusme sıklıgı", faq_answer="Ogrencilerimiz 2 haftada 1 15 dk zoom gorusmesi yapabilirler")
    
finally:   
    time.sleep(5)
    driver.quit()
    print("Tarayıcı kapatıldı.")