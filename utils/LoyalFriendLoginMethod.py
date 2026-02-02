from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

# --- LOGIN METODU ---
def login_ve_dogrula(driver, email, sifre, beklenen_isim):
    """
    Bu metot giriş yapar ve kullanıcı adını doğrular.
    """
    try:
        # 1. Giriş Sayfasına git ve Giriş Butonuna bas
        login_link_xpath = '//*[@id="top_menu"]/li[1]/a'
        driver.find_element(By.XPATH, login_link_xpath).click()
        time.sleep(2)

        # 2. Bilgileri doldur (ActionChains ile)
        actions = ActionChains(driver)
        actions.send_keys(email) \
               .send_keys(Keys.TAB) \
               .send_keys(sifre) \
               .send_keys(Keys.ENTER) \
               .perform()
        
        time.sleep(3) # Sayfanın yüklenmesi için kısa bir ara

        # 3. Kullanıcı adını kontrol et
        xpath_kullanici = "//a[@class='btn_add']"
        element = driver.find_element(By.XPATH, xpath_kullanici)
        gercek_isim = element.text.strip()

        # 4. Senin meşhur şiirsel raporun
        print("\n" + "="*30)
        print("--- TEST SONUÇ ŞİİRİ ---")
        print(f"Sistemde aranan: {beklenen_isim}")
        print(f"Karşımıza çıkan: {gercek_isim}")

        if gercek_isim == beklenen_isim:
            print("Ayarlar çarkı döndü, isim doğru takıldı, ✅")
            print("Testin meşalesi, gururla yakıldı!")
            return True
        else:
            print("Eyvah! Çarklar karıştı, isimler uymadı, ❌")
            print("Sistem bu hatayı, asla duymadı...")
            return False
            
    except Exception as e:
        print(f"Hata oluştu hocam: {e}")
        return False

# --- ANA PROGRAM ---

# Tarayıcıyı bir kez başlatıyoruz
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://qa.loyalfriendcare.com/en")

# Metodu çağırıyoruz
basari_durumu = login_ve_dogrula(
    driver, 
    "lazKorsan20220262058@gmail.com", 
    "Query.2026", 
    "lazKorsan"
)

if basari_durumu:
    print("\n[SONUÇ] Test Genel Olarak Başarılı!")
else:
    print("\n[SONUÇ] Test Başarısız Oldu!")

# driver.quit()