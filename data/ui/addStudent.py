# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addStudentLtecoF.ui'
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
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(518, 473)
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
"#addStudentTitle{\n"
"	font: 700 42pt \"Calibri\";\n"
"}\n"
"\n"
"#aSMainFrm{\n"
"	margin: 20px;\n"
"	padding: 5px;\n"
"	border-radius: 10px;\n"
"	border: 2px solid black;\n"
"	background-color: rgba(179, 196, 216, 120);\n"
"}\n"
"\n"
"#aSSearchFrm{\n"
"	margin: 5px;\n"
"	padding: 5px;\n"
"	border-radius: 10px;\n"
"	border: 2px solid #2596be;\n"
"}\n"
"\n"
"#aSRollNumber{\n"
"	border: none;\n"
"	background: transparent;\n"
"	color: #2596be;\n"
"}\n"
"\n"
"#aSContentFrm, #aSCLeftFrm, #aSCRightFrm{\n"
"	margin: 5px;\n"
"	background-color: rgba(179, 196, 216, 0);\n"
"}\n"
"\n"
"#aSStudentName, #aSGuardianName, #aSSMobileNumber, #aSUniversity, #aSCourse, #aSSemester{\n"
"	border:none;\n"
"	background-color: rgba(179, 196, 216, 0);\n"
"	border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"	color: rgba(0,0,0,240);\n"
"}\n"
"\n"
"#aSAddBtn{\n"
"	border: none;\n"
"	padding-left: 1"
                        "5px;\n"
"	background-color: rgba(179, 196, 216);\n"
"}\n"
"\n"
"#aSAddBtn:hover{\n"
"	background-color: rgba(179, 196, 216, 160);\n"
"	padding: 5px, 0px;\n"
"	border-top-left-radius: 10px;\n"
"}\n"
"\n"
"#aSAddBtn:pressed{\n"
"	background-color: rgba(179, 196, 216, 255);\n"
"	padding: 5px, 0px;\n"
"	border-top-left-radius: 10px;\n"
"}")
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.aAddStudentWidget = QWidget(Dialog)
        self.aAddStudentWidget.setObjectName(u"aAddStudentWidget")
        self.aAddStudentWidget.setMaximumSize(QSize(550, 500))
        self.aAddStudentWidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.aAddStudentWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.addStudentTitle = QLabel(self.aAddStudentWidget)
        self.addStudentTitle.setObjectName(u"addStudentTitle")
        self.addStudentTitle.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.addStudentTitle, 0, Qt.AlignTop)

        self.aSMainFrm = QFrame(self.aAddStudentWidget)
        self.aSMainFrm.setObjectName(u"aSMainFrm")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aSMainFrm.sizePolicy().hasHeightForWidth())
        self.aSMainFrm.setSizePolicy(sizePolicy)
        self.aSMainFrm.setMinimumSize(QSize(500, 380))
        self.aSMainFrm.setFrameShape(QFrame.StyledPanel)
        self.aSMainFrm.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.aSMainFrm)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.aSSearchFrm = QFrame(self.aSMainFrm)
        self.aSSearchFrm.setObjectName(u"aSSearchFrm")
        self.aSSearchFrm.setFrameShape(QFrame.StyledPanel)
        self.aSSearchFrm.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.aSSearchFrm)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.aSRollNumber = QLineEdit(self.aSSearchFrm)
        self.aSRollNumber.setObjectName(u"aSRollNumber")

        self.horizontalLayout.addWidget(self.aSRollNumber)


        self.verticalLayout_4.addWidget(self.aSSearchFrm, 0, Qt.AlignHCenter)

        self.aSContentFrm = QFrame(self.aSMainFrm)
        self.aSContentFrm.setObjectName(u"aSContentFrm")
        sizePolicy.setHeightForWidth(self.aSContentFrm.sizePolicy().hasHeightForWidth())
        self.aSContentFrm.setSizePolicy(sizePolicy)
        self.aSContentFrm.setFrameShape(QFrame.StyledPanel)
        self.aSContentFrm.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.aSContentFrm)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.aSCLeftFrm = QFrame(self.aSContentFrm)
        self.aSCLeftFrm.setObjectName(u"aSCLeftFrm")
        self.aSCLeftFrm.setFrameShape(QFrame.StyledPanel)
        self.aSCLeftFrm.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.aSCLeftFrm)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.aSStudentName = QLineEdit(self.aSCLeftFrm)
        self.aSStudentName.setObjectName(u"aSStudentName")

        self.verticalLayout_3.addWidget(self.aSStudentName)

        self.aSGuardianName = QLineEdit(self.aSCLeftFrm)
        self.aSGuardianName.setObjectName(u"aSGuardianName")

        self.verticalLayout_3.addWidget(self.aSGuardianName)

        self.aSSMobileNumber = QLineEdit(self.aSCLeftFrm)
        self.aSSMobileNumber.setObjectName(u"aSSMobileNumber")

        self.verticalLayout_3.addWidget(self.aSSMobileNumber)


        self.horizontalLayout_2.addWidget(self.aSCLeftFrm)

        self.aSCRightFrm = QFrame(self.aSContentFrm)
        self.aSCRightFrm.setObjectName(u"aSCRightFrm")
        self.aSCRightFrm.setFrameShape(QFrame.StyledPanel)
        self.aSCRightFrm.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.aSCRightFrm)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.aSUniversity = QComboBox(self.aSCRightFrm)
        self.aSUniversity.addItem("")
        self.aSUniversity.setObjectName(u"aSUniversity")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.aSUniversity.sizePolicy().hasHeightForWidth())
        self.aSUniversity.setSizePolicy(sizePolicy1)
        self.aSUniversity.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)

        self.verticalLayout_5.addWidget(self.aSUniversity)

        self.aSCourse = QComboBox(self.aSCRightFrm)
        self.aSCourse.addItem("")
        self.aSCourse.setObjectName(u"aSCourse")
        sizePolicy1.setHeightForWidth(self.aSCourse.sizePolicy().hasHeightForWidth())
        self.aSCourse.setSizePolicy(sizePolicy1)
        self.aSCourse.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)

        self.verticalLayout_5.addWidget(self.aSCourse)

        self.aSSemester = QComboBox(self.aSCRightFrm)
        self.aSSemester.addItem("")
        self.aSSemester.setObjectName(u"aSSemester")
        sizePolicy1.setHeightForWidth(self.aSSemester.sizePolicy().hasHeightForWidth())
        self.aSSemester.setSizePolicy(sizePolicy1)
        self.aSSemester.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)

        self.verticalLayout_5.addWidget(self.aSSemester)


        self.horizontalLayout_2.addWidget(self.aSCRightFrm)


        self.verticalLayout_4.addWidget(self.aSContentFrm)

        self.aSAddBtn = QPushButton(self.aSMainFrm)
        self.aSAddBtn.setObjectName(u"aSAddBtn")
        self.aSAddBtn.setMinimumSize(QSize(0, 0))

        self.verticalLayout_4.addWidget(self.aSAddBtn, 0, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.aSMainFrm)


        self.gridLayout.addWidget(self.aAddStudentWidget, 0, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.addStudentTitle.setText(QCoreApplication.translate("Dialog", u"Add Student", None))
        self.aSRollNumber.setPlaceholderText(QCoreApplication.translate("Dialog", u"Roll Number", None))
        self.aSStudentName.setPlaceholderText(QCoreApplication.translate("Dialog", u"Student Name", None))
        self.aSGuardianName.setPlaceholderText(QCoreApplication.translate("Dialog", u"Guardian Name", None))
        self.aSSMobileNumber.setPlaceholderText(QCoreApplication.translate("Dialog", u"Mobile Number", None))
        self.aSUniversity.setItemText(0, QCoreApplication.translate("Dialog", u"Select University", None))

        self.aSUniversity.setPlaceholderText("")
        self.aSCourse.setItemText(0, QCoreApplication.translate("Dialog", u"Select Course", None))

        self.aSSemester.setItemText(0, QCoreApplication.translate("Dialog", u"Select Semester", None))

        self.aSAddBtn.setText(QCoreApplication.translate("Dialog", u"Submit", None))
    # retranslateUi

