Feature: Yeni Kurs Oluşturma

  Scenario: Kullanıcı yeni bir kurs oluşturur
    Given Kullanıcı tarayıcıyı açar
    When Kullanıcı siteye gider
      | URL             | testData.login_url |
    And Kullanıcı giriş yapar
      | E-posta         | testData.mail      |
      | Şifre           | testData.password  |
    And Kullanıcı yeni kurs oluşturma sayfasına gider
    And Kullanıcı temel bilgileri doldurur
    And Kullanıcı ek bilgileri doldurur
      | Kapasite        | 50                 |
      | Süre            | 45                 |
      | Etiketler       | math               |
      | Kategori        | 956                |
    And Kullanıcı fiyatlandırma bilgilerini doldurur
      | Erişim Günleri  | 10                 |
      | Fiyat           | 0                  |
    And Kullanıcı yeni bölüm bilgilerini doldurur
      | Bölüm Başlığı   | Yeni Bölüm Başlığı |
    And Kullanıcı ön koşul bilgilerini doldurur
      | Arama Metni     | SDET               |
    And Kullanıcı sıkça sorulan sorulara cevap verir
      | Soru            | Öğretmenler ile görüşme sıklığı |
      | Cevap           | Öğrencilerimiz 2 haftada 1 15 dk zoom görüşmesi yapabilirler |
    And Kullanıcı kurs sonunda yapılacak sınav hakkında bilgi verir
      | Sınav Başlığı    | Sertifika alma sınavı |
      | Sınav Süresi     | 45                 |
      | Deneme Sayısı    | 3                  |

      
