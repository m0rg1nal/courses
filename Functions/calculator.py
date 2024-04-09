first_number = float(input('Enter a number: '))
operator = input('Enter an operation (+, - , /, *) : ')
second_number = float(input('Enter a number: '))

def calculate(number1, operator, number2):
    if operator == '+':
        return number1 + number2
    elif operator == '-':
        return number1 - number2
    elif operator == '/':
        return number1 / number2
    elif operator == '*':
        return number1 * number2
    else:
        return "Invalid operation..."

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


result = calculate(first_number, operator, second_number)
print(result)
print(is_prime(result))
