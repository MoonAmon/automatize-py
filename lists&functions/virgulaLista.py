spam = ['apples', 'bananas', 'tofu', 'cats']


def virgula(valor, none=None):
    newspam = str
    for i in valor:
        if i == valor[-2]:
            print(str(newspam))
        elif i == valor[-1]:
            newspam = ' and ' + str(i)
            print(newspam)
        else:
            newspam = str(i) + ','
            print(newspam, end=' ')
    return none


print(virgula(spam))
