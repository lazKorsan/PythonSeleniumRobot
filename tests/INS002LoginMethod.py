import sys
import os
import time

# Proje kök dizinini ekle
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.append(project_root)

# Importlar (Artık paket olarak görecektir)
from utils.config import LoginData
from utils.InstuLearnAutomation import InstuLearnAutomation # Sınıfın olduğu dosya ismi

# Testi Başlat
def run_login_test():
    # Sınıfı başlatıyoruz (Driver'ı sınıf kendi oluşturur)
    bot = InstuLearnAutomation()
    
    try:
        # Sınıfın içindeki login metodunu çağırıyoruz
        bot.test_login(LoginData.EMAIL, LoginData.PASSWORD)
        
        print("Login başarılı, 15 saniye bekleniyor...")
        time.sleep(15)
        
    except Exception as e:
        print(f"Hata oluştu: {e}")
    finally:
        bot.kapat()

if __name__ == "__main__":
    run_login_test()