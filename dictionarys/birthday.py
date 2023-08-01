import math
birthday = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break



    if name in birthday:
        print(birthday[name] + 'is the birthday of' + name)
    else:
        print('I do not have birthday information for' + name)
        print('What is their birthday?')
        bday = input()
        birthday[name] = bday
        print('Birthday database updated.')