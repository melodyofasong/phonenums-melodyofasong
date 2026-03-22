import pandas as pd
import phonenumbers
from phonenumbers import PhoneNumberMatcher

def phonenums(x):
	matcher = PhoneNumberMatcher(x, "IN")
	phones = []

	for match in matcher:
		original_num = phonenumbers.format_number(match.number, phonenumbers.PhoneNumberFormat.NATIONAL)
		phones.append(original_num)  

	phones = list(set(phones))
	phones = pd.DataFrame(phones, columns=["Phone Numbers"])
	phones.index += 1
	return phones