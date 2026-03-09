from generator import generate_password
import pyperclip


def main():

    print("=== Password Generator ===")

    length = int(input("Enter password length: "))

    symbol_choice = input("Include symbols? (y/n): ").lower()
    use_symbols = symbol_choice == "y"

    password = generate_password(length, use_symbols)

    print("\nGenerated Strong Password:")
    print(password)

    copy_choice = input("\nCopy password to clipboard? (y/n): ").lower()

    if copy_choice == "y":
        pyperclip.copy(password)
        print("Password copied to clipboard!")


if __name__ == "__main__":
    main()
