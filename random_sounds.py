import pygame
from random import choice
import os
from PyQt5 import QtCore, QtGui, QtWidgets

A = 0
nazv = ''
koordinat = [[[250, 200]],
             [[250, 130], [250, 240]],
             [[250, 140], [100, 130], [400, 130]],
             [[100, 130], [400, 130], [100, 220], [400, 220]],
             [[250, 250], [400, 160], [100, 160], [400, 70], [100, 70]],
             [[100, 70], [400, 70], [100, 160], [400, 160], [100, 250], [400, 250]],
             [[250, 310], [100, 220], [400, 220], [100, 130], [400, 130], [100, 40], [400, 40]],
             [[100, 40], [400, 40], [100, 130], [400, 130], [100, 220], [400, 220], [100, 310], [400, 310]],
             [[250, 300], [100, 230], [400, 230], [100, 160], [400, 160], [100, 90], [400, 90], [100, 20], [400, 20]],
             [[100, 20], [400, 20], [100, 90], [400, 90], [100, 160], [400, 160], [100, 230], [400, 230], [100, 300], [400, 300]]
             ]

directory = "."
files = os.listdir(directory)
files_2 = []
for i in files:
    if os.path.isdir(i) and i != '.idea':
        files_2.append(i)

myz = []
for l in files_2:
    myz0 = []
    directory = f"./{l}"
    files = os.listdir(directory)
    for j in files:
        if ('.mp3' in j) or ('.wav' in j):
            myz0.append(j)
    if len(myz0) != 0 and len(myz) < 10:
        myz.append([l, myz0])


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(750, 500)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        font_1, font_2, font_3 = QtGui.QFont(), QtGui.QFont(), QtGui.QFont()
        spisok_font = [[font_1, 14, True], [font_2, 7, True], [font_3, 12, False]]
        for i in range(len(spisok_font)):
            spisok_font[i][0].setFamily("Segoe Print")
            spisok_font[i][0].setPointSize(spisok_font[i][1])
            spisok_font[i][0].setBold(spisok_font[i][2])
            spisok_font[i][0].setWeight(75)

        self.pushButton_stop = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_stop.setGeometry(QtCore.QRect(300, 430, 150, 50))
        self.pushButton_stop.setFont(font_1)
        self.pushButton_stop.clicked.connect(kn_stop)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(610, 460, 130, 20))
        self.label.setFont(font_2)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(175, 380, 400, 40))
        self.label_2.setFont(font_3)
        self.spis_kno = []
        for i, l in enumerate(myz):
            self.pushButton = QtWidgets.QPushButton(self.centralwidget)
            self.pushButton.setGeometry(QtCore.QRect(koordinat[len(myz)-1][i][0], koordinat[len(myz)-1][i][1], 250, 50))
            self.pushButton.setFont(font_1)
            if A == i+1:
                self.pushButton.setStyleSheet("background-color: green")

            if i == 0:
                self.pushButton.clicked.connect(lambda: kn_plai(0))
            elif i == 1:
                self.pushButton.clicked.connect(lambda: kn_plai(1))
            elif i == 2:
                self.pushButton.clicked.connect(lambda: kn_plai(2))
            elif i == 3:
                self.pushButton.clicked.connect(lambda: kn_plai(3))
            elif i == 4:
                self.pushButton.clicked.connect(lambda: kn_plai(4))
            elif i == 5:
                self.pushButton.clicked.connect(lambda: kn_plai(5))
            elif i == 6:
                self.pushButton.clicked.connect(lambda: kn_plai(6))
            elif i == 7:
                self.pushButton.clicked.connect(lambda: kn_plai(7))
            elif i == 8:
                self.pushButton.clicked.connect(lambda: kn_plai(8))
            elif i == 9:
                self.pushButton.clicked.connect(lambda: kn_plai(9))

            self.spis_kno.append([l[0], self.pushButton])


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 750, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_stop.setText(_translate("MainWindow", "стоп"))
        for i in self.spis_kno:
            i[1].setText(_translate("MainWindow", i[0]))
        self.label.setText(_translate("MainWindow", "разработчик: Тарасов Д.Л."))
        self.label_2.setText(_translate("MainWindow", nazv))

def kn_stop():
    global A, nazv
    if A != 0:
        pygame.mixer.music.stop()
        A = 0
    nazv = ''
    ui.setupUi(MainWindow)

def kn_plai(a):
    global A, nazv
    A = a + 1
    spisok = myz[a][1]
    m = choice(spisok)
    nazv = otrez_tip(str(m))
    pygame.mixer.init()
    pygame.mixer.music.load(f'./{myz[a][0]}/{m}')
    pygame.mixer.music.play()
    ui.setupUi(MainWindow)

def otrez_tip(a):
    a1 = ''
    for i in a:
        if i != '.':
            a1 += i
        else:
            return a1
    return a1



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
