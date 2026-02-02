*** Settings ***
Documentation     Google ana sayfasını açmak için basit bir test.
Library           SeleniumLibrary

*** Test Cases ***
yandex Ana Sayfasi Basligini Dogrula
    [Documentation]    Google ana sayfasını açar ve başlığın doğru olduğunu doğrular.
    Open Browser    https://www.yandex.com    chrome
    Maximize Browser Window
    sleep  1200s
    Title Should Be    Google
    Close Browser

*** Keywords ***
# 13 ''
# Bu alana daha sonra kendi özel anahtar kelimelerinizi ekleyebilirsiniz. 
# robot robot_tests/test_cases/yandex_test.robot
