import logging
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# Log Yapılandırması
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class InstuLearnAutomation:
    def __init__(self, driver=None):
        if driver:
            self.driver = driver
            self._driver_managed_externally = True
        else:
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()
            self._driver_managed_externally = False
        
        self.wait = WebDriverWait(self.driver, 15)
        self.base_url = "https://qa.instulearn.com/"

    def inatci_tikla(self, xpath, max_deneme=5):
        """Elemente tıklamak için döngülü mekanizma."""
        for i in range(max_deneme):
            try:
                element = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
                element.click()
                return True
            except:
                logging.warning(f"Deneme {i+1}: Buton henüz hazır değil, bekleniyor...")
                time.sleep(2)
        return False

    def setup(self):
        logging.info(f"Siteye gidiliyor: {self.base_url}")
        self.driver.get(self.base_url)

    def test_register_instructor(self, full_name, password):
        """US003: Instructor Kayıt Testi"""
        logging.info("--- Register Testi Başladı ---")
        self.setup()
        
        # Register butonu
        register_xpath = '//a[@href="/register" and contains(@class, "text-dark-blue")]'
        self.inatci_tikla(register_xpath)

        # Instructor seçimi
        instructor_xpath = '(//*[@class="font-12 cursor-pointer px-15 py-10"])[2]'
        instructor_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, instructor_xpath)))
        instructor_btn.click()

        # Dinamik Email
        timestamp = datetime.now().strftime("%d%m%Y%H%M%S")
        dynamic_email = f"lazKorsan{timestamp}@gmail.com"
        
        # Form Doldurma (Tab Navigasyonu ile)
        email_box = self.wait.until(EC.visibility_of_element_located((By.ID, 'email')))
        email_box.send_keys(dynamic_email)
        
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.TAB).send_keys(full_name) # Full Name
        actions.send_keys(Keys.TAB).send_keys(password)  # Password
        actions.send_keys(Keys.TAB).send_keys(password)  # Confirm Password
        actions.send_keys(Keys.TAB)                      # Timezone'u atla
        actions.send_keys(Keys.TAB).send_keys(Keys.SPACE)# Terms Checkbox
        actions.perform()
        
        # Submit
        submit_xpath = '//button[@type="submit" and contains(@class, "btn-primary")]'
        self.driver.find_element(By.XPATH, submit_xpath).click()
        logging.info(f"Kayıt tamamlandı. Email: {dynamic_email}")
        return dynamic_email

    def test_login(self, email, password):
        """US001: Login Testi"""
        logging.info("--- Login Testi Başladı ---")
        self.setup()

        # Login butonu
        login_xpath = '//a[@href="/login" and contains(@class, "text-dark-blue")]'
        self.inatci_tikla(login_xpath)

        # Email ve Şifre
        email_box = self.wait.until(EC.visibility_of_element_located((By.ID, 'email')))
        email_box.send_keys(email)
        
        password_box = self.driver.find_element(By.ID, 'password')
        password_box.send_keys(password)

        # Submit
        submit_xpath = '//button[@type="submit" and contains(@class, "btn-primary")]'
        self.driver.find_element(By.XPATH, submit_xpath).click()
        logging.info(f"Giriş yapıldı: {email}")

    def kapat(self):
        if not self._driver_managed_externally:
            time.sleep(5)
            self.driver.quit()
            logging.info("Tarayıcı kapatıldı.")

# --- TESTLERİ ÇALIŞTIRMA BÖLÜMÜ ---
if __name__ == "__main__":
    bot = InstuLearnAutomation()
    
    try:
        # 1. Kayıt Ol (US003)
        yeni_email = bot.test_register_instructor("lazKorsan", "Query.2026")
        
        time.sleep(3) # Sayfalar arası geçiş için
        
        # 2. Yeni Kayıt Olunan Hesapla Giriş Yap (US001)
        bot.test_login(yeni_email, "Query.2026")
        
    except Exception as e:
        logging.error(f"Test sırasında hata: {e}")
    finally:
        bot.kapat()