def spam(dividBy):
    try:
        return 42 / dividBy
    except ZeroDivisionError:
        print('Error: invalid argument.')


print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))
