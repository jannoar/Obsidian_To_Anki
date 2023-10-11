#!/usr/bin/env python3

first_dollar = True
processed_text = ''
filename = input('Type the name of the file.\n')

with open(filename, 'r') as f:
    text = f.read()
    print('Vorher: ', text)

    for char in text:
        if char == '$':
            if first_dollar is True:
                char = r'\('
                first_dollar = False
            else:
                char = r'\)'
                first_dollar = True
        processed_text += char
    print('Nachher: ', processed_text)

with open(filename, 'w') as f:
    f.write(processed_text)
