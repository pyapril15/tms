# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'three_btn_comboAvKVTD.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)
import res_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(122, 42)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setStyleSheet(u"#threeFunctionFrm{\n"
"	background: transparent;\n"
"}\n"
"QPushButton{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(192, 192, 192, 150);\n"
"	border: 2px solid rgba(192, 192, 192, 130);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgba(192, 192, 192, 200);\n"
"	border: 2px solid rgba(192, 192, 192, 180);\n"
"}\n"
"\n"
"")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.threeFunctionFrm = QFrame(Form)
        self.threeFunctionFrm.setObjectName(u"threeFunctionFrm")
        self.threeFunctionFrm.setStyleSheet(u"")
        self.threeFunctionFrm.setFrameShape(QFrame.StyledPanel)
        self.threeFunctionFrm.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.threeFunctionFrm)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.firstEditBtn = QPushButton(self.threeFunctionFrm)
        self.firstEditBtn.setObjectName(u"firstEditBtn")
        self.firstEditBtn.setMinimumSize(QSize(40, 40))
        self.firstEditBtn.setMaximumSize(QSize(40, 40))
        self.firstEditBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.firstEditBtn.setAutoFillBackground(False)
        self.firstEditBtn.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/assets/icons/edit.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.firstEditBtn.setIcon(icon)
        self.firstEditBtn.setIconSize(QSize(28, 28))

        self.horizontalLayout.addWidget(self.firstEditBtn)

        self.secondDeleteBtn = QPushButton(self.threeFunctionFrm)
        self.secondDeleteBtn.setObjectName(u"secondDeleteBtn")
        self.secondDeleteBtn.setMinimumSize(QSize(40, 40))
        self.secondDeleteBtn.setMaximumSize(QSize(40, 40))
        self.secondDeleteBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.secondDeleteBtn.setStyleSheet(u"QPushButton{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgba(192, 192, 192, 150);\n"
"	border: 2px solid rgba(192, 192, 192, 130);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgba(192, 192, 192, 200);\n"
"	border: 2px solid rgba(192, 192, 192, 180);\n"
"}\n"
"\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/assets/icons/delete.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.secondDeleteBtn.setIcon(icon1)
        self.secondDeleteBtn.setIconSize(QSize(28, 28))

        self.horizontalLayout.addWidget(self.secondDeleteBtn)

        self.thirdPrintBtn = QPushButton(self.threeFunctionFrm)
        self.thirdPrintBtn.setObjectName(u"thirdPrintBtn")
        self.thirdPrintBtn.setMinimumSize(QSize(40, 40))
        self.thirdPrintBtn.setMaximumSize(QSize(40, 40))
        self.thirdPrintBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.thirdPrintBtn.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/assets/icons/printer.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.thirdPrintBtn.setIcon(icon2)
        self.thirdPrintBtn.setIconSize(QSize(28, 28))

        self.horizontalLayout.addWidget(self.thirdPrintBtn)


        self.verticalLayout.addWidget(self.threeFunctionFrm, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
#if QT_CONFIG(tooltip)
        self.firstEditBtn.setToolTip(QCoreApplication.translate("Form", u"Edit", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.firstEditBtn.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.firstEditBtn.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.firstEditBtn.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.firstEditBtn.setText("")
#if QT_CONFIG(tooltip)
        self.secondDeleteBtn.setToolTip(QCoreApplication.translate("Form", u"Delete", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.secondDeleteBtn.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.secondDeleteBtn.setText("")
#if QT_CONFIG(tooltip)
        self.thirdPrintBtn.setToolTip(QCoreApplication.translate("Form", u"Print", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.thirdPrintBtn.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.thirdPrintBtn.setText("")
    # retranslateUi

