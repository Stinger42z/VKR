import nltk
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def get_wordCloud(string):
    wordCloud = WordCloud(background_color='white',
                              width=3000,
                              height=2500,
                              max_words=200,
                              random_state=42
                         ).generate(string)
    return wordCloud

# сбор аннотаций
print('\nСбор аннотаций...')
classes = ['Физика', 'Химия', 'Математика', 'Биология и фундаментальная медицина', 'Экономика и управление', 'Строительство и архитектура', 'IT технологии и электроника']

labeled_annotation = []
for i in range(len(classes)):
    labeled_annotation.append([])
    print('\tСбор ' + str(i + 1) + ' класса...')
    path_to_translated_text = 'D:\\programs\\diplom\program\\translated_finished_text\\translated_finished_text_class_' + str(i + 1) + '.txt'
    current_annotations = open(path_to_translated_text, 'r', encoding = 'utf-8').readlines()
    for j in range(len(current_annotations)):
        labeled_annotation[i].append([i + 1, current_annotations[j].split('\n')[0]])

print('Пример полученного датасета')
print(labeled_annotation[0][0])

# разбить сроки на слова
print('\nРазбиение строк на слова...')
tokens = []
for i in range(len(labeled_annotation)):
    tokens.append([])
    for j in range(len(labeled_annotation[i])):
        tokens[i].append(nltk.word_tokenize(labeled_annotation[i][j][1]))

# удаление служебных слов и местоимений
print('Удаление лишних слов...')
print('\tОставляем глаголы, прилагательные, существительные...')
list_of_part_of_speech_tags = ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'FW', 'JJ', 'JJR', 'JJS', 'NN', 'NNS', 'NNP', 'NNPS', 'RB', 'RBR', 'RBS']
list_of_part_of_speech_tags_2 = ['FW', 'JJ', 'JJR', 'JJS', 'NN', 'NNS', 'NNP', 'NNPS', 'RB', 'RBR', 'RBS']
for i in range(len(tokens)):
    for j in range(len(tokens[i])):
        tagged = nltk.pos_tag(tokens[i][j])
        labeled_annotation[i][j][1] = []
        for k in range(len(tagged)):
            if tagged[k][1] in list_of_part_of_speech_tags:
                labeled_annotation[i][j][1].append(tagged[k][0])

print('Пример очищенного датасета')
print(labeled_annotation[0][0])

# сохранение очищенного датасета
path_to_save = 'D:\programs\diplom\program\data\dataset.txt'
file = open(path_to_save, 'w', encoding = 'utf-8')
for i in range(len(labeled_annotation)):
    for j in range(len(labeled_annotation[i])):
        file.write(str(labeled_annotation[i][j][0]) + '\t')
        for k in range(len(labeled_annotation[i][j][1])):
            file.write(labeled_annotation[i][j][1][k] + ' ')
        file.write('\n')
file.close()
# облако слов
print('\nПостроение облака слов')
all_words = []
for i in range(len(labeled_annotation)):
    all_words.append('')
    for j in range(len(labeled_annotation[i])):
        for k in range(len(labeled_annotation[i][j][1])):
            all_words[i] += ' ' + labeled_annotation[i][j][1][k]

    all_words[i] = all_words[i].strip()

plt.figure(figsize = [15,10])

for i in range(len(all_words)):
    procWordCloud = get_wordCloud(all_words[i])
    plt.subplot(3, 3, i+1)
    plt.title(classes[i])
    plt.imshow(procWordCloud)

plt.axis('off')
plt.show()