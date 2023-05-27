# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'anime_quotes.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(437, 287)
        self.actionSave_to_text_file = QAction(MainWindow)
        self.actionSave_to_text_file.setObjectName(u"actionSave_to_text_file")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.quoteLabel = QLabel(self.centralwidget)
        self.quoteLabel.setObjectName(u"quoteLabel")
        self.quoteLabel.setAlignment(Qt.AlignCenter)
        self.quoteLabel.setWordWrap(True)

        self.verticalLayout.addWidget(self.quoteLabel)

        self.characterAnimeLabel = QLabel(self.centralwidget)
        self.characterAnimeLabel.setObjectName(u"characterAnimeLabel")

        self.verticalLayout.addWidget(self.characterAnimeLabel)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.getQuoteButton = QPushButton(self.centralwidget)
        self.getQuoteButton.setObjectName(u"getQuoteButton")

        self.horizontalLayout.addWidget(self.getQuoteButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 437, 23))
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionSave_to_text_file.setText(QCoreApplication.translate("MainWindow", u"Save to text file", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.quoteLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.characterAnimeLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.getQuoteButton.setText(QCoreApplication.translate("MainWindow", u"Get Random Quote", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
    # retranslateUi

