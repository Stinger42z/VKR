import re

for i in range(1, 8):
    file_path = 'D:\\programs\\diplom\\program\\finished_text\\Proceedings_vol_' + str(i) + '.txt'
    file = open(file_path, 'r', encoding="utf-8").readlines()
    new_file = []
    for j in file:
        row = re.split('Введение|Introduction', j)
        if len(row) > 1:
            row[0] += '\n'
        new_file.append(row[0])

    file_path = 'D:\\programs\\diplom\\program\\finished_text\\Proceedings_vol_' + str(i) + 'test.txt'
    file = open(file_path, 'w', encoding="utf-8").writelines(new_file)