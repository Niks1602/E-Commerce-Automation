Feature: Login to SauceDemo

    Scenario: Valid user logs in
    Given user opens the login page
    When user logs in with username "standard_user" and password "secret_sauce"
    Then user should land on the products page
