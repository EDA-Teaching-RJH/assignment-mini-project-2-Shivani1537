import re

def is_valid_number(user_input):
    return bool(re.match(r"^\d+$", user_input))

def is_valid_name(name):
    return bool(re.match(r"^[A-Za-z]+$", name))