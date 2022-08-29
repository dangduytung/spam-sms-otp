import phonenumbers


def manual_replace(s, char, index):
    return s[:index] + char + s[index + 1:]


def add_code_VN(phone_number: str) -> str:
    """Prepend '+84' sign if required, then parse phone number"""
    if not phone_number.startswith('+'):
        if phone_number.startswith('0'):
            phone_number = manual_replace(phone_number, '+84', 0)
        else:
            phone_number = '+84' + phone_number
    return phone_number


def is_valid_phone_number_VN(phone_number: str) -> str:
    phone_number = add_code_VN(phone_number)
    z = phonenumbers.parse(phone_number)
    return phonenumbers.is_valid_number(z)
