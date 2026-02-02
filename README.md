# 🐍 Python Planet 2: Web Otomasyonu Keşif Alanı

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/downloads/) 
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Bu proje, Python kullanarak web otomasyonu ve test süreçleri için çeşitli teknikleri ve araçları sergileyen bir koleksiyondur. Basit bir betikle bir web sayfasını açmaktan, Selenium ve Robot Framework gibi gelişmiş araçlarla karmaşık test senaryoları oluşturmaya kadar geniş bir yelpazede örnekler sunar.

## 🚀 Proje Hakkında

Projenin temel amacı, `https://www.google.com` adresini farklı yöntemlerle açarak Python'un web otomasyon yeteneklerini göstermektir. Bu basit görev üzerinden, farklı kütüphanelerin ve framework'lerin nasıl kullanıldığını, avantajlarını ve kurulum süreçlerini öğrenebilirsiniz.

### ✨ Öne Çıkan Özellikler

- Temel Erişim: Python'un dahili `webbrowser` modülü ile anında sayfa açma.
- Gelişmiş Otomasyon: `Selenium` kullanarak tarayıcıyı kontrol etme, etkileşimde bulunma ve ekran görüntüsü alma.
- Yapısal Testler: `pytest` ile modüler ve ölçeklenebilir test senaryoları.
- Anahtar Kelime Odaklı Test (KDT): `Robot Framework` ile okunabilir ve bakımı kolay testler oluşturma.

### 🛠️ Kullanılan Teknolojiler

- [Python](https://www.python.org/)
- [Selenium](https://www.selenium.dev/)
- [Robot Framework](https://robotframework.org/)
- [Pytest](https://docs.pytest.org/)
- [webdriver-manager](https://github.com/SergeyPirogov/webdriver_manager)

## 🔧 Kurulum

Projeyi yerel makinenizde çalıştırmak için aşağıdaki adımları izleyin.

1. **Depoyu Klonlayın**
    ```sh
    git clone <depo_url>
    cd python_planet2
    ```

2. **Sanal Ortam Oluşturun (Önerilir)**
    ```sh
    python -m venv .venv
    # Windows
    .\.venv\Scripts\activate
    # macOS/Linux
    source .venv/bin/activate
    ```

3. **Gerekli Paketleri Yükleyin**
    Proje kök dizinindeyken `requirements.txt` dosyasını kullanarak tüm bağımlılıkları yükleyin.
    ```sh
    pip install -r requirements.txt
    ```

## ⚡ Kullanım

Proje, farklı kullanım senaryoları için çeşitli betikler ve testler içerir.

### 1. Basit Google Açma Betiği

`scripts/open_google.py` betiği, iki farklı modda çalışabilir.

- **Hızlı Mod (Varsayılan)**: Ekstra paket gerektirmeden, Python'un dahili `webbrowser` modülünü kullanır.
    ```powershell
    python .\open_google.py
    ```

- **Selenium Modu**: Otomasyon için `Selenium` ve `webdriver-manager` kullanır. Tarayıcıyı otomatik olarak açar ve yönetir.
    ```powershell
    python .\open_google.py --selenium
    ```

### 2. Testleri Çalıştırma

- **Pytest Testleri**: `tests/` dizinindeki testleri çalıştırmak için:
    ```sh
    pytest
    ```

- **Robot Framework Testleri**: `robot_tests/test_cases/` dizinindeki `.robot` dosyalarını çalıştırmak için:
    ```sh
    robot .\robot_tests\test_cases\google_test.robot
    ```

## 📂 Dosya Yapısı

```
python_planet2/
├── robot_tests/        # Robot Framework test dosyaları
├── scripts/            # Bağımsız çalıştırılabilir Python betikleri
├── tests/              # Pytest ve diğer test framework'leri için testler
├── utils/              # Yardımcı fonksiyonlar ve modüller
├── requirements.txt    # Proje bağımlılıkları
└── README.md           # Bu dosya
```

---

Bu README, projenize yeni başlayanlar için daha net bir yol haritası sunar ve projenizin yeteneklerini daha iyi pazarlar. Başarılar!