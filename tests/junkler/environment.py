from utils.driver_manager import DriverManager
import shutil

def before_scenario(context, scenario):
    """
    Her senaryo öncesi çalışır. Tarayıcıyı başlatır.
    """
    # headless=True ayarı ile tarayıcıyı gizli modda çalıştırabilirsiniz.
    dm = DriverManager(browser="chrome", headless=False, maximize=True)
    context.driver = dm.create_driver()
    context.dm = dm  # Geçici profili silebilmek için dm'i context'e ekliyoruz.

def after_scenario(context, scenario):
    """
    Her senaryo sonrası çalışır. Tarayıcıyı kapatır.
    """
    if hasattr(context, 'driver') and context.driver:
        context.driver.quit()
    
    # DriverManager tarafından oluşturulan geçici profil dizinini temizle
    if hasattr(context, 'dm') and context.dm._temp_profile_dir:
        try:
            shutil.rmtree(context.dm._temp_profile_dir, ignore_errors=True)
        except Exception as e:
            print(f"Geçici profil silinirken bir hata oluştu: {e}")
