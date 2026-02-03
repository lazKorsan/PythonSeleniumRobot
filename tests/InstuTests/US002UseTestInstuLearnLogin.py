import unittest
import logging
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Log Ayarları
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TestInstuLearnLogin(unittest.TestCase):

    def setUp(self):
        """Her testten önce çalışır: Tarayıcıyı hazırlar."""
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 15)
        self.url = "https://qa.instulearn.com/"

    def tearDown(self):
        """Her testten sonra çalışır: Tarayıcıyı kapatır."""
        time.sleep(3) # Sonucu görmek için kısa bekleme
        self.driver.quit()

    def inatci_tikla(self, xpath):
        """Tıklanamayan butonlar için özel bekleme ve tıklama metodu."""
        try:
            element = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
            element.click()
            return True
        except Exception as e:
            logging.error(f"Butona tıklanamadı: {xpath} - Hata: {e}")
            return False

    def test_login_successful(self):
        """US001: Geçerli bilgilerle login testi."""
        driver = self.driver
        logging.info("Siteye gidiliyor...")
        driver.get(self.url)

        # 1. Login Butonuna Tıkla (Ana sayfa)
        login_btn_xpath = '//a[@href="/login" and contains(@class, "text-dark-blue")]'
        success = self.inatci_tikla(login_btn_xpath)
        self.assertTrue(success, "Ana sayfadaki Login butonuna tıklanamadı!")

        # 2. Login Formunu Doldur
        logging.info("Login formu dolduruluyor...")
        
        email_field = self.wait.until(EC.visibility_of_element_located((By.ID, "email")))
        email_field.send_keys("lazKorsan030220260417@gmail.com")

        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys("Query.2026")

        # 3. Giriş Yap Butonuna Tıkla (Formun altındaki)
        submit_btn_xpath = '//button[@type="submit" and contains(@class, "btn-primary")]'
        driver.find_element(By.XPATH, submit_btn_xpath).click()
        
        logging.info("Login butonuna basıldı, yönlendirme bekleniyor.")

        # 4. DOĞRULAMA (Assertion)
        # Giriş başarılıysa URL değişmeli veya bir profil ikonu çıkmalı
        try:
            # Örnek: URL'de '/panel' veya '/dashboard' geçiyor mu kontrol et
            self.wait.until(EC.url_contains("dashboard"))
            logging.info("Giriş BAŞARILI: Dashboard sayfasındayız.")
        except:
            logging.error("Giriş BAŞARISIZ: Dashboard sayfasına ulaşılamadı.")
            self.fail("Login sonrası dashboard sayfası açılmadı!")

if __name__ == "__main__":
    unittest.main()