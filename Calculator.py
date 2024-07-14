def calculator():
    print("Simple Calculator")
    
    num1 = float(input("Enter the first number: "))
    operation = input("Enter operation (+, -, *, /): ")
    num2 = float(input("Enter the second number: "))
    
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 == 0:
            result = "Error! Division by zero."
        else:
            result = num1 / num2
    else:
        result = "Invalid operation!"
    
    print(f"The result is: {result}")

if name == "main":
    calculator()
