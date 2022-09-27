def cid_to_text(string):
    a = string.find('(cid:')
    b = string[a:].find(')')


    while a != -1:
        string = string[:a] + chr(int(string[a + 5:a + b]) + 470) + string[a+b+1:]
        a = string.find('(cid:')
        b = string[a:].find(')')

    return string

