from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Tarayıcı sürücüsünü başlat
driver = webdriver.Chrome()

# Belirli bir URL'ye git
driver.get("https://yandex.com")

time.sleep(5)

# Belirli bir öğenin yüklenmesini bekle
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "element_id"))
    )
finally:
    driver.quit()
    driver.get("https://www.yandex.com")
    assert driver.title == "Yandex"
    driver.quit()
    
    
def test_yandex_title():
    """yandex ana sayfasının başlığını kontrol eder."""
    driver = webdriver.Chrome()
    driver.get("https://www.yandex.com")
    assert driver.title == "Yandex"
    
    #driver belli bir sure bekletmek için gerekli komut 
    import time
    time.sleep(5)  # 5 saniye bekletir
    driver.quit()
    
    # bu test fonksiyonunu pytest ile çalıştırabilirsiniz.
    # pytest komutunu kullanarak terminalden çalıştırabilirsiniz.
    # pytest tests/test_open_driver.py