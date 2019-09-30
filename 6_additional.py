def custom_split(string, delimiter):
    list1 = []
    while string.find(delimiter) != -1:
        index = string.find(delimiter)
        list1.append(string[:index])
        string = string[index+len(delimiter):]
    list1.append(string)
    return list1


string1 = 'abcdefabcdefabcdef'
print(custom_split(string1, 'cd'))