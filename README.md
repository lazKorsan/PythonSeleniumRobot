# open_google.py

Bu küçük proje `open_google.py` betiğini içerir. Amaç: Python ile `https://www.google.com` açmak.

Kullanım:

- Hızlı (varsayılan, ekstra paket gerektirmez):

```powershell
python .\open_google.py
```

- Selenium ile otomasyon (ek paketler gerekli):

```powershell
pip install -r requirements.txt
python .\open_google.py --selenium
```

Notlar:
- `--selenium` seçeneği `selenium` ve `webdriver-manager` paketlerini kullanır.
- Eğer tarayıcı otomatik kurulumu sorun çıkarırsa, manuel sürücü kurulumunu veya farklı bir WebDriver kullanmayı deneyin.
