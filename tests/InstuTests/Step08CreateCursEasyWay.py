from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import testData
import InstuUtils

# Driver oluştur
driver = webdriver.Chrome()
driver.maximize_window()
print("Driver oluşturuldu.")

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

# 4. yeni kurs oluşturma sayfasına git
InstuUtils.navigateToNewCoursePage(driver)

# 5. basic infoBilgilerini doldur 
InstuUtils.step1(driver)

# 6. extraInfıBilgilerini doldur
InstuUtils.step2(driver, capacity="50", duration="45", tags="math", category_value="956")

# 7. pricingBilgilerini doldur
InstuUtils.step3(driver, access_days="10", price="0")

# 8. newSection Bilgilerini doldurma 
InstuUtils.step4(driver, title_text="Yeni Bölüm Başlığı")   

# 9. preRequest bilgilerini doldur 
InstuUtils.step5(driver, search_text="SDET")

# 10. sıkça sorulan soruya cevap ver 
InstuUtils.step6(driver, faq_question="Ogretmenler ile gorusme sıklıgı", faq_answer="Ogrencilerimiz 2 haftada 1 15 dk zoom gorusmesi yapabilirler")

# 11. Course sonunda yapılacak sınav hakkında bilgi ver
InstuUtils.step7(driver, quiz_title="Certifica alma sınavı", exam_time="45", attempt_count="3")



