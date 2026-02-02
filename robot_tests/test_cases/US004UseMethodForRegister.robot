*** Settings ***
Library     SeleniumLibrary
Resource    LoyalFriendKeywords.resource

*** Test Cases ***
New User Registration Test
    Open Browser    https://qa.loyalfriendcare.com/en    chrome
    Maximize Browser Window
    
    # Kayıt metodunu çağırıyoruz
    Loyal Friend Register Method    lazKorsan    Query.2026
    
    Close Browser