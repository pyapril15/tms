# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'exam_detailKzCHIi.ui'
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
        Dialog.resize(330, 443)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.aExamDetailWidget = QWidget(Dialog)
        self.aExamDetailWidget.setObjectName(u"aExamDetailWidget")
        self.aExamDetailWidget.setMaximumSize(QSize(360, 450))
        self.aExamDetailWidget.setStyleSheet(u"*{\n"
"	border: none;\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#aEDTitle, #aEDUniversity, #aEDCourse, #aEDSemester, #aEDCenter, #aEDShift, #aEDExamIsActive, #aEDAddtBtn{\n"
"	margin: 10px;\n"
"}\n"
"\n"
"#aEDTitle{\n"
"	font: 700 20pt \"Calibri\";	\n"
"	color: rgba(0,0,0,200);\n"
"}\n"
"\n"
"#aEDUniversity, #aEDCourse, #aEDSemester, #aEDCenter, #aEDShift, #aEDExamIsActive{\n"
"	font: 700 13pt \"Calibri\";\n"
"	background-color: rgba(0,0,0,0);\n"
"	border:none;\n"
"	border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"	color: rgba(0,0,0,240);\n"
"}\n"
"\n"
"#aEDAddBtn{\n"
"	text-align: center;\n"
"	font: 700 13pt \"Calibri\";\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255,255,255,210);\n"
"	border-radius:5px;\n"
"}\n"
"\n"
"#aEDAddBtn:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
""
                        "\n"
"#aEDAddBtn:pressed{\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	backbground-color: rgba(150,123,111,255);\n"
"}")
        self.verticalLayout = QVBoxLayout(self.aExamDetailWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.aEDTitle = QLabel(self.aExamDetailWidget)
        self.aEDTitle.setObjectName(u"aEDTitle")
        self.aEDTitle.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.aEDTitle, 0, Qt.AlignTop)

        self.aExamDetailFrm = QFrame(self.aExamDetailWidget)
        self.aExamDetailFrm.setObjectName(u"aExamDetailFrm")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aExamDetailFrm.sizePolicy().hasHeightForWidth())
        self.aExamDetailFrm.setSizePolicy(sizePolicy)
        self.aExamDetailFrm.setMinimumSize(QSize(330, 390))
        self.aExamDetailFrm.setFrameShape(QFrame.StyledPanel)
        self.aExamDetailFrm.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.aExamDetailFrm)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.aEDUniversity = QComboBox(self.aExamDetailFrm)
        self.aEDUniversity.addItem("")
        self.aEDUniversity.setObjectName(u"aEDUniversity")

        self.verticalLayout_2.addWidget(self.aEDUniversity)

        self.aEDCourse = QComboBox(self.aExamDetailFrm)
        self.aEDCourse.addItem("")
        self.aEDCourse.setObjectName(u"aEDCourse")

        self.verticalLayout_2.addWidget(self.aEDCourse)

        self.aEDSemester = QComboBox(self.aExamDetailFrm)
        self.aEDSemester.addItem("")
        self.aEDSemester.setObjectName(u"aEDSemester")

        self.verticalLayout_2.addWidget(self.aEDSemester)

        self.aEDCenter = QComboBox(self.aExamDetailFrm)
        self.aEDCenter.addItem("")
        self.aEDCenter.setObjectName(u"aEDCenter")

        self.verticalLayout_2.addWidget(self.aEDCenter)

        self.aEDShift = QComboBox(self.aExamDetailFrm)
        self.aEDShift.addItem("")
        self.aEDShift.addItem("")
        self.aEDShift.addItem("")
        self.aEDShift.setObjectName(u"aEDShift")

        self.verticalLayout_2.addWidget(self.aEDShift)

        self.aEDAddBtn = QPushButton(self.aExamDetailFrm)
        self.aEDAddBtn.setObjectName(u"aEDAddBtn")
        self.aEDAddBtn.setMinimumSize(QSize(120, 50))

        self.verticalLayout_2.addWidget(self.aEDAddBtn, 0, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.aExamDetailFrm)


        self.gridLayout.addWidget(self.aExamDetailWidget, 0, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.aEDTitle.setText(QCoreApplication.translate("Dialog", u"Exam Detail", None))
        self.aEDUniversity.setItemText(0, QCoreApplication.translate("Dialog", u"Select University", None))

        self.aEDCourse.setItemText(0, QCoreApplication.translate("Dialog", u"Select Course", None))

        self.aEDSemester.setItemText(0, QCoreApplication.translate("Dialog", u"Select Semster", None))

        self.aEDCenter.setItemText(0, QCoreApplication.translate("Dialog", u"Select Center", None))

        self.aEDShift.setItemText(0, QCoreApplication.translate("Dialog", u"Select Shift", None))
        self.aEDShift.setItemText(1, QCoreApplication.translate("Dialog", u"Morning", None))
        self.aEDShift.setItemText(2, QCoreApplication.translate("Dialog", u"Afternoon", None))

        self.aEDAddBtn.setText(QCoreApplication.translate("Dialog", u"Submit", None))
    # retranslateUi

