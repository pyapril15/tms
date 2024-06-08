# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user_registrationdTGbBU.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(496, 436)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"#uContentFrm{\n"
"	border-radius:50px;\n"
"	background-color: rgb(158, 232, 255);\n"
"}\n"
"\n"
"#uLeftFrm{\n"
"	border-top-left-radius:50px;\n"
"	border-bottom-left-radius:50px;\n"
"	background-color: rgba(0,0,0,80);\n"
"}\n"
"\n"
"#uDescriptionFrm{\n"
"	margin-top: 50px;\n"
"	padding: 10px;\n"
"	background-color:rgba(0,0,0,75);\n"
"}\n"
"\n"
"#uCreator{\n"
"	margin: 5px;\n"
"	font: 700 20pt \"Calibri\";\n"
"	color:rgba(255,255,255,200);\n"
"}\n"
"\n"
"#uWisher{\n"
"	margin: 5px;\n"
"	color: rgba(255,255,255,170);\n"
"}\n"
"\n"
"#uRightFrm{\n"
"	padding: 10px;\n"
"	border-top-right-radius: 50px;\n"
"	border-bottom-right-radius: 50px;\n"
"	background-color: rgba(255,255,255,255);\n"
"}\n"
"\n"
"#uTitle{\n"
"	margin: 10px;\n"
"	font: 700 20pt \"Calibri\";	\n"
"	color: rgba(0,0,0,200);\n"
"}\n"
"\n"
"#uUsername, #uFullName, #uMobileNumber, #uPassword{\n"
"	margin: 10px;\n"
"	background-color: rgba(0,0,0,0);\n"
"	border:none;\n"
"	border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"	color: rgba(0,0,0,240);\n"
"}\n"
""
                        "\n"
"#uSignUpBtn{\n"
"	margin: 10px;\n"
"	text-align: center;\n"
"	font: 700 13pt \"Calibri\";\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255,255,255,210);\n"
"	border-radius:5px;\n"
"}\n"
"\n"
"#uSignUpBtn:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"\n"
"#uSignUpBtn:hover{\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	backbground-color: rgba(150,123,111,255);\n"
"}\n"
"")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.uContentFrm = QFrame(self.widget)
        self.uContentFrm.setObjectName(u"uContentFrm")
        self.uContentFrm.setMinimumSize(QSize(460, 400))
        self.uContentFrm.setMaximumSize(QSize(600, 510))
        self.uContentFrm.setFrameShape(QFrame.StyledPanel)
        self.uContentFrm.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.uContentFrm)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.uLeftFrm = QFrame(self.uContentFrm)
        self.uLeftFrm.setObjectName(u"uLeftFrm")
        self.uLeftFrm.setFrameShape(QFrame.StyledPanel)
        self.uLeftFrm.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.uLeftFrm)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.uDescriptionFrm = QFrame(self.uLeftFrm)
        self.uDescriptionFrm.setObjectName(u"uDescriptionFrm")
        self.uDescriptionFrm.setFrameShape(QFrame.StyledPanel)
        self.uDescriptionFrm.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.uDescriptionFrm)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.uCreator = QLabel(self.uDescriptionFrm)
        self.uCreator.setObjectName(u"uCreator")
        font = QFont()
        font.setFamilies([u"Calibri"])
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        self.uCreator.setFont(font)

        self.verticalLayout_2.addWidget(self.uCreator)

        self.uWisher = QLabel(self.uDescriptionFrm)
        self.uWisher.setObjectName(u"uWisher")
        font1 = QFont()
        font1.setFamilies([u"Calibri"])
        font1.setPointSize(14)
        font1.setBold(False)
        font1.setItalic(False)
        self.uWisher.setFont(font1)
        self.uWisher.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.uWisher)


        self.verticalLayout.addWidget(self.uDescriptionFrm, 0, Qt.AlignTop)


        self.horizontalLayout.addWidget(self.uLeftFrm)

        self.uRightFrm = QFrame(self.uContentFrm)
        self.uRightFrm.setObjectName(u"uRightFrm")
        self.uRightFrm.setFrameShape(QFrame.StyledPanel)
        self.uRightFrm.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.uRightFrm)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.uTitle = QLabel(self.uRightFrm)
        self.uTitle.setObjectName(u"uTitle")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uTitle.sizePolicy().hasHeightForWidth())
        self.uTitle.setSizePolicy(sizePolicy)
        self.uTitle.setFont(font)
        self.uTitle.setStyleSheet(u"")
        self.uTitle.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.uTitle)

        self.uUsername = QLineEdit(self.uRightFrm)
        self.uUsername.setObjectName(u"uUsername")
        sizePolicy.setHeightForWidth(self.uUsername.sizePolicy().hasHeightForWidth())
        self.uUsername.setSizePolicy(sizePolicy)
        self.uUsername.setMinimumSize(QSize(0, 60))
        self.uUsername.setSizeIncrement(QSize(0, 0))
        self.uUsername.setBaseSize(QSize(0, 0))
        self.uUsername.setFont(font1)
        self.uUsername.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.uUsername)

        self.uFullName = QLineEdit(self.uRightFrm)
        self.uFullName.setObjectName(u"uFullName")
        sizePolicy.setHeightForWidth(self.uFullName.sizePolicy().hasHeightForWidth())
        self.uFullName.setSizePolicy(sizePolicy)
        self.uFullName.setMinimumSize(QSize(0, 60))
        self.uFullName.setSizeIncrement(QSize(0, 0))
        self.uFullName.setBaseSize(QSize(0, 0))
        self.uFullName.setFont(font1)
        self.uFullName.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.uFullName)

        self.uMobileNumber = QLineEdit(self.uRightFrm)
        self.uMobileNumber.setObjectName(u"uMobileNumber")
        sizePolicy.setHeightForWidth(self.uMobileNumber.sizePolicy().hasHeightForWidth())
        self.uMobileNumber.setSizePolicy(sizePolicy)
        self.uMobileNumber.setMinimumSize(QSize(0, 60))
        self.uMobileNumber.setSizeIncrement(QSize(0, 0))
        self.uMobileNumber.setBaseSize(QSize(0, 0))
        self.uMobileNumber.setFont(font1)
        self.uMobileNumber.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.uMobileNumber)

        self.uPassword = QLineEdit(self.uRightFrm)
        self.uPassword.setObjectName(u"uPassword")
        sizePolicy.setHeightForWidth(self.uPassword.sizePolicy().hasHeightForWidth())
        self.uPassword.setSizePolicy(sizePolicy)
        self.uPassword.setMinimumSize(QSize(0, 60))
        self.uPassword.setSizeIncrement(QSize(0, 0))
        self.uPassword.setFont(font1)
        self.uPassword.setStyleSheet(u"")
        self.uPassword.setEchoMode(QLineEdit.Password)

        self.verticalLayout_3.addWidget(self.uPassword)

        self.uSignUpBtn = QPushButton(self.uRightFrm)
        self.uSignUpBtn.setObjectName(u"uSignUpBtn")
        sizePolicy.setHeightForWidth(self.uSignUpBtn.sizePolicy().hasHeightForWidth())
        self.uSignUpBtn.setSizePolicy(sizePolicy)
        self.uSignUpBtn.setMinimumSize(QSize(0, 70))
        font2 = QFont()
        font2.setFamilies([u"Calibri"])
        font2.setPointSize(13)
        font2.setBold(True)
        font2.setItalic(False)
        self.uSignUpBtn.setFont(font2)
        self.uSignUpBtn.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.uSignUpBtn)


        self.horizontalLayout.addWidget(self.uRightFrm)


        self.gridLayout_2.addWidget(self.uContentFrm, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.uCreator.setText(QCoreApplication.translate("Dialog", u"<strong>pyapril15</strong>", None))
        self.uWisher.setText(QCoreApplication.translate("Dialog", u"Hi, Welcome to <strong>Transport</strong> Fee Manament System", None))
        self.uTitle.setText(QCoreApplication.translate("Dialog", u"User Registration", None))
        self.uUsername.setPlaceholderText(QCoreApplication.translate("Dialog", u"Username", None))
        self.uFullName.setPlaceholderText(QCoreApplication.translate("Dialog", u"Fullname", None))
        self.uMobileNumber.setPlaceholderText(QCoreApplication.translate("Dialog", u"Mobile Number", None))
        self.uPassword.setPlaceholderText(QCoreApplication.translate("Dialog", u"Password", None))
        self.uSignUpBtn.setText(QCoreApplication.translate("Dialog", u"Signup", None))
#if QT_CONFIG(shortcut)
        self.uSignUpBtn.setShortcut(QCoreApplication.translate("Dialog", u"Enter", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

