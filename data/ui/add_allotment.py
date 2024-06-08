# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_allotmentXIXSFb.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QGridLayout, QLabel, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(320, 373)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.aAllotmentWidget = QWidget(Dialog)
        self.aAllotmentWidget.setObjectName(u"aAllotmentWidget")
        self.aAllotmentWidget.setMaximumSize(QSize(360, 450))
        self.aAllotmentWidget.setStyleSheet(u"*{\n"
"	border: none;\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#aATitle, #aAUniversity, #aACourse, #aASemester, #aASubject, #aAExamDate, #aAAddtBtn{\n"
"	margin: 10px;\n"
"}\n"
"\n"
"#aATitle{\n"
"	font: 700 20pt \"Calibri\";	\n"
"	color: rgba(0,0,0,200);\n"
"}\n"
"\n"
"#aAUniversity, #aACourse, #aASemester, #aASubject, #aAExamDate{\n"
"	font: 700 13pt \"Calibri\";\n"
"	background-color: rgba(0,0,0,0);\n"
"	border:none;\n"
"	border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"	color: rgba(0,0,0,240);\n"
"}\n"
"\n"
"#aAAddBtn{\n"
"	text-align: center;\n"
"	font: 700 13pt \"Calibri\";\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255,255,255,210);\n"
"	border-radius:5px;\n"
"}\n"
"\n"
"#aAAddBtn:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"\n"
"#aAAddBtn:pressed{\n"
"	padding-lef"
                        "t:5px;\n"
"	padding-top:5px;\n"
"	backbground-color: rgba(150,123,111,255);\n"
"}")
        self.verticalLayout = QVBoxLayout(self.aAllotmentWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.aATitle = QLabel(self.aAllotmentWidget)
        self.aATitle.setObjectName(u"aATitle")
        self.aATitle.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.aATitle, 0, Qt.AlignTop)

        self.aAllotmentFrm = QFrame(self.aAllotmentWidget)
        self.aAllotmentFrm.setObjectName(u"aAllotmentFrm")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aAllotmentFrm.sizePolicy().hasHeightForWidth())
        self.aAllotmentFrm.setSizePolicy(sizePolicy)
        self.aAllotmentFrm.setMinimumSize(QSize(320, 320))
        self.aAllotmentFrm.setFrameShape(QFrame.StyledPanel)
        self.aAllotmentFrm.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.aAllotmentFrm)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.aAUniversity = QComboBox(self.aAllotmentFrm)
        self.aAUniversity.addItem("")
        self.aAUniversity.setObjectName(u"aAUniversity")

        self.verticalLayout_2.addWidget(self.aAUniversity)

        self.aACourse = QComboBox(self.aAllotmentFrm)
        self.aACourse.addItem("")
        self.aACourse.setObjectName(u"aACourse")

        self.verticalLayout_2.addWidget(self.aACourse)

        self.aASemester = QComboBox(self.aAllotmentFrm)
        self.aASemester.addItem("")
        self.aASemester.setObjectName(u"aASemester")

        self.verticalLayout_2.addWidget(self.aASemester)

        self.aASubject = QComboBox(self.aAllotmentFrm)
        self.aASubject.addItem("")
        self.aASubject.setObjectName(u"aASubject")

        self.verticalLayout_2.addWidget(self.aASubject)

        self.aAAddBtn = QPushButton(self.aAllotmentFrm)
        self.aAAddBtn.setObjectName(u"aAAddBtn")
        self.aAAddBtn.setMinimumSize(QSize(120, 50))

        self.verticalLayout_2.addWidget(self.aAAddBtn, 0, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.aAllotmentFrm)


        self.gridLayout.addWidget(self.aAllotmentWidget, 0, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.aATitle.setText(QCoreApplication.translate("Dialog", u"Allotment of subject", None))
        self.aAUniversity.setItemText(0, QCoreApplication.translate("Dialog", u"Select University", None))

        self.aACourse.setItemText(0, QCoreApplication.translate("Dialog", u"Select Course", None))

        self.aASemester.setItemText(0, QCoreApplication.translate("Dialog", u"Select Semster", None))

        self.aASubject.setItemText(0, QCoreApplication.translate("Dialog", u"Select Subject", None))

        self.aAAddBtn.setText(QCoreApplication.translate("Dialog", u"Submit", None))
    # retranslateUi

