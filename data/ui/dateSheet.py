# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dateSheetYzijxb.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(420, 400)
        Form.setMaximumSize(QSize(420, 400))
        Form.setStyleSheet(u"*{\n"
"	color: #000;\n"
"	background-color: #fff;\n"
"	font: 14pt \"Calibri\";\n"
"}\n"
"\n"
"QPushButton{\n"
"	padding: 5px;\n"
"}\n"
"\n"
"#dateSheetTitle{\n"
"	font: 700 42pt \"Calibri\";\n"
"}\n"
"\n"
"#dateSheetTableFrm{\n"
"	margin: 20px;\n"
"	padding: 5px;\n"
"	border-radius: 10px;\n"
"	border: 2px solid black;\n"
"}\n"
"\n"
"#dateSheetSubmitBtn{\n"
"	margin-bottom:10px;\n"
"	border: none;\n"
"	padding-left: 15px;\n"
"	background-color: rgba(179, 196, 216);\n"
"}\n"
"\n"
"#dateSheetSubmitBtn:hover{\n"
"	background-color: rgba(179, 196, 216, 160);\n"
"	padding: 5px, 0px;\n"
"	border-top-left-radius: 10px;\n"
"}\n"
"\n"
"#dateSheetSubmitBtn:pressed{\n"
"	background-color: rgba(179, 196, 216, 255);\n"
"	padding: 5px, 0px;\n"
"	border-top-left-radius: 10px;\n"
"}")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.dateSheetTitle = QLabel(Form)
        self.dateSheetTitle.setObjectName(u"dateSheetTitle")
        self.dateSheetTitle.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.dateSheetTitle)

        self.dateSheetWidget = QWidget(Form)
        self.dateSheetWidget.setObjectName(u"dateSheetWidget")
        self.verticalLayout_2 = QVBoxLayout(self.dateSheetWidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.dateSheetTableFrm = QFrame(self.dateSheetWidget)
        self.dateSheetTableFrm.setObjectName(u"dateSheetTableFrm")
        self.dateSheetTableFrm.setFrameShape(QFrame.StyledPanel)
        self.dateSheetTableFrm.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.dateSheetTableFrm)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.dUniversity = QLabel(self.dateSheetTableFrm)
        self.dUniversity.setObjectName(u"dUniversity")

        self.horizontalLayout.addWidget(self.dUniversity)

        self.dCourse = QLabel(self.dateSheetTableFrm)
        self.dCourse.setObjectName(u"dCourse")

        self.horizontalLayout.addWidget(self.dCourse)

        self.dSemester = QLabel(self.dateSheetTableFrm)
        self.dSemester.setObjectName(u"dSemester")

        self.horizontalLayout.addWidget(self.dSemester)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.dateSheetTable = QTableWidget(self.dateSheetTableFrm)
        if (self.dateSheetTable.columnCount() < 2):
            self.dateSheetTable.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.dateSheetTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.dateSheetTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.dateSheetTable.setObjectName(u"dateSheetTable")
        self.dateSheetTable.setMinimumSize(QSize(360, 200))
        self.dateSheetTable.setAlternatingRowColors(True)
        self.dateSheetTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.dateSheetTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.dateSheetTable.horizontalHeader().setMinimumSectionSize(150)
        self.dateSheetTable.horizontalHeader().setDefaultSectionSize(150)
        self.dateSheetTable.horizontalHeader().setStretchLastSection(True)
        self.dateSheetTable.verticalHeader().setMinimumSectionSize(40)
        self.dateSheetTable.verticalHeader().setDefaultSectionSize(40)

        self.verticalLayout_3.addWidget(self.dateSheetTable)


        self.verticalLayout_2.addWidget(self.dateSheetTableFrm)

        self.dateSheetSubmitBtn = QPushButton(self.dateSheetWidget)
        self.dateSheetSubmitBtn.setObjectName(u"dateSheetSubmitBtn")
        self.dateSheetSubmitBtn.setMinimumSize(QSize(110, 0))

        self.verticalLayout_2.addWidget(self.dateSheetSubmitBtn, 0, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.dateSheetWidget)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.dateSheetTitle.setText(QCoreApplication.translate("Form", u"Datesheet", None))
        self.dUniversity.setText(QCoreApplication.translate("Form", u"University:-", None))
        self.dCourse.setText(QCoreApplication.translate("Form", u"Course:- ", None))
        self.dSemester.setText(QCoreApplication.translate("Form", u"Semester:- ", None))
        ___qtablewidgetitem = self.dateSheetTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Subject Name", None));
        ___qtablewidgetitem1 = self.dateSheetTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Subject Date", None));
        self.dateSheetSubmitBtn.setText(QCoreApplication.translate("Form", u"Submit", None))
    # retranslateUi

