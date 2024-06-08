# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_journeyOMjbuE.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDialog,
    QFrame, QLabel, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(370, 350)
        Dialog.setMaximumSize(QSize(370, 350))
        Dialog.setStyleSheet(u"*{\n"
"	color: #000;\n"
"	background-color: #fff;\n"
"	font: 14pt \"Calibri\";\n"
"}\n"
"\n"
"QPushButton{\n"
"	padding: 5px;\n"
"}\n"
"\n"
"#aJTitle{\n"
"	font: 700 42pt \"Calibri\";\n"
"}\n"
"\n"
"#aJourneyFrm{\n"
"	padding: 10px;\n"
"	border-radius: 10px;\n"
"	border: 2px solid black;\n"
"	background-color: rgba(179, 196, 216, 120);\n"
"}\n"
"\n"
"\n"
"#aJPlace, #aJDate, #aJShift{\n"
"	border:none;\n"
"	background-color: rgba(179, 196, 216, 0);\n"
"	border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"	color: rgba(0,0,0,240);\n"
"}\n"
"\n"
"#aJSubmitBtn{\n"
"	border: none;\n"
"	margin-top: 10px;\n"
"	padding-left: 15px;\n"
"	background-color: rgba(179, 196, 216);\n"
"}\n"
"\n"
"#aJSubmitBtn:hover{\n"
"	background-color: rgba(179, 196, 216, 160);\n"
"	padding: 5px, 0px;\n"
"	border-top-left-radius: 10px;\n"
"}\n"
"\n"
"#aJSubmitBtn:pressed{\n"
"	background-color: rgba(179, 196, 216, 255);\n"
"	padding: 5px, 0px;\n"
"	border-top-left-radius: 10px;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.aJTitle = QLabel(Dialog)
        self.aJTitle.setObjectName(u"aJTitle")
        self.aJTitle.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.aJTitle, 0, Qt.AlignTop)

        self.aJourneyFrm = QFrame(Dialog)
        self.aJourneyFrm.setObjectName(u"aJourneyFrm")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aJourneyFrm.sizePolicy().hasHeightForWidth())
        self.aJourneyFrm.setSizePolicy(sizePolicy)
        self.aJourneyFrm.setMaximumSize(QSize(350, 250))
        self.aJourneyFrm.setFrameShape(QFrame.StyledPanel)
        self.aJourneyFrm.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.aJourneyFrm)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.aJPlace = QComboBox(self.aJourneyFrm)
        self.aJPlace.setObjectName(u"aJPlace")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.aJPlace.sizePolicy().hasHeightForWidth())
        self.aJPlace.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.aJPlace)

        self.aJDate = QDateEdit(self.aJourneyFrm)
        self.aJDate.setObjectName(u"aJDate")
        sizePolicy1.setHeightForWidth(self.aJDate.sizePolicy().hasHeightForWidth())
        self.aJDate.setSizePolicy(sizePolicy1)
        self.aJDate.setDateTime(QDateTime(QDate(1999, 12, 31), QTime(0, 0, 0)))
        self.aJDate.setCalendarPopup(True)

        self.verticalLayout.addWidget(self.aJDate)

        self.aJShift = QComboBox(self.aJourneyFrm)
        self.aJShift.addItem("")
        self.aJShift.addItem("")
        self.aJShift.addItem("")
        self.aJShift.setObjectName(u"aJShift")
        sizePolicy1.setHeightForWidth(self.aJShift.sizePolicy().hasHeightForWidth())
        self.aJShift.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.aJShift)

        self.aJSubmitBtn = QPushButton(self.aJourneyFrm)
        self.aJSubmitBtn.setObjectName(u"aJSubmitBtn")
        sizePolicy1.setHeightForWidth(self.aJSubmitBtn.sizePolicy().hasHeightForWidth())
        self.aJSubmitBtn.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.aJSubmitBtn, 0, Qt.AlignHCenter)


        self.verticalLayout_2.addWidget(self.aJourneyFrm)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.aJTitle.setText(QCoreApplication.translate("Dialog", u"Create Journey", None))
        self.aJDate.setDisplayFormat(QCoreApplication.translate("Dialog", u"yyyy-MM-dd", None))
        self.aJShift.setItemText(0, QCoreApplication.translate("Dialog", u"Select Shift", None))
        self.aJShift.setItemText(1, QCoreApplication.translate("Dialog", u"Morning", None))
        self.aJShift.setItemText(2, QCoreApplication.translate("Dialog", u"Afternoon", None))

        self.aJSubmitBtn.setText(QCoreApplication.translate("Dialog", u"Submit", None))
    # retranslateUi

