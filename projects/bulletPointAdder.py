#! /usr/bin/env python3
# bulletPointAdder.py - Acrecenta marcadores da Wikipedia no início
# de cada linha de texto do clipboard.

import pyperclip
text = pyperclip.paste()

# Separa as linhas e acrecenta os asteriscos.
lines = text.split('/n')
for i in range(len(lines)):        # percorre todos os índices da lista "lines" em um loop
    lines[i] = '* ' + lines[i]      # acrecenta um asterisco me cada string da lista "lines"
text = '/n'.join(lines)
pyperclip.copy(text)