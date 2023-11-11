#!/usr/bin/env python3

first_dollar = True
processed_text = ''
filename = input('Type the name of the file.\n')
processed_filename = filename[:-3] + '_processed.md'

with open(filename, 'r') as f:
    text = f.read()
    print('Vorher: ', text)

    for char in text:
        if char == '$' and (char-1) != '\\':
            if first_dollar is True:
                char = r'\('
                first_dollar = False
            else:
                char = r'\)'
                first_dollar = True
        processed_text += char
    print('Nachher: ', processed_text)

with open(processed_filename, 'w') as f:
    f.write(processed_text)
