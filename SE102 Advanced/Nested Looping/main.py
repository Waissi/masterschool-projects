def print_triangle(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end='')
        print()
    for i in range(n - 1, 0, -1):
        for j in range(1, i + 1):
            print(j, end='')
        print()


def print_multiplication_table(n):
    print('', end='  ')
    for i in range(1, n + 1):
        print(i, end='  ')
    print()
    for i in range(1, n + 1):
        print(i, end=' ')
        for j in range(1, n + 1):
            space = ' ' if i * j > 9 else '  '
            print(i * j, end=space)
        print()


while True:
    number = int(input("Please enter a number:"))
    if number == -1:
        print("Bye!")
        break
    command = input("Please enter a command (triangle/mp):")
    if command == "triangle":
        print_triangle(number)
    elif command == "mp":
        print_multiplication_table(number)
