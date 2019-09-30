def insert_whitespace(text):
    new_text = ''
    for character in text:
        if character.isupper():
            new_text += ' ' + character
        else:
            new_text += character
    return new_text


text1 = 'WhatIsUp'
print(insert_whitespace(text1))