# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'book_transportGBOIHt.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QDialog,
    QFrame, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
import res_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(580, 550)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.bookTransportWidget = QWidget(Dialog)
        self.bookTransportWidget.setObjectName(u"bookTransportWidget")
        self.bookTransportWidget.setMinimumSize(QSize(580, 550))
        self.bookTransportWidget.setMaximumSize(QSize(600, 580))
        self.bookTransportWidget.setStyleSheet(u"*{\n"
"	color: #000;\n"
"	background-color: #fff;\n"
"	font: 14pt \"Calibri\";\n"
"}\n"
"\n"
"QLabel{\n"
"	background-color: rgba(192, 192, 192, 0);\n"
"}\n"
"\n"
"#bTTitle{\n"
"	font: 700 42pt \"Calibri\";\n"
"}\n"
"\n"
"#bTSearchFrm{\n"
"	margin: 5px;\n"
"	padding: 5px;\n"
"	border-radius: 10px;\n"
"	border: 2px solid #2596be;\n"
"}\n"
"\n"
"#bTRollNumber{\n"
"	border: none;\n"
"	background: transparent;\n"
"	color: #2596be;\n"
"	padding-left: 5px;\n"
"}\n"
"\n"
"#bTSearchBtn{\n"
"	border: none;\n"
"	background: transparent;\n"
"	padding-left: 15px;\n"
"}\n"
"\n"
"#bTSearchBtn:hover{\n"
"	padding: 10px;\n"
"}\n"
"\n"
"#bTSearchBtn:pressed{\n"
"	padding: 5px;\n"
"}\n"
"\n"
"\n"
"#bTStaticDataFrm{\n"
"	padding: 5px;\n"
"	border-radius: 10px;\n"
"	border: 2px solid rgba(192, 192, 192, 50);\n"
"	background-color: rgba(192, 192, 192, 50);\n"
"}\n"
"\n"
"#bTStudentName, #bTGardianName, #bTMobileNumber, #bTUniversity, #bTCourse, #bTSemester, #bTAmount{\n"
"	border:none;\n"
"	background-color: rgba(179, 196, 216, 0)"
                        ";\n"
"	border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"	color: rgba(0,0,0,240);\n"
"}\n"
"\n"
"#bTViewTableFrm{\n"
"	padding: 5px;\n"
"	border-radius: 10px;\n"
"	border: 2px solid rgba(192, 192, 192, 50);\n"
"}\n"
"\n"
"QTableWidget{\n"
"	color: black;\n"
"	background-color: rgba(192, 192, 192, 50);\n"
"	alternate-background-color: rgba(96, 96, 96, 50);\n"
"	selection-background-color: rgba(40, 40, 40, 30);\n"
"	gridline-color: black;\n"
"	font: 700 13pt \"Arial\";\n"
"	selection-color: blue;\n"
"}\n"
"\n"
"QTableWidget::item:selected{\n"
"	color: white;\n"
"	background-color: rgba(0, 170, 0, 50);\n"
"}\n"
"\n"
"QHeaderView{\n"
"	border:none;\n"
"	font: 700 14pt \"Arial\";\n"
"	background-color: rgba(0, 0, 0, 230);\n"
"	color: white;\n"
"	border: 2px solid white;\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"	border:none;\n"
"	font: 700 14pt \"Arial\";\n"
"	background-color: rgba(0, 0, 0, 230);\n"
"	color: white;\n"
"	border: 1px solid white;\n"
"}\n"
"\n"
"#bTFunctionFrm{\n"
"	padding: 5px;\n"
"	border-radius:"
                        " 10px;\n"
"	border: 2px solid rgba(192, 192, 192, 50);\n"
"	background-color: rgba(192, 192, 192, 50);\n"
"}\n"
"\n"
"#bTAmount{\n"
"	width: 80;\n"
"}\n"
"\n"
"#bTModeOfPayment{\n"
"	background: transparent;\n"
"}\n"
"\n"
"#bTSubmitBtn{\n"
"	border-radius: 10px;\n"
"	background-color: rgba(192, 192, 192, 50);\n"
"	padding-top: 5px;\n"
"	padding-bottom: 5px;\n"
"	padding-left: 5px;\n"
"}\n"
"\n"
"#bTSubmitBtn:hover{\n"
"	background-color: rgba(192, 192, 192, 100);\n"
"	padding-left: 0px;\n"
"}\n"
"\n"
"#bTSubmitBtn:pressed{\n"
"	background-color: rgba(192, 192, 192, 150);\n"
"	padding-left: 0px;\n"
"}")
        self.verticalLayout_7 = QVBoxLayout(self.bookTransportWidget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.bTTitle = QLabel(self.bookTransportWidget)
        self.bTTitle.setObjectName(u"bTTitle")
        self.bTTitle.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.bTTitle)

        self.bTSearchFrm = QFrame(self.bookTransportWidget)
        self.bTSearchFrm.setObjectName(u"bTSearchFrm")
        self.bTSearchFrm.setFrameShape(QFrame.StyledPanel)
        self.bTSearchFrm.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.bTSearchFrm)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.bTRollNumber = QLineEdit(self.bTSearchFrm)
        self.bTRollNumber.setObjectName(u"bTRollNumber")

        self.horizontalLayout.addWidget(self.bTRollNumber)

        self.bTSearchBtn = QPushButton(self.bTSearchFrm)
        self.bTSearchBtn.setObjectName(u"bTSearchBtn")
        self.bTSearchBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icon/assets/icon/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bTSearchBtn.setIcon(icon)
        self.bTSearchBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.bTSearchBtn)


        self.verticalLayout_7.addWidget(self.bTSearchFrm, 0, Qt.AlignHCenter)

        self.bTStaticDataFrm = QFrame(self.bookTransportWidget)
        self.bTStaticDataFrm.setObjectName(u"bTStaticDataFrm")
        self.bTStaticDataFrm.setMaximumSize(QSize(16777215, 16777215))
        self.bTStaticDataFrm.setFrameShape(QFrame.StyledPanel)
        self.bTStaticDataFrm.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.bTStaticDataFrm)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.bTSStudentName = QLabel(self.bTStaticDataFrm)
        self.bTSStudentName.setObjectName(u"bTSStudentName")

        self.verticalLayout.addWidget(self.bTSStudentName)

        self.bTSGardianName = QLabel(self.bTStaticDataFrm)
        self.bTSGardianName.setObjectName(u"bTSGardianName")

        self.verticalLayout.addWidget(self.bTSGardianName)

        self.bTSMobileNumber = QLabel(self.bTStaticDataFrm)
        self.bTSMobileNumber.setObjectName(u"bTSMobileNumber")

        self.verticalLayout.addWidget(self.bTSMobileNumber)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.bTStudentName = QLineEdit(self.bTStaticDataFrm)
        self.bTStudentName.setObjectName(u"bTStudentName")

        self.verticalLayout_3.addWidget(self.bTStudentName)

        self.bTGardianName = QLineEdit(self.bTStaticDataFrm)
        self.bTGardianName.setObjectName(u"bTGardianName")

        self.verticalLayout_3.addWidget(self.bTGardianName)

        self.bTMobileNumber = QLineEdit(self.bTStaticDataFrm)
        self.bTMobileNumber.setObjectName(u"bTMobileNumber")

        self.verticalLayout_3.addWidget(self.bTMobileNumber)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.bTSUniversity = QLabel(self.bTStaticDataFrm)
        self.bTSUniversity.setObjectName(u"bTSUniversity")

        self.verticalLayout_2.addWidget(self.bTSUniversity)

        self.bTSCourse = QLabel(self.bTStaticDataFrm)
        self.bTSCourse.setObjectName(u"bTSCourse")

        self.verticalLayout_2.addWidget(self.bTSCourse)

        self.bTSSemester = QLabel(self.bTStaticDataFrm)
        self.bTSSemester.setObjectName(u"bTSSemester")

        self.verticalLayout_2.addWidget(self.bTSSemester)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.bTUniversity = QLineEdit(self.bTStaticDataFrm)
        self.bTUniversity.setObjectName(u"bTUniversity")

        self.verticalLayout_4.addWidget(self.bTUniversity)

        self.bTCourse = QLineEdit(self.bTStaticDataFrm)
        self.bTCourse.setObjectName(u"bTCourse")

        self.verticalLayout_4.addWidget(self.bTCourse)

        self.bTSemester = QLineEdit(self.bTStaticDataFrm)
        self.bTSemester.setObjectName(u"bTSemester")

        self.verticalLayout_4.addWidget(self.bTSemester)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)


        self.verticalLayout_7.addWidget(self.bTStaticDataFrm)

        self.bTViewTableFrm = QFrame(self.bookTransportWidget)
        self.bTViewTableFrm.setObjectName(u"bTViewTableFrm")
        self.bTViewTableFrm.setFrameShape(QFrame.StyledPanel)
        self.bTViewTableFrm.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.bTViewTableFrm)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.bTViewTable = QTableWidget(self.bTViewTableFrm)
        if (self.bTViewTable.columnCount() < 5):
            self.bTViewTable.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.bTViewTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.bTViewTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.bTViewTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.bTViewTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.bTViewTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.bTViewTable.setObjectName(u"bTViewTable")
        self.bTViewTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.bTViewTable.setAlternatingRowColors(True)
        self.bTViewTable.setSelectionMode(QAbstractItemView.MultiSelection)
        self.bTViewTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.bTViewTable.setSortingEnabled(True)
        self.bTViewTable.horizontalHeader().setMinimumSectionSize(150)
        self.bTViewTable.horizontalHeader().setDefaultSectionSize(160)
        self.bTViewTable.horizontalHeader().setStretchLastSection(True)
        self.bTViewTable.verticalHeader().setMinimumSectionSize(40)
        self.bTViewTable.verticalHeader().setDefaultSectionSize(40)
        self.bTViewTable.verticalHeader().setProperty("showSortIndicator", True)

        self.verticalLayout_5.addWidget(self.bTViewTable)


        self.verticalLayout_7.addWidget(self.bTViewTableFrm)

        self.bTFunctionFrm = QFrame(self.bookTransportWidget)
        self.bTFunctionFrm.setObjectName(u"bTFunctionFrm")
        self.bTFunctionFrm.setFrameShape(QFrame.StyledPanel)
        self.bTFunctionFrm.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.bTFunctionFrm)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.bTFunctionFrm)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.bTAmount = QLineEdit(self.bTFunctionFrm)
        self.bTAmount.setObjectName(u"bTAmount")
        self.bTAmount.setAlignment(Qt.AlignCenter)
        self.bTAmount.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.bTAmount)

        self.bTModeOfPayment = QComboBox(self.bTFunctionFrm)
        self.bTModeOfPayment.addItem("")
        self.bTModeOfPayment.addItem("")
        self.bTModeOfPayment.addItem("")
        self.bTModeOfPayment.setObjectName(u"bTModeOfPayment")
        self.bTModeOfPayment.setMinimumSize(QSize(120, 0))
        self.bTModeOfPayment.setCursor(QCursor(Qt.PointingHandCursor))
        self.bTModeOfPayment.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.horizontalLayout_3.addWidget(self.bTModeOfPayment)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)

        self.bTSubmitBtn = QPushButton(self.bTFunctionFrm)
        self.bTSubmitBtn.setObjectName(u"bTSubmitBtn")
        self.bTSubmitBtn.setMinimumSize(QSize(80, 0))
        self.bTSubmitBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_6.addWidget(self.bTSubmitBtn, 0, Qt.AlignHCenter)


        self.verticalLayout_7.addWidget(self.bTFunctionFrm, 0, Qt.AlignHCenter)


        self.gridLayout.addWidget(self.bookTransportWidget, 0, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.bTTitle.setText(QCoreApplication.translate("Dialog", u"Book Transport", None))
        self.bTRollNumber.setPlaceholderText(QCoreApplication.translate("Dialog", u"Roll Number", None))
        self.bTSearchBtn.setText("")
#if QT_CONFIG(shortcut)
        self.bTSearchBtn.setShortcut(QCoreApplication.translate("Dialog", u"Enter", None))
#endif // QT_CONFIG(shortcut)
        self.bTSStudentName.setText(QCoreApplication.translate("Dialog", u"Student Name", None))
        self.bTSGardianName.setText(QCoreApplication.translate("Dialog", u"Gardian Name", None))
        self.bTSMobileNumber.setText(QCoreApplication.translate("Dialog", u"Mobile Number", None))
        self.bTSUniversity.setText(QCoreApplication.translate("Dialog", u"University", None))
        self.bTSCourse.setText(QCoreApplication.translate("Dialog", u"Course", None))
        self.bTSSemester.setText(QCoreApplication.translate("Dialog", u"Semester", None))
        ___qtablewidgetitem = self.bTViewTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"Journey ID", None));
        ___qtablewidgetitem1 = self.bTViewTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"Subject Code", None));
        ___qtablewidgetitem2 = self.bTViewTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"Subject Name", None));
        ___qtablewidgetitem3 = self.bTViewTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Dialog", u"Date of Exam", None));
        ___qtablewidgetitem4 = self.bTViewTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Dialog", u"Exam Center", None));
        self.label.setText(QCoreApplication.translate("Dialog", u"Amount", None))
        self.bTAmount.setInputMask("")
        self.bTAmount.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.bTAmount.setPlaceholderText("")
        self.bTModeOfPayment.setItemText(0, QCoreApplication.translate("Dialog", u"Mode of Payment", None))
        self.bTModeOfPayment.setItemText(1, QCoreApplication.translate("Dialog", u"Cash", None))
        self.bTModeOfPayment.setItemText(2, QCoreApplication.translate("Dialog", u"Online", None))

        self.bTSubmitBtn.setText(QCoreApplication.translate("Dialog", u"Submit", None))
    # retranslateUi

