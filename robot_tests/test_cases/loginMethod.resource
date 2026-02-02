*** Settings ***
Library    SeleniumLibrary
Library    String

*** Keywords ***
Loyal Friend Login Method
    [Arguments]    ${email}    ${password}    ${expected_user}
    
    # Giriş linkine tıkla
    Wait Until Element Is Visible    //*[@id="top_menu"]/li[1]/a    10s
    Click Element    //*[@id="top_menu"]/li[1]/a
    Sleep    2s

    # Bilgileri doldur (Press Keys ile TAB ve ENTER simülasyonu)
    Press Keys    None    ${email}    TAB    ${password}    ENTER
    Sleep    3s

    # Kullanıcı ismini al ve ayıkla
    Wait Until Element Is Visible    //a[@class='btn_add']    10s
    ${raw_text}=    Get Text    //a[@class='btn_add']
    ${actual_name}=    Strip String    ${raw_text}

    # Şiirsel Raporlama
    Log To Console    \n--- İKON AYIKLAMA VE TEST ŞİİRİ ---
    Log To Console    Aranan kahraman: ${expected_user}
    Log To Console    Bulunan cengaver: ${actual_name}

    # Doğrulama (Assert)
    Should Be Equal As Strings    ${actual_name}    ${expected_user}
    Log To Console    Ayarlar çarkı döndü, isim doğru takıldı! ✅