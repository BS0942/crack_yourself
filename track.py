import phonenumbers
from phonenumbers import geocoder, carrier
# Get the phone number from the user.
phone_number = input("Enter a Bangladeshi phone number: ")
# Parse the phone number.
parsed_phone_number = phonenumbers.parse(phone_number, "BD")
# Get the location of the phone number.
location = geocoder.description_for_number(parsed_phone_number, "en")
# Get the carrier of the phone number.
carrier = carrier.name_for_number(parsed_phone_number, "en")
# Print the location and carrier of the phone number.
print("Location:", location)
print("Carrier:", carrier)