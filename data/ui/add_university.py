# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_universityZFuduQ.ui'
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
        Dialog.resize(300, 280)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.auUniversityWidget = QWidget(Dialog)
        self.auUniversityWidget.setObjectName(u"auUniversityWidget")
        self.auUniversityWidget.setMinimumSize(QSize(300, 280))
        self.auUniversityWidget.setMaximumSize(QSize(350, 280))
        self.auUniversityWidget.setStyleSheet(u"*{\n"
"	border: none;\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#auTitle, #auUniversityName, #auUniversityCode, #auUniversityShortName, #auSubmitBtn{\n"
"	margin: 10px;\n"
"}\n"
"\n"
"#auTitle{\n"
"	font: 700 20pt \"Calibri\";	\n"
"	color: rgba(0,0,0,200);\n"
"}\n"
"\n"
"#auUniversityName, #auUniversityCode, #auUniversityShortName{\n"
"	font: 700 14pt \"Calibri\";\n"
"	background-color: rgba(0,0,0,0);\n"
"	border:none;\n"
"	border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"	color: rgba(0,0,0,240);\n"
"}\n"
"\n"
"#auSubmitBtn{\n"
"	text-align: center;\n"
"	font: 700 13pt \"Calibri\";\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255,255,255,210);\n"
"	border-radius:5px;\n"
"}\n"
"\n"
"#auSubmitBtn:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"\n"
"#auSubmitBtn:pressed{\n"
"	padd"
                        "ing-left:5px;\n"
"	padding-top:5px;\n"
"	backbground-color: rgba(150,123,111,255);\n"
"}")
        self.verticalLayout = QVBoxLayout(self.auUniversityWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.auTitle = QLabel(self.auUniversityWidget)
        self.auTitle.setObjectName(u"auTitle")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.auTitle.sizePolicy().hasHeightForWidth())
        self.auTitle.setSizePolicy(sizePolicy)
        self.auTitle.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.auTitle, 0, Qt.AlignTop)

        self.auUniversityFrm = QFrame(self.auUniversityWidget)
        self.auUniversityFrm.setObjectName(u"auUniversityFrm")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.auUniversityFrm.sizePolicy().hasHeightForWidth())
        self.auUniversityFrm.setSizePolicy(sizePolicy1)
        self.auUniversityFrm.setMinimumSize(QSize(0, 0))
        self.auUniversityFrm.setFrameShape(QFrame.StyledPanel)
        self.auUniversityFrm.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.auUniversityFrm)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.auUniversityName = QLineEdit(self.auUniversityFrm)
        self.auUniversityName.setObjectName(u"auUniversityName")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.auUniversityName.sizePolicy().hasHeightForWidth())
        self.auUniversityName.setSizePolicy(sizePolicy2)
        self.auUniversityName.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.auUniversityName)

        self.auUniversityCode = QLineEdit(self.auUniversityFrm)
        self.auUniversityCode.setObjectName(u"auUniversityCode")
        sizePolicy2.setHeightForWidth(self.auUniversityCode.sizePolicy().hasHeightForWidth())
        self.auUniversityCode.setSizePolicy(sizePolicy2)
        self.auUniversityCode.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.auUniversityCode)

        self.auUniversityShortName = QLineEdit(self.auUniversityFrm)
        self.auUniversityShortName.setObjectName(u"auUniversityShortName")
        sizePolicy2.setHeightForWidth(self.auUniversityShortName.sizePolicy().hasHeightForWidth())
        self.auUniversityShortName.setSizePolicy(sizePolicy2)
        self.auUniversityShortName.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.auUniversityShortName)

        self.auSubmitBtn = QPushButton(self.auUniversityFrm)
        self.auSubmitBtn.setObjectName(u"auSubmitBtn")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.auSubmitBtn.sizePolicy().hasHeightForWidth())
        self.auSubmitBtn.setSizePolicy(sizePolicy3)
        self.auSubmitBtn.setMinimumSize(QSize(120, 60))

        self.verticalLayout_2.addWidget(self.auSubmitBtn, 0, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.auUniversityFrm)


        self.gridLayout.addWidget(self.auUniversityWidget, 0, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.auTitle.setText(QCoreApplication.translate("Dialog", u"Add University", None))
        self.auUniversityName.setPlaceholderText(QCoreApplication.translate("Dialog", u"University Name", None))
        self.auUniversityCode.setPlaceholderText(QCoreApplication.translate("Dialog", u"University Code", None))
        self.auUniversityShortName.setPlaceholderText(QCoreApplication.translate("Dialog", u"University Short Name", None))
        self.auSubmitBtn.setText(QCoreApplication.translate("Dialog", u"Submit", None))
#if QT_CONFIG(shortcut)
        self.auSubmitBtn.setShortcut(QCoreApplication.translate("Dialog", u"Enter", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

