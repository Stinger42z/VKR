import re

def parsing_annotation(text):

    parts = re.split('Аннотация\.|Abstract\.', text)[1:]
    ans = []

    for q in parts:
        part = re.split('\n\n|\n \n', q)[0]
        part = ''.join(part)

        while part[-1] == ' ':
            part = part[:-1]

        while part[0] == ' ':
            part = part[1:]

        part = part.split('\n')
        part = ''.join(part)

        ans.append(part)
    
    return ans