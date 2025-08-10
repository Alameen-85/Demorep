# Basic Calculator Program

# Ask user for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Ask user for the operation
operation = input("Enter the operation (+, -, *, /): ")

# Perform the calculation
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        print("Error: Division by zero is not allowed.")
        exit()
else:
    print("Invalid operation entered.")
    exit()

# Display the result
print(f"{num1} {operation} {num2} = {result}")