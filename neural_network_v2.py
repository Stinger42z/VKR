def classification():

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import SGDClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import euclidean_distances
from copy import deepcopy
from wordcloud import WordCloud, STOPWORDS


# создание тренировочной (80%) и тестовой (20%) выборок
print('\nРазбиение на тренировочную(80%) и тестовую(20%) части...')
x_all = []
y_all = []

for i in range(len(labeled_annotation)):
    for j in range(len(labeled_annotation[i])):
        x_all.append(labeled_annotation[i][j][1])
        y_all.append(labeled_annotation[i][j][0])

for i, l in enumerate(x_all):
    x_all[i] = " ".join(l)

x_train, x_test, y_train, y_test = train_test_split(x_all, y_all, test_size = 0.2, random_state = 42)

# модель линейной классификации
print('\nЛинейная классификация...')
sgd_ppl_clf = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('sgd_clf', SGDClassifier(max_iter = 100, random_state = 42))])

sgd_ppl_clf.fit(x_train, y_train)

# оценка полученных результатов
print('\tОценка полученных результатов')
predicted_sgd = sgd_ppl_clf.predict(x_test)
print(metrics.classification_report(predicted_sgd, y_test))

# confusion matrix
conf_matr = confusion_matrix(y_test, predicted_sgd, labels = [1, 2, 3, 4, 5, 6, 7], normalize = 'pred')
disp = ConfusionMatrixDisplay(confusion_matrix = conf_matr, display_labels = [1, 2, 3, 4, 5, 6, 7])
disp.plot()
plt.show()

'''
# test
print('\nTest')
vectrorizer = TfidfVectorizer()
x_all = vectrorizer.fit_transform(x_all)

x_train, x_test, y_train, y_test = train_test_split(x_all, y_all, test_size = 0.2, random_state = 42)

SGD_clf = SGDClassifier(random_state = 42)
SGD_clf.fit(x_train, y_train)

predicted_sgd = SGD_clf.predict(x_test)
print(metrics.classification_report(predicted_sgd, y_test))
'''

# модель классификации методом ближайших соседей
print('\nКлассификация методом ближайших средних...')
knb_ppl_clf = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('knb_clf', KNeighborsClassifier(n_neighbors = 10))])

knb_ppl_clf.fit(x_train, y_train)

# оценка полученных результатов
print('\tОценка полученных результатов')
predicted_knb = knb_ppl_clf.predict(x_test)
print(metrics.classification_report(predicted_knb, y_test))

# confusion matrix
conf_matr = confusion_matrix(y_test, predicted_knb, labels = [1, 2, 3, 4, 5, 6, 7])
disp = ConfusionMatrixDisplay(confusion_matrix = conf_matr, display_labels = [1, 2, 3, 4, 5, 6, 7])
disp.plot()
plt.show()

# сортировка внутри секции
print('\nСортировка внутри секций...')
x = x_test
y = predicted_sgd

arg_sort = sorted(range(len(y)), key = lambda i: y[i])

x = [x[i] for i in arg_sort]
y = [y[i] for i in arg_sort]

labeled_data = []
x_by_classes = []
q = 0
w = 0
number_of_classes = 7
while w < number_of_classes:
    labeled_data.append([])
    x_by_classes.append([])
    while q < len(y) and y[q] == w + 1:
        labeled_data[w].append([y[q], x[q]])
        x_by_classes[w].append(x[q])
        q += 1

    w += 1

vectorizer = TfidfVectorizer()

x_by_classes_old = deepcopy(x_by_classes)

for i in range(len(x_by_classes)):
    x_by_classes_vectorized = vectorizer.fit_transform(x_by_classes[i])
    for k in range(len(x_by_classes[i]) - 2):
        dist = []
        for j in range(k + 1, len(x_by_classes[i])):
                dist.append(euclidean_distances(x_by_classes_vectorized[k], x_by_classes_vectorized[j])[0][0])

        pos = dist.index(min(dist)) + 1
        x_by_classes[i][pos], x_by_classes[i][k + 1] = x_by_classes[i][k + 1], x_by_classes[i][pos]
        x_by_classes_vectorized[pos], x_by_classes_vectorized[k + 1] = x_by_classes_vectorized[k + 1], x_by_classes_vectorized[pos]

# сортировка среди всех докладов
