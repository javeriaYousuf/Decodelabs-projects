import random
import string

def generate_password(length):
    # letters (upper + lower), numbers, and symbols like @#$
    characters = string.ascii_letters + string.digits + string.punctuation

    # make sure the password has at least one of each type
    # otherwise we might get a password with no numbers or no symbols
    password_chars = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation),
    ]

    # fill up the rest of the password
    for _ in range(length - 4):
        password_chars.append(random.choice(characters))

    # shuffle so it doesn't always start with a letter then number then symbol
    random.shuffle(password_chars)

    return ''.join(password_chars)


def get_valid_length():
    while True:
        user_input = input("Enter password length (minimum 8): ")

        # if they typed something like "abc" instead of a number
        if not user_input.isdigit():
            print("  Please enter a number.\n")
            continue

        length = int(user_input)

        # 8 is the minimum, anything less is too easy to crack
        if length < 8:
            print("  Too short! Use at least 8 characters.\n")
            continue

        return length


def main():
    print("----------------------------------")
    print("     Random Password Generator    ")
    print("----------------------------------\n")

    length = get_valid_length()
    password = generate_password(length)

    print(f"\n  Your password: {password}")
    print(f"  Length: {len(password)} characters")
    print("\n----------------------------------")


if __name__ == "__main__":
    main()