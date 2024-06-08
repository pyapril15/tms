# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'custom_title_barceQpOm.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import res_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(782, 44)
        Form.setStyleSheet(u"*{\n"
"	margin: 0px;\n"
"	padding: 0px;\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(255, 255, 255);\n"
"	font: 12pt \"Segoe UI\";\n"
"	outline: none;\n"
"	border: none;\n"
"}\n"
"\n"
"QToolTip {\n"
"	background-color: #f8f8f2;\n"
"	border: 1px solid #CCC;\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"}\n"
"\n"
"\n"
"QPushButton{\n"
"	border: none;\n"
"	margin: 2px;\n"
"}\n"
"\n"
"#titlebar_frm{\n"
"	margin: 2px;\n"
"}\n"
"\n"
"#search_frm{\n"
"	padding-left: 2px;\n"
"	padding-right: 2px;\n"
"	border-radius: 10px;\n"
"	border: 2px solid #2596be;\n"
"}\n"
"\n"
"#search_icon{\n"
"	margin-right: 2px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"#searchItem{\n"
"	border: none;\n"
"	background: transparent;\n"
"	color: #2596be;\n"
"	font: 13pt \"Segoe UI\";\n"
"}\n"
"\n"
"#maximizeBtn, #minimizeBtn, #closeBtn{\n"
"	border-radius: 10px;\n"
"	padding: 5px;\n"
""
                        "	font-size: 12px;\n"
"	color: #ffffff;\n"
"}\n"
"\n"
"#maximizeBtn {\n"
"	background-color: #2a82da;\n"
"}\n"
"\n"
"#maximizeBtn:hover {\n"
"	background-color: #1767b8;\n"
"}\n"
"\n"
"#maximizeBtn:pressed {\n"
"	background-color: #0e4673;\n"
"}\n"
"\n"
"#minimizeBtn{\n"
"	background-color: rgb(255, 170, 0);\n"
"}\n"
"\n"
"#minimizeBtn:hover {\n"
"	background-color: rgba(255, 170, 0, 150);\n"
"}\n"
"\n"
"#minimizeBtn:pressed {\n"
"	background-color: rgba(255, 170, 34, 200);\n"
"}\n"
"\n"
"#closeBtn {\n"
"	background-color: rgb(255, 0, 0);\n"
"}\n"
"\n"
"#closeBtn:hover {\n"
"	background-color: rgba(255, 0, 0, 150);\n"
"}\n"
"\n"
"#closeBtn:pressed {\n"
"	background-color: rgba(255, 0, 0, 200);\n"
"}")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.titlebar_frm = QFrame(Form)
        self.titlebar_frm.setObjectName(u"titlebar_frm")
        self.titlebar_frm.setMaximumSize(QSize(16777215, 50))
        self.titlebar_frm.setStyleSheet(u"")
        self.titlebar_frm.setFrameShape(QFrame.StyledPanel)
        self.titlebar_frm.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.titlebar_frm)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.titlebar_left_frm = QFrame(self.titlebar_frm)
        self.titlebar_left_frm.setObjectName(u"titlebar_left_frm")
        self.titlebar_left_frm.setFrameShape(QFrame.StyledPanel)
        self.titlebar_left_frm.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.titlebar_left_frm)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.window_icon_btn = QPushButton(self.titlebar_left_frm)
        self.window_icon_btn.setObjectName(u"window_icon_btn")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.window_icon_btn.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icon/assets/icon/bus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.window_icon_btn.setIcon(icon)
        self.window_icon_btn.setIconSize(QSize(48, 32))

        self.horizontalLayout.addWidget(self.window_icon_btn)

        self.window_title = QLabel(self.titlebar_left_frm)
        self.window_title.setObjectName(u"window_title")
        self.window_title.setFont(font)

        self.horizontalLayout.addWidget(self.window_title)

        self.name_icon_btn = QPushButton(self.titlebar_left_frm)
        self.name_icon_btn.setObjectName(u"name_icon_btn")
        self.name_icon_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icon/assets/icon/menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.name_icon_btn.setIcon(icon1)
        self.name_icon_btn.setIconSize(QSize(32, 32))
        self.name_icon_btn.setCheckable(True)
        self.name_icon_btn.setAutoExclusive(True)

        self.horizontalLayout.addWidget(self.name_icon_btn)


        self.horizontalLayout_5.addWidget(self.titlebar_left_frm)

        self.titlebar_middle_frm = QFrame(self.titlebar_frm)
        self.titlebar_middle_frm.setObjectName(u"titlebar_middle_frm")
        self.titlebar_middle_frm.setFrameShape(QFrame.StyledPanel)
        self.titlebar_middle_frm.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.titlebar_middle_frm)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(154, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.search_frm = QFrame(self.titlebar_middle_frm)
        self.search_frm.setObjectName(u"search_frm")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_frm.sizePolicy().hasHeightForWidth())
        self.search_frm.setSizePolicy(sizePolicy)
        self.search_frm.setMinimumSize(QSize(180, 0))
        self.search_frm.setAutoFillBackground(False)
        self.search_frm.setFrameShape(QFrame.StyledPanel)
        self.search_frm.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.search_frm)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.search_icon = QLabel(self.search_frm)
        self.search_icon.setObjectName(u"search_icon")
        self.search_icon.setPixmap(QPixmap(u":/icon/assets/icon/search.svg"))
        self.search_icon.setScaledContents(False)
        self.search_icon.setWordWrap(False)

        self.horizontalLayout_4.addWidget(self.search_icon)

        self.searchItem = QLineEdit(self.search_frm)
        self.searchItem.setObjectName(u"searchItem")

        self.horizontalLayout_4.addWidget(self.searchItem)


        self.horizontalLayout_3.addWidget(self.search_frm)

        self.horizontalSpacer_2 = QSpacerItem(154, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.horizontalLayout_5.addWidget(self.titlebar_middle_frm)

        self.titlebar_right_frm = QFrame(self.titlebar_frm)
        self.titlebar_right_frm.setObjectName(u"titlebar_right_frm")
        self.titlebar_right_frm.setMaximumSize(QSize(100, 16777215))
        self.titlebar_right_frm.setFrameShape(QFrame.StyledPanel)
        self.titlebar_right_frm.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.titlebar_right_frm)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.userBtn = QPushButton(self.titlebar_right_frm)
        self.userBtn.setObjectName(u"userBtn")
        self.userBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icon/assets/icon/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.userBtn.setIcon(icon2)
        self.userBtn.setIconSize(QSize(32, 32))
        self.userBtn.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.userBtn)

        self.maximizeBtn = QPushButton(self.titlebar_right_frm)
        self.maximizeBtn.setObjectName(u"maximizeBtn")
        self.maximizeBtn.setMinimumSize(QSize(24, 24))
        self.maximizeBtn.setMaximumSize(QSize(24, 24))
        self.maximizeBtn.setCursor(QCursor(Qt.ArrowCursor))
        self.maximizeBtn.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.maximizeBtn)

        self.minimizeBtn = QPushButton(self.titlebar_right_frm)
        self.minimizeBtn.setObjectName(u"minimizeBtn")
        self.minimizeBtn.setMinimumSize(QSize(24, 24))
        self.minimizeBtn.setMaximumSize(QSize(24, 24))
        self.minimizeBtn.setCursor(QCursor(Qt.ArrowCursor))
        self.minimizeBtn.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.minimizeBtn)

        self.closeBtn = QPushButton(self.titlebar_right_frm)
        self.closeBtn.setObjectName(u"closeBtn")
        self.closeBtn.setMinimumSize(QSize(24, 24))
        self.closeBtn.setMaximumSize(QSize(24, 24))
        self.closeBtn.setCursor(QCursor(Qt.ArrowCursor))
        self.closeBtn.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.closeBtn)


        self.horizontalLayout_5.addWidget(self.titlebar_right_frm)


        self.verticalLayout.addWidget(self.titlebar_frm)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
#if QT_CONFIG(tooltip)
        self.window_icon_btn.setToolTip(QCoreApplication.translate("Form", u"Application Icon", None))
#endif // QT_CONFIG(tooltip)
        self.window_icon_btn.setText("")
#if QT_CONFIG(tooltip)
        self.window_title.setToolTip(QCoreApplication.translate("Form", u"Application name", None))
#endif // QT_CONFIG(tooltip)
        self.window_title.setText(QCoreApplication.translate("Form", u"Bus Transport", None))
#if QT_CONFIG(tooltip)
        self.name_icon_btn.setToolTip(QCoreApplication.translate("Form", u"Sidebar", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.name_icon_btn.setStatusTip(QCoreApplication.translate("Form", u"Sidebar", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.name_icon_btn.setWhatsThis(QCoreApplication.translate("Form", u"Icon and Icon with name", None))
#endif // QT_CONFIG(whatsthis)
        self.name_icon_btn.setText("")
#if QT_CONFIG(shortcut)
        self.name_icon_btn.setShortcut(QCoreApplication.translate("Form", u"Ctrl+Alt+\u1e24", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.search_frm.setToolTip(QCoreApplication.translate("Form", u"Search Bar", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.search_frm.setStatusTip(QCoreApplication.translate("Form", u"Search Bar", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.search_frm.setWhatsThis(QCoreApplication.translate("Form", u"Search any thing like Rull Number, Receipt Number etc", None))
#endif // QT_CONFIG(whatsthis)
        self.search_icon.setText("")
#if QT_CONFIG(tooltip)
        self.searchItem.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.searchItem.setPlaceholderText(QCoreApplication.translate("Form", u"Search Something...", None))
#if QT_CONFIG(tooltip)
        self.userBtn.setToolTip(QCoreApplication.translate("Form", u"User", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.userBtn.setStatusTip(QCoreApplication.translate("Form", u"User", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.userBtn.setWhatsThis(QCoreApplication.translate("Form", u"User Description", None))
#endif // QT_CONFIG(whatsthis)
        self.userBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeBtn.setToolTip(QCoreApplication.translate("Form", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeBtn.setToolTip(QCoreApplication.translate("Form", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeBtn.setToolTip(QCoreApplication.translate("Form", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeBtn.setText("")
    # retranslateUi

