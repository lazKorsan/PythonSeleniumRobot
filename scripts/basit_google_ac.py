"""
Bu basit betik, Selenium kullanarak Chrome tarayıcısını açar ve google.com'a gider.
"""
from utils.driver_manager import DriverManager
import time

def open_google():
    """
    Chrome'u açar, google.com'a gider ve 5 saniye açık tutar.
    """
    print("Chrome tarayıcısı başlatılıyor...")
    # headless=False parametresi tarayıcının görünür olmasını sağlar.
    # Eğer tarayıcıyı görmeden arka planda çalıştırmak isterseniz True yapabilirsiniz.
    dm = DriverManager(browser="chrome", headless=False)
    
    # driver_context, işi bittiğinde tarayıcının otomatik olarak kapanmasını sağlar.
    with dm.driver_context() as driver:
        print("Google.com açılıyor...")
        driver.get("https://www.google.com")
        print("Sayfa başlığı:", driver.title)
        print("Tarayıcı 5 saniye açık kalacak...")
        time.sleep(5)
        print("Tarayıcı kapatılıyor.")

if __name__ == "__main__":
    open_google()
