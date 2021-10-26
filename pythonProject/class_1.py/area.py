import phonenumbers
from class_1 import number

from phonenumbers import geocoder
ch_number = phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(ch_number, "en"))

from phonenumbers import carrier
operator_name = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(operator_name, "RO"))