#password generator
import random
print("--------------------------")
print("     PASSWORD GNERATOR    ")
print("--------------------------")
while True:
    try:
        length = int(input("\nEnter desired length for your password: "))
        if length <= 0:
            print("Please enter a positive number.")
            continue
    except ValueError:
        print("Please enter a valid number.")
        continue

    print("\nChoose type of pattern: ")
    print("1. Letters only")
    print("2. Letters and numbers")
    print("3. Letters, numbers and symbols")

    choice = input("Enter your choice: ")

    if choice == "1":
        characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    elif choice == "2":
        characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    elif choice == "3":
        characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    else:
        print("Invalid choice!setting default to letters only")
        characters ="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    
    password = "".join(random.choice(characters) for _ in range(length))

    print("\nGenerated password:", password)
    print("Length of your password:", length)

    #strength
    if length < 6:
        print("Password strength: Weak password!")
    elif length < 10:
        print("Password strength: Medium password")
    else:
        print("Password strength: Strong password")

    new = input("\nDo you want to generate another password? (yes/no): ")
    if new.lower() != "yes":
        print("\nThank you for using the password generator.")
        print("Have a good day!")
        break