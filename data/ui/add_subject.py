# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_subjectAtfLyb.ui'
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
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(250, 273)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.asSubjectWidget = QWidget(Dialog)
        self.asSubjectWidget.setObjectName(u"asSubjectWidget")
        self.asSubjectWidget.setMinimumSize(QSize(0, 0))
        self.asSubjectWidget.setMaximumSize(QSize(350, 420))
        self.asSubjectWidget.setStyleSheet(u"*{\n"
"	border: none;\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#asTitle, #asSubjectName, #asSubjectCode, #asAddtBtn{\n"
"	margin: 10px;\n"
"}\n"
"\n"
"#asTitle{\n"
"	font: 700 20pt \"Calibri\";	\n"
"	color: rgba(0,0,0,200);\n"
"}\n"
"\n"
"#asSubjectName, #asSubjectCode{\n"
"	font: 700 13pt \"Calibri\";\n"
"	background-color: rgba(0,0,0,0);\n"
"	border:none;\n"
"	border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"	color: rgba(0,0,0,240);\n"
"}\n"
"\n"
"#asAddBtn{\n"
"	text-align: center;\n"
"	font: 700 13pt \"Calibri\";\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255,255,255,210);\n"
"	border-radius:5px;\n"
"}\n"
"\n"
"#asAddBtn:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"\n"
"#asAddBtn:pressed{\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	backbground-color: rgba(150,12"
                        "3,111,255);\n"
"}")
        self.verticalLayout = QVBoxLayout(self.asSubjectWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.asTitle = QLabel(self.asSubjectWidget)
        self.asTitle.setObjectName(u"asTitle")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.asTitle.sizePolicy().hasHeightForWidth())
        self.asTitle.setSizePolicy(sizePolicy)
        self.asTitle.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.asTitle, 0, Qt.AlignTop)

        self.asSubjectFrm = QFrame(self.asSubjectWidget)
        self.asSubjectFrm.setObjectName(u"asSubjectFrm")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.asSubjectFrm.sizePolicy().hasHeightForWidth())
        self.asSubjectFrm.setSizePolicy(sizePolicy1)
        self.asSubjectFrm.setMinimumSize(QSize(250, 220))
        self.asSubjectFrm.setFrameShape(QFrame.StyledPanel)
        self.asSubjectFrm.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.asSubjectFrm)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.asSubjectName = QLineEdit(self.asSubjectFrm)
        self.asSubjectName.setObjectName(u"asSubjectName")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.asSubjectName.sizePolicy().hasHeightForWidth())
        self.asSubjectName.setSizePolicy(sizePolicy2)
        self.asSubjectName.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.asSubjectName)

        self.asSubjectCode = QLineEdit(self.asSubjectFrm)
        self.asSubjectCode.setObjectName(u"asSubjectCode")
        sizePolicy2.setHeightForWidth(self.asSubjectCode.sizePolicy().hasHeightForWidth())
        self.asSubjectCode.setSizePolicy(sizePolicy2)
        self.asSubjectCode.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.asSubjectCode)

        self.asAddBtn = QPushButton(self.asSubjectFrm)
        self.asAddBtn.setObjectName(u"asAddBtn")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.asAddBtn.sizePolicy().hasHeightForWidth())
        self.asAddBtn.setSizePolicy(sizePolicy3)
        self.asAddBtn.setMinimumSize(QSize(120, 50))

        self.verticalLayout_2.addWidget(self.asAddBtn, 0, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.asSubjectFrm)


        self.gridLayout.addWidget(self.asSubjectWidget, 0, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.asTitle.setText(QCoreApplication.translate("Dialog", u"Add Subject", None))
        self.asSubjectName.setPlaceholderText(QCoreApplication.translate("Dialog", u"Subject Name", None))
        self.asSubjectCode.setPlaceholderText(QCoreApplication.translate("Dialog", u"Subject Code", None))
        self.asAddBtn.setText(QCoreApplication.translate("Dialog", u"Add", None))
#if QT_CONFIG(shortcut)
        self.asAddBtn.setShortcut(QCoreApplication.translate("Dialog", u"Enter", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

