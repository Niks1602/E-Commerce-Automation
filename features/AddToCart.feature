Feature: Add product to cart
#
  @a1
  Scenario: Add a product to cart after successful login
    Given user opens the login page
    When user logs in with username "standard_user" and password "secret_sauce"
    And user adds product "Sauce Labs Backpack" to the cart
    Then cart icon should show 1 item

   @a2
  Scenario: User adds product to cart and completes checkout
    Given user is logged into the e-commerce site
    When user adds "Sauce Labs Bolt T-Shirt" to the cart
    And user proceeds to the cart
    And user clicks on checkout
    And user fills shipping info with "Nikhil", "Namdev", "411001"
    And user completes the checkout
    Then order confirmation page should be displayed

#        @a2
#  Scenario: User adds product to cart and completes checkout
#    Given user is logged into the e-commerce site
#    When user adds "Sauce Labs Backpack" to the cart
#    And user proceeds to the cart
#    And user clicks on checkout
#    And user fills shipping info with "Nikhil", "Namdev", "411001"
#    And user completes the checkout
#    Then order confirmation page should be displayed
