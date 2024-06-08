# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'statusbarYxuEet.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(592, 40)
        Form.setMinimumSize(QSize(0, 40))
        Form.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.left_status_lbl = QLabel(Form)
        self.left_status_lbl.setObjectName(u"left_status_lbl")

        self.horizontalLayout.addWidget(self.left_status_lbl)

        self.middle_status_lbl = QLabel(Form)
        self.middle_status_lbl.setObjectName(u"middle_status_lbl")
        self.middle_status_lbl.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.middle_status_lbl)

        self.right_status_lbl = QLabel(Form)
        self.right_status_lbl.setObjectName(u"right_status_lbl")
        self.right_status_lbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.right_status_lbl)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.left_status_lbl.setText("")
        self.middle_status_lbl.setText("")
        self.right_status_lbl.setText("")
    # retranslateUi

