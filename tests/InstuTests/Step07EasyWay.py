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

# Buradaki adım step 7'nin başına dahil edilmeyecek.
driver.get("https://qa.instulearn.com/panel/webinars/3652/step/7")

InstuUtils.step7(driver, quiz_title="Certifica alma sınavı", exam_time="45", attempt_count="3")