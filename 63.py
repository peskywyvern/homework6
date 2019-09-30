def wrap(string, width):
    new_string = ''
    for character in string:
        if string.index(character) % width == 0:
            new_string = f'{new_string} \n'
        new_string = f'{new_string}{character}'
    return new_string


print(wrap('ABCDEFGHIJKLMNOP', 5))
