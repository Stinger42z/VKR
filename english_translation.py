from deep_translator import GoogleTranslator

print('\nСбор аннотаций...')
classes = ['Физика', 'Химия', 'Математика', 'Биология и фундаментальная медицина', 'Экономика и управление', 'Строительство и архитектура', 'IT технологии и электроника']

labeled_annotation = []
for i in range(len(classes)):
    labeled_annotation.append([])
    path_to_annotation = 'D:\\programs\\diplom\program\\finished_text\\Proceedings_vol_' + str(i + 1) + 'test.txt'
    current_annotations = open(path_to_annotation, 'r', encoding = 'utf-8').readlines()
    print('\tОбработка аннотаций ' + str(i + 1))
    for k in range(len(current_annotations)):
        labeled_annotation[i].append(current_annotations[k].split('\t')[1].split('\n')[0])


# English translation
print('\nПеревод русского текста на английский...')
for i in range(len(labeled_annotation)):
    for j in range(len(labeled_annotation[i])):
        labeled_annotation[i][j] = GoogleTranslator(source = 'auto', target = 'en').translate(labeled_annotation[i][j])

print('\nСохранение в файл...')
for i in range(len(labeled_annotation)):
    path_to_save_tranlated_labeled_annotation = 'D:\\programs\\diplom\program\\translated_finished_text\\translated_finished_text_class_' + str(i + 1) + '.txt'
    save_tranlated_labeled_annotation = open(path_to_save_tranlated_labeled_annotation, 'w', encoding = 'utf-8')
    for j in range(len(labeled_annotation[i])):
        save_tranlated_labeled_annotation.write(labeled_annotation[i][j])
        save_tranlated_labeled_annotation.write('\n')

