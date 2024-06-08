# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_transport_fee_detailDXZKKz.ui'
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
        Dialog.resize(280, 280)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.aTWidget = QWidget(Dialog)
        self.aTWidget.setObjectName(u"aTWidget")
        self.aTWidget.setMinimumSize(QSize(280, 280))
        self.aTWidget.setMaximumSize(QSize(350, 280))
        self.aTWidget.setStyleSheet(u"*{\n"
"	border: none;\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#aTTitle, #aTCenterName, #aTCenterCode, #aTAmount, #aTAddtBtn{\n"
"	margin: 10px;\n"
"}\n"
"\n"
"#aTTitle{\n"
"	font: 700 20pt \"Calibri\";	\n"
"	color: rgba(0,0,0,200);\n"
"}\n"
"\n"
"#aTCenterName, #aTCenterCode, #aTAmount{\n"
"	font: 700 13pt \"Calibri\";\n"
"	background-color: rgba(0,0,0,0);\n"
"	border:none;\n"
"	border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"	color: rgba(0,0,0,240);\n"
"}\n"
"\n"
"#aTAddBtn{\n"
"	text-align: center;\n"
"	font: 700 13pt \"Calibri\";\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255,255,255,210);\n"
"	border-radius:5px;\n"
"}\n"
"\n"
"#aTAddBtn:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"\n"
"#aTAddBtn:pressed{\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	backbground-"
                        "color: rgba(150,123,111,255);\n"
"}")
        self.verticalLayout = QVBoxLayout(self.aTWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.aTTitle = QLabel(self.aTWidget)
        self.aTTitle.setObjectName(u"aTTitle")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aTTitle.sizePolicy().hasHeightForWidth())
        self.aTTitle.setSizePolicy(sizePolicy)
        self.aTTitle.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.aTTitle, 0, Qt.AlignTop)

        self.aTFrm = QFrame(self.aTWidget)
        self.aTFrm.setObjectName(u"aTFrm")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.aTFrm.sizePolicy().hasHeightForWidth())
        self.aTFrm.setSizePolicy(sizePolicy1)
        self.aTFrm.setMinimumSize(QSize(280, 210))
        self.aTFrm.setFrameShape(QFrame.StyledPanel)
        self.aTFrm.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.aTFrm)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.aTCenterName = QLineEdit(self.aTFrm)
        self.aTCenterName.setObjectName(u"aTCenterName")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.aTCenterName.sizePolicy().hasHeightForWidth())
        self.aTCenterName.setSizePolicy(sizePolicy2)
        self.aTCenterName.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.aTCenterName)

        self.aTCenterCode = QLineEdit(self.aTFrm)
        self.aTCenterCode.setObjectName(u"aTCenterCode")
        sizePolicy2.setHeightForWidth(self.aTCenterCode.sizePolicy().hasHeightForWidth())
        self.aTCenterCode.setSizePolicy(sizePolicy2)
        self.aTCenterCode.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.aTCenterCode)

        self.aTAmount = QLineEdit(self.aTFrm)
        self.aTAmount.setObjectName(u"aTAmount")
        sizePolicy2.setHeightForWidth(self.aTAmount.sizePolicy().hasHeightForWidth())
        self.aTAmount.setSizePolicy(sizePolicy2)
        self.aTAmount.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.aTAmount)

        self.aTAddBtn = QPushButton(self.aTFrm)
        self.aTAddBtn.setObjectName(u"aTAddBtn")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.aTAddBtn.sizePolicy().hasHeightForWidth())
        self.aTAddBtn.setSizePolicy(sizePolicy3)
        self.aTAddBtn.setMinimumSize(QSize(120, 50))

        self.verticalLayout_2.addWidget(self.aTAddBtn, 0, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.aTFrm)


        self.gridLayout.addWidget(self.aTWidget, 0, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.aTTitle.setText(QCoreApplication.translate("Dialog", u"Transport Fee", None))
        self.aTCenterName.setPlaceholderText(QCoreApplication.translate("Dialog", u"Destination or Exam Center", None))
        self.aTCenterCode.setPlaceholderText(QCoreApplication.translate("Dialog", u"Center Code", None))
        self.aTAmount.setText("")
        self.aTAmount.setPlaceholderText(QCoreApplication.translate("Dialog", u"Amount", None))
        self.aTAddBtn.setText(QCoreApplication.translate("Dialog", u"Add", None))
#if QT_CONFIG(shortcut)
        self.aTAddBtn.setShortcut(QCoreApplication.translate("Dialog", u"Enter", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

