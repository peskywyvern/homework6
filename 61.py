def insert_whitespace(text):
    new_text = ''
    for character in text:
        index = text.index(character)
        if index != len(text) - 1 and character.islower() and text[index+1].isupper():
            new_text = f'{new_text}{character} '
        else:
            new_text = f'{new_text}{character}'
    return new_text


text1 = 'WhatIsUp'
print(insert_whitespace(text1))