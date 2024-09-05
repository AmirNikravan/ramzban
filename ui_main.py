# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(600, 500)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(600, 500))
        MainWindow.setMaximumSize(QSize(600, 500))
        MainWindow.setStyleSheet(u"background-color: rgb(237, 237, 237);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"IRANSansXFaNum"])
        font.setPointSize(16)
        font.setBold(True)
        self.label.setFont(font)

        self.verticalLayout_3.addWidget(self.label)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer = QSpacerItem(18, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer)

        self.pushButton_randomkey = QPushButton(self.centralwidget)
        self.pushButton_randomkey.setObjectName(u"pushButton_randomkey")
        self.pushButton_randomkey.setMinimumSize(QSize(64, 25))
        font1 = QFont()
        font1.setFamilies([u"IRANSansXFaNum"])
        font1.setPointSize(8)
        font1.setBold(True)
        self.pushButton_randomkey.setFont(font1)
        self.pushButton_randomkey.setStyleSheet(u"QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(44, 70, 140);\n"
"border-radius : 5px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(170, 170, 127);\n"
"}")

        self.horizontalLayout_8.addWidget(self.pushButton_randomkey)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy1)
        self.lineEdit.setMinimumSize(QSize(473, 24))
        font2 = QFont()
        font2.setFamilies([u"IRANSansXFaNum"])
        font2.setPointSize(12)
        font2.setBold(True)
        self.lineEdit.setFont(font2)
        self.lineEdit.setStyleSheet(u"QLineEdit{\n"
"border-radius : 5px;\n"
"	background-color: rgb(206, 206, 206);\n"
"}\n"
"QLineEdit:focus\n"
"{\n"
"\n"
"	border : 1px solid;\n"
"}")

        self.horizontalLayout_8.addWidget(self.lineEdit)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        font3 = QFont()
        font3.setFamilies([u"IRANSansXFaNum"])
        font3.setPointSize(10)
        font3.setBold(True)
        self.label_2.setFont(font3)

        self.horizontalLayout_8.addWidget(self.label_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        font4 = QFont()
        font4.setFamilies([u"IRANSansXFaNum"])
        font4.setBold(True)
        self.groupBox_2.setFont(font4)
        self.groupBox_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.listWidget_filename_decrypt = QListWidget(self.groupBox_2)
        self.listWidget_filename_decrypt.setObjectName(u"listWidget_filename_decrypt")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.listWidget_filename_decrypt.sizePolicy().hasHeightForWidth())
        self.listWidget_filename_decrypt.setSizePolicy(sizePolicy3)
        self.listWidget_filename_decrypt.setMinimumSize(QSize(0, 0))
        self.listWidget_filename_decrypt.setMaximumSize(QSize(16777215, 53))

        self.horizontalLayout_4.addWidget(self.listWidget_filename_decrypt)

        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(45, 0))
        self.label_8.setMaximumSize(QSize(28, 19))
        self.label_8.setFont(font3)

        self.horizontalLayout_4.addWidget(self.label_8)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.listWidget_fileaddress_decrypt = QListWidget(self.groupBox_2)
        self.listWidget_fileaddress_decrypt.setObjectName(u"listWidget_fileaddress_decrypt")
        sizePolicy3.setHeightForWidth(self.listWidget_fileaddress_decrypt.sizePolicy().hasHeightForWidth())
        self.listWidget_fileaddress_decrypt.setSizePolicy(sizePolicy3)
        self.listWidget_fileaddress_decrypt.setMaximumSize(QSize(16777215, 103))

        self.horizontalLayout_5.addWidget(self.listWidget_fileaddress_decrypt)

        self.label_10 = QLabel(self.groupBox_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(60, 0))
        self.label_10.setMaximumSize(QSize(61, 16777215))
        self.label_10.setFont(font3)

        self.horizontalLayout_5.addWidget(self.label_10)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(4)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.pushButton_decrypt = QPushButton(self.groupBox_2)
        self.pushButton_decrypt.setObjectName(u"pushButton_decrypt")
        self.pushButton_decrypt.setMinimumSize(QSize(81, 21))
        self.pushButton_decrypt.setFont(font4)
        self.pushButton_decrypt.setStyleSheet(u"QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(44, 70, 140);\n"
"border-radius : 5px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(170, 170, 127);\n"
"}")

        self.horizontalLayout_6.addWidget(self.pushButton_decrypt)

        self.pushButton_choosefile_decrpyt = QPushButton(self.groupBox_2)
        self.pushButton_choosefile_decrpyt.setObjectName(u"pushButton_choosefile_decrpyt")
        self.pushButton_choosefile_decrpyt.setMinimumSize(QSize(81, 21))
        self.pushButton_choosefile_decrpyt.setFont(font4)
        self.pushButton_choosefile_decrpyt.setStyleSheet(u"QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(44, 70, 140);\n"
"border-radius : 5px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(170, 170, 127);\n"
"}")

        self.horizontalLayout_6.addWidget(self.pushButton_choosefile_decrpyt)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)


        self.horizontalLayout_7.addWidget(self.groupBox_2)

        self.verticalSpacer = QSpacerItem(19, 132, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.horizontalLayout_7.addItem(self.verticalSpacer)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setFont(font4)
        self.groupBox.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.listWidget_filename_encrpyt = QListWidget(self.groupBox)
        self.listWidget_filename_encrpyt.setObjectName(u"listWidget_filename_encrpyt")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.listWidget_filename_encrpyt.sizePolicy().hasHeightForWidth())
        self.listWidget_filename_encrpyt.setSizePolicy(sizePolicy4)
        self.listWidget_filename_encrpyt.setMinimumSize(QSize(0, 53))
        self.listWidget_filename_encrpyt.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.listWidget_filename_encrpyt.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.horizontalLayout.addWidget(self.listWidget_filename_encrpyt)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(45, 0))
        self.label_3.setMaximumSize(QSize(28, 19))
        self.label_3.setFont(font3)

        self.horizontalLayout.addWidget(self.label_3)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.listWidget_fileaddress_encrypt = QListWidget(self.groupBox)
        self.listWidget_fileaddress_encrypt.setObjectName(u"listWidget_fileaddress_encrypt")
        sizePolicy4.setHeightForWidth(self.listWidget_fileaddress_encrypt.sizePolicy().hasHeightForWidth())
        self.listWidget_fileaddress_encrypt.setSizePolicy(sizePolicy4)
        self.listWidget_fileaddress_encrypt.setMaximumSize(QSize(16777215, 103))
        self.listWidget_fileaddress_encrypt.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)

        self.horizontalLayout_2.addWidget(self.listWidget_fileaddress_encrypt)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(60, 0))
        self.label_5.setMaximumSize(QSize(61, 16777215))
        self.label_5.setFont(font3)

        self.horizontalLayout_2.addWidget(self.label_5)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_encrypt = QPushButton(self.groupBox)
        self.pushButton_encrypt.setObjectName(u"pushButton_encrypt")
        self.pushButton_encrypt.setMinimumSize(QSize(81, 21))
        self.pushButton_encrypt.setFont(font4)
        self.pushButton_encrypt.setStyleSheet(u"QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(44, 70, 140);\n"
"border-radius : 5px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(170, 170, 127);\n"
"}")

        self.horizontalLayout_3.addWidget(self.pushButton_encrypt)

        self.pushButton_choosefile_encrypt = QPushButton(self.groupBox)
        self.pushButton_choosefile_encrypt.setObjectName(u"pushButton_choosefile_encrypt")
        self.pushButton_choosefile_encrypt.setMinimumSize(QSize(81, 21))
        self.pushButton_choosefile_encrypt.setFont(font4)
        self.pushButton_choosefile_encrypt.setStyleSheet(u"QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(44, 70, 140);\n"
"border-radius : 5px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(170, 170, 127);\n"
"}")

        self.horizontalLayout_3.addWidget(self.pushButton_choosefile_encrypt)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_7.addWidget(self.groupBox)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.textEdit.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.textEdit)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0631\u0645\u0632\u0628\u0627\u0646", None))
        self.pushButton_randomkey.setText(QCoreApplication.translate("MainWindow", u"\u06a9\u0644\u06cc\u062f \u062a\u0635\u0627\u062f\u0641\u06cc", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u06a9\u0644\u06cc\u062f:", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u0631\u0645\u0632\u06af\u0634\u0627\u06cc\u06cc", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u0646\u0627\u0645 \u0641\u0627\u06cc\u0644 :", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u0622\u062f\u0631\u0633 \u0641\u0627\u06cc\u0644:", None))
        self.pushButton_decrypt.setText(QCoreApplication.translate("MainWindow", u"\u0631\u0645\u0632\u06af\u0634\u0627\u06cc\u06cc", None))
        self.pushButton_choosefile_decrpyt.setText(QCoreApplication.translate("MainWindow", u"\u0641\u0627\u06cc\u0644 \u0631\u0627 \u0627\u0646\u062a\u062e\u0627\u0628 \u06a9\u0646\u06cc\u062f", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u0631\u0645\u0632\u06af\u0630\u0627\u0631\u06cc", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0646\u0627\u0645 \u0641\u0627\u06cc\u0644 :", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0622\u062f\u0631\u0633 \u0641\u0627\u06cc\u0644:", None))
        self.pushButton_encrypt.setText(QCoreApplication.translate("MainWindow", u"\u0631\u0645\u0632\u06af\u0630\u0627\u0631\u06cc", None))
        self.pushButton_choosefile_encrypt.setText(QCoreApplication.translate("MainWindow", u"\u0641\u0627\u06cc\u0644 \u0631\u0627 \u0627\u0646\u062a\u062e\u0627\u0628 \u06a9\u0646\u06cc\u062f", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
    # retranslateUi

