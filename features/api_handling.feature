Feature: Reverse Geocoding using latitude and longitude

  Scenario: Get address using valid coordinates
    Given I have latitude "40.748817" and longitude "-73.985428"
    When I send a GET request to the reverse geocoding API
    Then the response status code should be 200
    And the response should contain "New York"

