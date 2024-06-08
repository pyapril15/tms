# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_courseFEmBwp.ui'
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
        Dialog.resize(300, 350)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.acUniversityWidget = QWidget(Dialog)
        self.acUniversityWidget.setObjectName(u"acUniversityWidget")
        self.acUniversityWidget.setMinimumSize(QSize(300, 350))
        self.acUniversityWidget.setMaximumSize(QSize(350, 420))
        self.acUniversityWidget.setStyleSheet(u"*{\n"
"	border: none;\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#acTitle, #acCourseName, #acCourseCode, #acCourseShortName, #acCourseYear, #acAddtBtn{\n"
"	margin: 10px;\n"
"}\n"
"\n"
"#acTitle{\n"
"	font: 700 20pt \"Calibri\";	\n"
"	color: rgba(0,0,0,200);\n"
"}\n"
"\n"
"#acCourseName, #acCourseCode, #acCourseShortName, #acCourseYear{\n"
"	font: 700 13pt \"Calibri\";\n"
"	background-color: rgba(0,0,0,0);\n"
"	border:none;\n"
"	border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"	color: rgba(0,0,0,240);\n"
"}\n"
"\n"
"#acAddBtn{\n"
"	text-align: center;\n"
"	font: 700 13pt \"Calibri\";\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255,255,255,210);\n"
"	border-radius:5px;\n"
"}\n"
"\n"
"#acAddBtn:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"\n"
"#acAddBtn:pressed{\n"
"	padding-l"
                        "eft:5px;\n"
"	padding-top:5px;\n"
"	backbground-color: rgba(150,123,111,255);\n"
"}")
        self.verticalLayout = QVBoxLayout(self.acUniversityWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.acTitle = QLabel(self.acUniversityWidget)
        self.acTitle.setObjectName(u"acTitle")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.acTitle.sizePolicy().hasHeightForWidth())
        self.acTitle.setSizePolicy(sizePolicy)
        self.acTitle.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.acTitle, 0, Qt.AlignTop)

        self.acCourseFrm = QFrame(self.acUniversityWidget)
        self.acCourseFrm.setObjectName(u"acCourseFrm")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.acCourseFrm.sizePolicy().hasHeightForWidth())
        self.acCourseFrm.setSizePolicy(sizePolicy1)
        self.acCourseFrm.setMinimumSize(QSize(280, 210))
        self.acCourseFrm.setFrameShape(QFrame.StyledPanel)
        self.acCourseFrm.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.acCourseFrm)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.acCourseName = QLineEdit(self.acCourseFrm)
        self.acCourseName.setObjectName(u"acCourseName")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.acCourseName.sizePolicy().hasHeightForWidth())
        self.acCourseName.setSizePolicy(sizePolicy2)
        self.acCourseName.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.acCourseName)

        self.acCourseCode = QLineEdit(self.acCourseFrm)
        self.acCourseCode.setObjectName(u"acCourseCode")
        sizePolicy2.setHeightForWidth(self.acCourseCode.sizePolicy().hasHeightForWidth())
        self.acCourseCode.setSizePolicy(sizePolicy2)
        self.acCourseCode.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.acCourseCode)

        self.acCourseShortName = QLineEdit(self.acCourseFrm)
        self.acCourseShortName.setObjectName(u"acCourseShortName")
        sizePolicy2.setHeightForWidth(self.acCourseShortName.sizePolicy().hasHeightForWidth())
        self.acCourseShortName.setSizePolicy(sizePolicy2)
        self.acCourseShortName.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.acCourseShortName)

        self.acCourseYear = QLineEdit(self.acCourseFrm)
        self.acCourseYear.setObjectName(u"acCourseYear")
        sizePolicy2.setHeightForWidth(self.acCourseYear.sizePolicy().hasHeightForWidth())
        self.acCourseYear.setSizePolicy(sizePolicy2)
        self.acCourseYear.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.acCourseYear)

        self.acAddBtn = QPushButton(self.acCourseFrm)
        self.acAddBtn.setObjectName(u"acAddBtn")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.acAddBtn.sizePolicy().hasHeightForWidth())
        self.acAddBtn.setSizePolicy(sizePolicy3)
        self.acAddBtn.setMinimumSize(QSize(120, 50))

        self.verticalLayout_2.addWidget(self.acAddBtn, 0, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.acCourseFrm)


        self.gridLayout.addWidget(self.acUniversityWidget, 0, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.acTitle.setText(QCoreApplication.translate("Dialog", u"Add Course", None))
        self.acCourseName.setPlaceholderText(QCoreApplication.translate("Dialog", u"Course Name", None))
        self.acCourseCode.setPlaceholderText(QCoreApplication.translate("Dialog", u"Course Code", None))
        self.acCourseShortName.setPlaceholderText(QCoreApplication.translate("Dialog", u"Short Course Name", None))
        self.acCourseYear.setText("")
        self.acCourseYear.setPlaceholderText(QCoreApplication.translate("Dialog", u"Duration in Year", None))
        self.acAddBtn.setText(QCoreApplication.translate("Dialog", u"Add", None))
#if QT_CONFIG(shortcut)
        self.acAddBtn.setShortcut(QCoreApplication.translate("Dialog", u"Enter", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

