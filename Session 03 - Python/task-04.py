import random
import string

print("1. Random Password Generator")
print("2. Password Strength Checker")

choice = input("Choose (1 or 2): ")

if choice == "1":
    while True:
        length = int(input("Enter password length: "))

        if length < 8:
            print("Password must be at least 8 characters")
            continue

        chars = string.ascii_letters + string.digits + "!@#$%&*?_"
        password = ""

        for i in range(length):
            password += random.choice(chars)

        print("Generated Password:")
        print(password)

        again = input("Generate another password? (y/n): ")

        if again.lower() != "y":
            break

elif choice == "2":
    while True:
        password = input("Enter your password: ")

        length = len(password) >= 8
        lower = False
        upper = False
        digit = False
        special = False

        for ch in password:
            if ch.islower():
                lower = True
            elif ch.isupper():
                upper = True
            elif ch.isdigit():
                digit = True
            elif ch in "!@#$%&*?_":
                special = True

        passed = 0

        if length:
            passed += 1
        if lower:
            passed += 1
        if upper:
            passed += 1
        if digit:
            passed += 1
        if special:
            passed += 1

        failed = 5 - passed

        if failed >= 3:
            print("Password Strength: Weak")
        elif failed == 2:
            print("Password Strength: Medium")
        elif failed == 1:
            print("Password Strength: Strong")
        else:
            print("Password Strength: Very Strong")

        if failed >= 2:
            print("Suggestions:")

            if not length:
                print("- Increase the length to at least 8 characters")
            if not upper:
                print("- Add uppercase letters")
            if not lower:
                print("- Add lowercase letters")
            if not digit:
                print("- Add numbers")
            if not special:
                print("- Add special characters")

            again = input("Enter another password? (yes / no): ")

            if again.lower() != "yes":
                break
        else:
            break

else:
    print("Invalid choice")