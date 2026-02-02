Feature: Login Functionality
  Scenario: Successful login with valid credentials
    Given the user is on the login page
    When the user enters "lazKorsan20220262058@gmail.com" and "Query.2026"
    Then the user name "lazKorsan" should be visible
    