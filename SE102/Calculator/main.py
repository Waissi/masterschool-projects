def calculate(text_input):
    num1 = int(text_input[0])
    num2 = int(text_input[-1])
    operator = text_input[1]
    if operator == '+':
        return num1 + num2, -1
    elif operator == '-':
        return num1 - num2, -1
    elif operator == '*':
        return num1 * num2, -1
    elif operator == '/':
        return num1 / num2, -1
    elif operator == '~':
        return num1 // num2, num1 % num2


print("Welcome to the Python calculator!")
number_of_calculations = int(
    input("How many calculations do you want to do? "))
for i in range(number_of_calculations):
    user_input = input("What do you want to calculate? ")
    result, remainder = calculate(user_input)
    print(f"The answer is {result}")
    if remainder >= 0:
        print(f"The remainder is {remainder}")
