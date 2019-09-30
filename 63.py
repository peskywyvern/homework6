def wrap(string, width):
    new_string = ''
    for index, character in enumerate(string):
        if index % width == 0:
            new_string = f'{new_string} \n'
        new_string = f'{new_string}{character}'
    return new_string


print(wrap('testestestest', 2))
