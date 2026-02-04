import sys
import os
import time

# CRITICAL FIX: Üst dizini değil, iki üst dizini ekle
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)  # insert(0) daha öncelikli

print(f"Project root: {project_root}")
print(f"Utils path exists: {os.path.exists(os.path.join(project_root, 'utils'))}")

# Importlar - ARTIK PAKET GİBİ ÇALIŞACAK
try:
    from utils.config import LoginData
    from utils.InstuLearnAutomation import InstuLearnAutomation
    print("✓ Import başarılı!")
except ImportError as e:
    print(f"✗ Import hatası: {e}")
    print(f"Current sys.path: {sys.path}")
    exit(1)

# Testi Başlat
def run_login_test():
    bot = InstuLearnAutomation()
    
    try:
        bot.test_login(LoginData.EMAIL, LoginData.PASSWORD)
        print("Login başarılı, 15 saniye bekleniyor...")
        time.sleep(15)
    except Exception as e:
        print(f"Hata oluştu: {e}")
    finally:
        bot.kapat()

if __name__ == "__main__":
    run_login_test()