import requests
from behave import given, when, then


@given('I have latitude "{lat}" and longitude "{lon}"')
def step_given_coordinates(context, lat, lon):
    context.lat = lat
    context.lon = lon
    context.url = f"https://nominatim.openstreetmap.org/reverse?lat={lat}&lon={lon}&format=json"


@when("I send a GET request to the reverse geocoding API")
def step_send_request(context):
    headers = {"User-Agent": "TestAgent"}  # Required by nominatim API
    context.response = requests.get(context.url, headers=headers)


@then("the response status code should be 200")
def step_check_status_code(context):
    assert context.response.status_code == 200, f"Expected 200, got {context.response.status_code}"


@then('the response should contain "{expected_city}"')
def step_validate_response_content(context, expected_city):
    json_response = context.response.json()
    address = json_response.get("address", {})
    city = address.get("city") or address.get("town") or address.get("village")
    print(city)
    assert expected_city in city, f"Expected city {expected_city}, but got {city}"
