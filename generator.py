import random
import string


def generate_password(length, use_symbols):

    if length < 4:
        raise ValueError("Password length should be at least 4")

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    password_chars = []

    # Ensure required characters
    password_chars.append(random.choice(lowercase))
    password_chars.append(random.choice(uppercase))
    password_chars.append(random.choice(digits))

    if use_symbols:
        password_chars.append(random.choice(symbols))

    # Create character pool
    characters = lowercase + uppercase + digits
    if use_symbols:
        characters += symbols

    # Fill remaining characters
    while len(password_chars) < length:
        password_chars.append(random.choice(characters))

    # Shuffle to randomize positions
    random.shuffle(password_chars)

    return "".join(password_chars)
