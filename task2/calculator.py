#basic python calculator
opt = input("Choose operation (+ , - , * , / ): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if opt == "+":
    result = num1 + num2
    print("Result: ", result)


elif opt == "-":
    result = num1 - num2
    print("Result: ", result)

elif opt == "*":
    result = num1 * num2
    print("Result: ", result)

elif opt == "/":
    if num2 != 0:
        result = num1 / num2
        print("Result: ", result)
    else:
        print("Division by zero is not possible!!")

else:
    print("invalid choice.")