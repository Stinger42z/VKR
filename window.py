import sys
from PyQt5.QtWidgets import (QWidget, QToolTip,
                            QPushButton, QApplication, QTextEdit, QFileDialog, QMessageBox)
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import QCoreApplication
from classification import classification
import os
from scipy.spatial import distance
from sklearn.feature_extraction.text import TfidfVectorizer

class Example(QWidget):
    
    def __init__(self):
        super().__init__()

        self.initUI()

    def button1(self):
        self.text = self.textbox.toPlainText()
        self.textbox.clear()
        classes = ['Физика', 'Химия', 'Математика', 'Биология и фундаментальная медицина', 'Экономика и управление', 'Строительство и архитектура', 'IT технологии и электроника']
        path_to_save_sgd = str(os.getcwd()) + '\\result_sgd.txt'
        path_to_save_knb = str(os.getcwd()) + '\\result_knb.txt'
        path_to_save_lr = str(os.getcwd()) + '\\result_lr.txt'
        predicted_sgd = sgd_ppl_clf.predict([self.text])
        predicted_knb = knb_ppl_clf.predict([self.text])
        predicted_lr = lr_ppl_clf.predict([self.text])
        f = open(path_to_save_sgd, 'w', encoding = 'utf-8')
        f.write(str(classes[predicted_sgd[0]-1]) + '\t' + self.text)
        f.close()

        f = open(path_to_save_knb, 'w', encoding = 'utf-8')
        f.write(str(classes[predicted_knb[0]-1]) + '\t' + self.text)
        f.close()

        f = open(path_to_save_lr, 'w', encoding = 'utf-8')
        f.write(str(classes[predicted_lr[0]-1]) + '\t' + self.text)
        f.close()

        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setStyleSheet("QLabel{min-width: 60px;}")
        msgBox.setText("Done")
        msgBox.setWindowTitle("Done")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec()

    def button2(self):
        path = QFileDialog.getOpenFileName(self, 'Open File', './', 'Text Files (*.txt)')
        f = open(path[0], 'r', encoding = 'utf-8').readlines()
        predicted_sgd = sgd_ppl_clf.predict(f)
        predicted_knb = knb_ppl_clf.predict(f)
        predicted_lr = lr_ppl_clf.predict(f)
        
        y = predicted_sgd
        f_by_classes = [[], [], [], [], [], [], []]
        for i in range(len(y)):
            f_by_classes[y[i] - 1].append(f[i])
        
        vectorizer = TfidfVectorizer()
        for i in range(len(f_by_classes)):
            cur = vectorizer.fit_transform(f_by_classes[i]).toarray()
            for k in range(len(f_by_classes[i]) - 2):
                dist = []
                for j in range(k + 1, len(f_by_classes[i])):
                    dist.append(distance.cosine(cur[k], cur[j]))
                
                pos = dist.index(min(dist)) + 1
                f_by_classes[i][pos], f_by_classes[i][k + 1] = f_by_classes[i][k + 1], f_by_classes[i][pos]
                cur[pos], cur[k + 1] = cur[k + 1], cur[pos]

        y = predicted_knb
        f_by_classes_1 = [[], [], [], [], [], [], []]
        for i in range(len(y)):
            f_by_classes_1[y[i] - 1].append(f[i])
        
        vectorizer = TfidfVectorizer()
        for i in range(len(f_by_classes_1)):
            cur = vectorizer.fit_transform(f_by_classes_1[i]).toarray()
            for k in range(len(f_by_classes_1[i]) - 2):
                dist = []
                for j in range(k + 1, len(f_by_classes_1[i])):
                    dist.append(distance.cosine(cur[k], cur[j]))
                
                pos = dist.index(min(dist)) + 1
                f_by_classes_1[i][pos], f_by_classes_1[i][k + 1] = f_by_classes_1[i][k + 1], f_by_classes_1[i][pos]
                cur[pos], cur[k + 1] = cur[k + 1], cur[pos]

        y = predicted_lr
        f_by_classes_2 = [[], [], [], [], [], [], []]
        for i in range(len(y)):
            f_by_classes_2[y[i] - 1].append(f[i])

        vectorizer = TfidfVectorizer()
        for i in range(len(f_by_classes_2)):
            cur = vectorizer.fit_transform(f_by_classes_2[i]).toarray()
            for k in range(len(f_by_classes_2[i]) - 2):
                dist = []
                for j in range(k + 1, len(f_by_classes_2[i])):
                    dist.append(distance.cosine(cur[k], cur[j]))
                
                pos = dist.index(min(dist)) + 1
                f_by_classes_2[i][pos], f_by_classes_2[i][k + 1] = f_by_classes_2[i][k + 1], f_by_classes_2[i][pos]
                cur[pos], cur[k + 1] = cur[k + 1], cur[pos]
        
        path_to_save_sgd = str(os.getcwd()) + '\\result_sgd.txt'
        path_to_save_knb = str(os.getcwd()) + '\\result_knb.txt'
        path_to_save_lr = str(os.getcwd()) + '\\result_lr.txt'
        classes = ['Физика', 'Химия', 'Математика', 'Биология и фундаментальная медицина', 'Экономика и управление', 'Строительство и архитектура', 'IT технологии и электроника']
        f2 = open(path_to_save_sgd, 'w', encoding = 'utf-8')
        for i in range(len(f_by_classes)):
            for j in range(len(f_by_classes[i])):
                f2.write(str(classes[i]) + '\t' + f_by_classes[i][j])

        f2.close()

        f2 = open(path_to_save_knb, 'w', encoding = 'utf-8')
        for i in range(len(f_by_classes_1)):
            for j in range(len(f_by_classes_1[i])):
                f2.write(str(classes[i]) + '\t' + f_by_classes_1[i][j])
        
        f2.close()

        f2 = open(path_to_save_lr, 'w', encoding = 'utf-8')
        for i in range(len(f_by_classes_2)):
            for j in range(len(f_by_classes_2[i])):
                f2.write(str(classes[i]) + '\t' + f_by_classes_2[i][j])
        
        f2.close()

        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setStyleSheet("QLabel{min-width: 60px;}")
        msgBox.setText("Done")
        msgBox.setWindowTitle("Done")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec()

    def initUI(self):

        QToolTip.setFont(QFont('SansSerif', 10))

        self.setToolTip('This is a <b>QWidget</b> widget')

        self.textbox = QTextEdit(self)
        self.textbox.setPlaceholderText('Введите аннотацию...')
        self.textbox.resize(500, 100)
        self.textbox.move(50, 20)

        self.btn1 = QPushButton('Go', self)
        self.btn1.setToolTip('This is a <b>QPushButton</b> widget')
        self.btn1.resize(80, 20)
        self.btn1.move(260, 130)
        self.btn1.clicked.connect(self.button1)
        

        self.btn2 = QPushButton('Attach file', self)
        self.btn2.setToolTip('This is a <b>QPushButton</b> widget')
        self.btn2.resize(160, 40)
        self.btn2.move(220, 300)
        self.btn2.clicked.connect(self.button2)
        
        self.setGeometry(660, 240, 600, 500)
        self.setWindowTitle('my_program')
        self.setWindowIcon(QIcon('icon.png'))
        self.show()

if __name__ == '__main__':
    sgd_ppl_clf, knb_ppl_clf, lr_ppl_clf = classification(str(os.getcwd()) + '\\x_test.txt', str(os.getcwd()) + '\\y_test.txt')
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())