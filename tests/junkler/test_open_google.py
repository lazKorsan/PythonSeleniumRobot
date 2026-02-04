"""
Örnek test dosyası.

Bu testin çalışması için projenin ana dizinindeyken
'pytest' komutunu çalıştırmanız gerekir.

'pytest' kurulu değilse, 'pip install pytest' ile kurabilirsiniz.
"""
import pytest
from utils.driver_manager import DriverManager

def test_google_title():
    """Google ana sayfasının başlığını kontrol eder."""
    dm = DriverManager(browser="chrome", headless=False)
    with dm.driver_context() as driver:
        driver.get("https://www.google.com")
        assert driver.title == "Google"
        
# Bu dosyayı pytest ile çalıştırmak için terminalde şu komutu kullanın:
# pytest tests/test_open_google.py        

