#BaseCalc is a basic calculator

# Add Function
def add(num1, num2):
    return num1 + num2

# Subtract Function 
def subtract(num1, num2):
    return num1 - num2

# Multiply Function
def multiply(num1, num2):
    return num1 * num2

# divide Function
def divide(num1, num2):
    return num1 / num2

print("List of available operations: \n" \
        "[1] Add +\n" \
        "[2] Subtract - \n" \
        "[3] Multiply x\n" \
        "[4] Divide /\n")

# USER INPUT
select = int(input("Select an operation from [1] [2] [3] [4]: "))

number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))

if select == 1:
    print(number_1, "+", number_2, "=", add(number_1, number_2))

elif select == 2:
    print(number_1, "-", number_2, "=", subtract(number_1, number_2))

elif select == 3:
    print(number_1, "x", number_2, "=", multiply(number_1, number_2))

elif select == 4:
    print(number_1, "/", number_2, "=", divide(number_1, number_2))
else:
    print("Error! Invalid user input. Please try again.")
