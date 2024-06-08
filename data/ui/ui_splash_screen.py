# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splash_screenFlLepn.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QMainWindow, QSizePolicy, QVBoxLayout, QWidget)

class Ui_splashScreen(object):
    def setupUi(self, splashScreen):
        if not splashScreen.objectName():
            splashScreen.setObjectName(u"splashScreen")
        splashScreen.resize(340, 340)
        splashScreen.setMinimumSize(QSize(340, 340))
        splashScreen.setMaximumSize(QSize(340, 340))
        self.centralwidget = QWidget(splashScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.circularProgressBar = QFrame(self.centralwidget)
        self.circularProgressBar.setObjectName(u"circularProgressBar")
        self.circularProgressBar.setGeometry(QRect(10, 10, 320, 320))
        self.circularProgressBar.setMinimumSize(QSize(320, 0))
        self.circularProgressBar.setFrameShape(QFrame.NoFrame)
        self.circularProgressBar.setFrameShadow(QFrame.Raised)
        self.circularProgress = QFrame(self.circularProgressBar)
        self.circularProgress.setObjectName(u"circularProgress")
        self.circularProgress.setGeometry(QRect(10, 10, 300, 300))
        self.circularProgress.setMinimumSize(QSize(300, 300))
        self.circularProgress.setStyleSheet(u"QFrame{\n"
"	border-radius: 150px;\n"
"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.749 rgba(255, 0, 127, 0), stop:0.750 rgba(85, 170, 255, 255));\n"
"}")
        self.circularProgress.setFrameShape(QFrame.NoFrame)
        self.circularProgress.setFrameShadow(QFrame.Raised)
        self.circularBg = QFrame(self.circularProgressBar)
        self.circularBg.setObjectName(u"circularBg")
        self.circularBg.setGeometry(QRect(10, 10, 300, 300))
        self.circularBg.setStyleSheet(u"QFrame{\n"
"	border-radius: 150px;\n"
"	background-color: rgba(77, 77, 127, 120);\n"
"}")
        self.circularBg.setFrameShape(QFrame.NoFrame)
        self.circularBg.setFrameShadow(QFrame.Raised)
        self.container = QFrame(self.circularProgressBar)
        self.container.setObjectName(u"container")
        self.container.setGeometry(QRect(25, 25, 270, 270))
        self.container.setMinimumSize(QSize(270, 270))
        self.container.setStyleSheet(u"QFrame{\n"
"	border-radius: 135px;\n"
"	background-color: rgb(77, 77, 127);\n"
"}")
        self.container.setFrameShape(QFrame.NoFrame)
        self.container.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.container)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, 30, 0, 10)
        self.title = QLabel(self.container)
        self.title.setObjectName(u"title")
        self.title.setMinimumSize(QSize(0, 40))
        font = QFont()
        font.setPointSize(12)
        self.title.setFont(font)
        self.title.setStyleSheet(u"margin-top: 5px;\n"
"background-color: none;\n"
"color: rgb(255, 255, 255);")
        self.title.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.title, 0, 0, 1, 1)

        self.percentage = QLabel(self.container)
        self.percentage.setObjectName(u"percentage")
        font1 = QFont()
        font1.setFamilies([u"Rockwell"])
        font1.setPointSize(68)
        self.percentage.setFont(font1)
        self.percentage.setStyleSheet(u"background-color: none;\n"
"color: rgb(255, 255, 255);")
        self.percentage.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.percentage, 1, 0, 1, 1)

        self.loading = QLabel(self.container)
        self.loading.setObjectName(u"loading")
        self.loading.setMinimumSize(QSize(100, 20))
        self.loading.setMaximumSize(QSize(100, 20))
        font2 = QFont()
        font2.setPointSize(9)
        self.loading.setFont(font2)
        self.loading.setStyleSheet(u"QLabel{\n"
"	border-radius: 10px;\n"
"	background-color: rgb(93, 93, 154);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.loading.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.loading, 2, 0, 1, 1, Qt.AlignHCenter)

        self.credits = QLabel(self.container)
        self.credits.setObjectName(u"credits")
        self.credits.setFont(font2)
        self.credits.setStyleSheet(u"background-color: none;\n"
"color: rgb(155, 155, 255);")
        self.credits.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.credits, 3, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.circularBg.raise_()
        self.circularProgress.raise_()
        self.container.raise_()
        splashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(splashScreen)

        QMetaObject.connectSlotsByName(splashScreen)
    # setupUi

    def retranslateUi(self, splashScreen):
        splashScreen.setWindowTitle(QCoreApplication.translate("splashScreen", u"MainWindow", None))
        self.title.setText(QCoreApplication.translate("splashScreen", u"<html><head/><body><p><span style=\" font-weight:700; color:#9b9bff;\">Your</span> Application Name</p></body></html>", None))
        self.percentage.setText(QCoreApplication.translate("splashScreen", u"<p><span style=\" font-size:68pt;\">0</span><span style=\" font-size:58pt; vertical-align:super;\">%</span></p>", None))
        self.loading.setText(QCoreApplication.translate("splashScreen", u"Loading....", None))
        self.credits.setText(QCoreApplication.translate("splashScreen", u"-By pyapril15", None))
    # retranslateUi

