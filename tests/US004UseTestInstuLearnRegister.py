import unittest
import logging
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.InstuLearnAutomation import InstuLearnAutomation

# Log yapılandırması
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class US004UseTestInstuLearnRegister(unittest.TestCase):

    def setUp(self):
        """Test başlamadan önce tarayıcı ayarlarını yapar."""
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 15)

    def tearDown(self):
        """Test bittikten sonra tarayıcıyı kapatır."""
        time.sleep(5) # Sonucu görmek için
        self.driver.quit()

    def test_register_with_automation_class(self):
        """US004: InstuLearnAutomation sınıfını kullanarak Instructor kaydı testi."""
        # Otomasyon sınıfından bir nesne oluştur ve mevcut driver'ı kullanmasını sağla
        bot = InstuLearnAutomation(driver=self.driver)
        
        # Kayıt metodunu çağır
        yeni_kullanici_email = bot.test_register_instructor("Test Otomasyon Kullanici", "Query.2026")
        
        logging.info(f"Yeni email ile kayıt denendi: {yeni_kullanici_email}")

        # DOĞRULAMA (Validation)
        # Kayıt sonrası login sayfasına yönlendirilip yönlendirilmediğini kontrol et
        try:
            self.wait.until(EC.url_contains("/login"))
            logging.info("Kayıt BAŞARILI: Login sayfasına yönlendirildi.")
        except Exception as e:
            self.driver.save_screenshot("register_hata_US004.png")
            self.fail(f"Kayıt sonrası beklenen yönlendirme gerçekleşmedi! Hata: {e}")

if __name__ == "__main__":
    unittest.main()