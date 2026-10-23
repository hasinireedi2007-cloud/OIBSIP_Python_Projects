import random
import string
import secrets
import tkinter as tk


def generate_password():
    try:
        length = int(input("Enter password length: "))

        if length <= 0:
            print("Please enter a positive number.")
            return

        print("\nSelect character types:")
        print("1. Digits")
        print("2. Special characters")
        print("3. Uppercase letters")
        print("4. Lowercase letters")

        choices = input(
            "Enter choices (e.g., 1234): "
        )

        characters = ""

        if '1' in choices:
            characters += string.digits
        if '2' in choices:
            characters += string.punctuation
        if '3' in choices:
            characters += string.ascii_uppercase
        if '4' in choices:
            characters += string.ascii_lowercase

        if not characters:
            print("Please select at least one character type.")
            return

        if not all(c in "1234" for c in choices):
            print("Invalid choice. Please enter digits from 1 to 4.")
            return

        password = ''.join(
            secrets.choice(characters)
            for _ in range(length)
        )

        print("\n" + "=" * 40)
        print("GENERATED PASSWORD:", password)
        print("=" * 40)

        print("\n1. Copy password to clipboard")
        print("2. Save password to file")
        print("3. Generate another password")
        print("4. Exit")

        action = input("Choose an option: ")

        if action == '1':
            try:
                root = tk.Tk()
                root.withdraw()
                root.clipboard_clear()
                root.clipboard_append(password)
                root.update()
                root.destroy()
                print("Password copied to clipboard!")
            except Exception:
                print("Could not copy password to clipboard.")

        elif action == '2':
            with open("generated_password.txt", "a") as file:
                file.write(password + "\n")
            print("Password saved to generated_password.txt")

        elif action == '3':
            return generate_password()

        elif action == '4':
            print("Thank you for using Password Generator!")

        else:
            print("Invalid option.")

    except ValueError:
        print("Please enter a valid number.")


print("=" * 40)
print("     RANDOM PASSWORD GENERATOR")
print("=" * 40)

generate_password()