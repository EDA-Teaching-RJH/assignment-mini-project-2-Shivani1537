import re

def is_valid_number(user_input):
    return bool(re.match(r"^\d+$", user_input))