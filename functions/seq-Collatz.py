def collatz(number):
    try:
        if (number % 2) == 0:
            number //= 2
            return number
        else:
            number = 3 * number + 1
            return number
    except ValueError:
        print('Error: invalid argument!')


print('Digite um número:')
number = int(input())
while number != 1:
    print(number)
    number = collatz(number)
