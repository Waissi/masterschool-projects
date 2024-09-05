def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def get_sum_list_of_two_primes(user_number):
    sum_list = []
    for num1 in range(2, user_number // 2):
        if is_prime(num1):
            num2 = user_number - num1
            if num2 >= 2 and is_prime(num2):
                sum_list.append((num1, num2))
    return sum_list


def get_user_number():
    while True:
        try:
            user_number = int(input("Enter an even number:"))
            if user_number % 2 == 1:
                print(f"{user_number} is not an even number")
                continue
            break
        except ValueError:
            print("Incorrect input")
    return user_number


def main():
    user_number = get_user_number()
    prime_list = get_sum_list_of_two_primes(user_number)
    for num1, num2 in prime_list:
        print(f"The number {user_number} equals to the sum of {
              num1} and {num2}")


if __name__ == "__main__":
    main()
