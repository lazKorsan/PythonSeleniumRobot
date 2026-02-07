import time
from driver_setup import get_appium_driver, quit_appium_driver

# bu testin çalışması için case içinde olunmalıdır 
# case için dir C:\Users\user\Desktop\python_planet2\Appium> kullan
# arkasından python test_sample.py 

def run_sample_test():
    """
    Basit bir test senaryosunu çalıştırır:
    1. Uygulamayı başlatır.
    2. 5 saniye bekler.
    3. Uygulamayı kapatır.
    """
    driver = None
    try:
        # 1. driver_setup.py'dan Appium sürücüsünü al
        driver = get_appium_driver()
        print("Test başladı. Uygulama açıldı.")

        # 2. Uygulamanın açıldığını görmek için bekle
        print("5 saniye bekleniyor...")
        time.sleep(5)
        print("Bekleme süresi bitti.")

        # Burada test adımlarınız yer alacak
        # Örnek: driver.find_element(by=AppiumBy.ID, value="...").click()
        
        print("✅ Örnek test başarıyla tamamlandı.")

    except Exception as e:
        print(f"❌ Test sırasında bir hata oluştu: {e}")

    finally:
        # 3. Test bittiğinde sürücüyü kapat
        if driver:
            quit_appium_driver()

if __name__ == "__main__":
    # Bu betiği doğrudan çalıştırmak için
    # 1. Appium sunucusunu başlatın.
    # 2. Android emülatörünüzü ("emulator-5554") başlatın.
    # 3. Komut satırından `python test_sample.py` komutunu çalıştırın.
    run_sample_test()
