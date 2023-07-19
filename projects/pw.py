#! /usr/bin/env python3
# pw.py - Um programa para repositório de senhas que não é seguro.

PASSWORDS = {'email': 'fjaksdfowie23kfj',
             'blog': 'sdkfjwo4235ef9LLOJj',
             'luggage': '12345'}

import sys,pyperclip
if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1] # o primeiro argumento da linha de comando é o nome da conta

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)
    print('Digite a senha para a conta steam')
    senha = input()
    PASSWORDS[account] = senha
    pyperclip.copy(PASSWORDS[account])
    print('Password saved!\n Password for ' + account + ' copied to clipboard.')