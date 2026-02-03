from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import logging
import time

# 1. Log Yapılandırması (Bunu eklemeni öneririm, logları konsolda görmen için)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

driver = webdriver.Chrome()
driver.maximize_window()

# 2. Yardımcı Fonksiyon: "İnatçı" Element Bulucu (Senin istediğin döngü mantığı)
def inatci_tikla(xpath, max_deneme=5):
    for i in range(max_deneme):
        try:
            logging.info(f"Deneme {i+1}: Element aranıyor...")
            element = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, xpath)))
            element.click()
            logging.info("Tıklama başarılı!")
            return True
        except:
            logging.warning(f"{xpath} henüz hazır değil, 3 saniye bekleniyor...")
            time.sleep(3)
    return False

# Test Akışı
driver.get("https://qa.instulearn.com/")

# Register Butonu için döngülü tıklama
register_xpath = '//a[@href="/register" and contains(@class, "text-dark-blue")]'
if not inatci_tikla(register_xpath):
    logging.error("Register butonu bulunamadı, test durduruluyor.")
    driver.quit()

# Instructor Seçeneği (Wait ekledik çünkü formun değişmesini beklemeliyiz)
wait = WebDriverWait(driver, 10)
instructor_xpath = '//div[contains(text(), "Instructor")]' # Metin üzerinden gitmek daha sağlıklıdır
try:
    # Eğer önceki XPath çalışmazsa senin verdiğini kullan:
    instructor_xpath = '(//*[@class="font-12 cursor-pointer px-15 py-10"])[2]'
    instructor_opt = wait.until(EC.element_to_be_clickable((By.XPATH, instructor_xpath)))
    instructor_opt.click()
    logging.info("Instructor seçildi.")
except Exception as e:
    logging.error(f"Instructor seçilemedi: {e}")

try:
    # Full Name'e geç ve yaz
    # Email
    # Dinamik Email oluşturuyoruz
    # Şimdiki zamanı al
    now = datetime.now()

    # İstenilen formatta tarihi oluştur
    timestamp = now.strftime("%d%m%Y%H%M")

    # Dinamik e-posta adresini oluştur
    dynamic_Email = "lazKorsan" + timestamp + "@gmail.com"
    print(f"Dinamik Email: {dynamic_Email}")
    logging.info(f"Dinamik Email: {dynamic_Email}")


    email_box = wait.until(EC.visibility_of_element_located((By.ID, 'email')))
    email_box.send_keys(dynamic_Email) # Benzersiz email için

    email_box.send_keys(Keys.TAB)
    time.sleep(0.2) # Çok hızlı geçişlerde bazen input odaklanamayabilir
    webdriver.ActionChains(driver).send_keys("lazKorsan").perform()
    logging.info("Full Name Tab ile girildi.")

    # Password'e geç ve yaz
    webdriver.ActionChains(driver).send_keys(Keys.TAB).send_keys("Query.2026").perform()
    logging.info("Password Tab ile girildi.")

    # Retype Password'e geç ve yaz
    webdriver.ActionChains(driver).send_keys(Keys.TAB).send_keys("Query.2026").perform()
    logging.info("Confirm Password Tab ile girildi.")

    # Time Zone'u geç (Genelde 1 veya 2 TAB gerekebilir, deneyelim)
    webdriver.ActionChains(driver).send_keys(Keys.TAB).perform()
    logging.info("Time Zone alanı Tab ile geçildi.")

    # termsCheckbox'e geç ve boşluk ile işaretle
    webdriver.ActionChains(driver).send_keys(Keys.TAB).send_keys(Keys.SPACE).perform()
    logging.info("Terms checkbox işaretlendi.")

    # Register Submit Button
    submit_btn_xpath = '//button[@type="submit" and contains(@class, "btn-primary")]'
    submit_btn = wait.until(EC.element_to_be_clickable((By.XPATH, submit_btn_xpath)))
    submit_btn.click()
    logging.info("Kayıt ol butonuna basıldı.")

    # Kayıt başarılı mesajı

except Exception as e:  logging.error(f"Form doldurma hatası: {e}")

time.sleep(10)
driver.quit()