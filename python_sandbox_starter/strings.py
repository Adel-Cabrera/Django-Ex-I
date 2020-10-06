# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods


# String Formatting

# String Methods

import sys

from datetime import date

import validator

print(date.today())

s = 'Hello World'

print(s.count('World') * 5)

print(sys.version)

print(validator.validate_email('email@email.com'))