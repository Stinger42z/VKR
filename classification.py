def classification(path_x_test, path_y_test):
    from sklearn.pipeline import Pipeline
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.linear_model import SGDClassifier, LogisticRegression
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.model_selection import train_test_split
    '''
    from sklearn import metrics
    from sklearn.model_selection import GridSearchCV
    from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
    import matplotlib.pyplot as plt
    from sklearn.metrics.pairwise import euclidean_distances
    from copy import deepcopy
    from wordcloud import WordCloud, STOPWORDS
    '''
    labeled_annotation = [[], [], [], [], [], [], []]
    path_to_dataset = 'dataset.txt'
    file = open(path_to_dataset, 'r', encoding = 'utf-8').readlines()
    for i in file:
        row = i.split('\t')
        if row[0] == '1':
            labeled_annotation[0].append([1, row[1]])
        elif row[0] == '2':
            labeled_annotation[1].append([2, row[1]])
        elif row[0] == '3':
            labeled_annotation[2].append([3, row[1]])
        elif row[0] == '4':
            labeled_annotation[3].append([4, row[1]])
        elif row[0] == '5':
            labeled_annotation[4].append([5, row[1]])
        elif row[0] == '6':
            labeled_annotation[5].append([6, row[1]])
        elif row[0] == '7':
            labeled_annotation[6].append([7, row[1]])

    x_all = []
    y_all = []

    for i in range(len(labeled_annotation)):
        for j in range(len(labeled_annotation[i])):
            x_all.append(labeled_annotation[i][j][1])
            y_all.append(labeled_annotation[i][j][0])

    x_train, x_test, y_train, y_test = train_test_split(x_all, y_all, test_size = 0.2, random_state = 42)
    # надо сделать выгрузку x_test и y_test
    file = open(path_x_test, 'w', encoding = 'utf-8').writelines(x_test)

    for i in range(len(y_test)):
        y_test[i] = str(y_test[i]) + '\n'

    file = open(path_y_test, 'w', encoding = 'utf-8').writelines(y_test)

    sgd_ppl_clf = Pipeline([
                            ('tfidf', TfidfVectorizer()),
                            ('sgd_clf', SGDClassifier(max_iter = 100, random_state = 42))])

    sgd_ppl_clf.fit(x_train, y_train)
    
    knb_ppl_clf = Pipeline([
                            ('tfidf', TfidfVectorizer()),
                            ('knb_clf', KNeighborsClassifier(n_neighbors = 10))])

    knb_ppl_clf.fit(x_train, y_train)

    lr_ppl_clf = Pipeline([
                            ('tfidf', TfidfVectorizer()),
                            ('sgd_clf', LogisticRegression(max_iter = 1000, random_state = 42))])

    lr_ppl_clf.fit(x_train, y_train)

    return sgd_ppl_clf, knb_ppl_clf, lr_ppl_clf