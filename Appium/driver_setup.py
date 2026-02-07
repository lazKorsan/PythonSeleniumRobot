import os
from appium import webdriver
from appium.options.android import UiAutomator2Options

# Tekil bir driver nesnesi sağlamak için global bir değişken
_driver = None

def get_appium_driver():
    """
    Appium sürücüsünü (driver) başlatan ve yapılandıran ana fonksiyondur.
    Eğer sürücü zaten varsa, mevcut olanı döndürür (Singleton pattern).
    """
    global _driver
    if _driver is not None:
        return _driver

    try:
        # --- Desired Capabilities (İstenen Yetenekler) ---
        # Java kodunuzdaki ayarları buraya taşıyoruz.
        
        # APK dosyasının tam yolunu dinamik olarak alıyoruz.
        # Bu betik (driver_setup.py) Appium klasörü içindedir.
        current_dir = os.path.dirname(os.path.abspath(__file__))
        app_path = os.path.join(current_dir, 'querycart2006.apk')

        options = UiAutomator2Options()
        # Temel Platform ve Otomasyon Ayarları
        options.platform_name = 'Android'
        options.automation_name = 'UiAutomator2'
        
        # Cihaz ve Uygulama Ayarları
        options.udid = 'emulator-5554'  # Java'da belirtilen cihaz ID'si
        options.app = app_path          # APK dosyasının yolu
        options.app_package = 'com.wise.querycart'
        options.app_activity = 'com.wise.querycart.MainActivity'
        
        # Oturum ve İzin Ayarları
        options.no_reset = False  # Her test öncesi uygulamayı sıfırlar
        options.auto_grant_permissions = True # İzinleri otomatik olarak kabul eder
        options.new_command_timeout = 3000 # Komut zaman aşımı (saniye cinsinden)

        # Appium sunucusuna bağlan ve sürücüyü oluştur
        _driver = webdriver.Remote('http://127.0.0.1:4723', options=options)
        
        print("✅ Appium sürücüsü başarıyla oluşturuldu.")
        
        return _driver

    except Exception as e:
        print(f"❌ Appium sürücüsü oluşturulurken bir hata oluştu: {e}")
        raise

def quit_appium_driver():
    """
    Mevcut Appium sürücüsünü sonlandırır ve değişkeni sıfırlar.
    """
    global _driver
    if _driver:
        _driver.quit()
        _driver = None
        print("✅ Appium sürücüsü başarıyla kapatıldı.")

