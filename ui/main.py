# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/main.ui'
#
# Created: Wed Jan 29 04:37:57 2014
#      by: pyside-uic 0.2.15 running on qt 1.2.1
#
# WARNING! All changes made in this file will be lost!

from qt import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(421, 456)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabs = QtGui.QTabWidget(self.centralwidget)
        self.tabs.setObjectName("tabs")
        self.fs2 = QtGui.QWidget()
        self.fs2.setObjectName("fs2")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.fs2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.gogextract = QtGui.QPushButton(self.fs2)
        self.gogextract.setObjectName("gogextract")
        self.verticalLayout_2.addWidget(self.gogextract)
        self.select = QtGui.QPushButton(self.fs2)
        self.select.setObjectName("select")
        self.verticalLayout_2.addWidget(self.select)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.tabs.addTab(self.fs2, "")
        self.mods = QtGui.QWidget()
        self.mods.setObjectName("mods")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.mods)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tableWidget = QtGui.QTableWidget(self.mods)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.verticalLayout_3.addWidget(self.tableWidget)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.update = QtGui.QPushButton(self.mods)
        self.update.setObjectName("update")
        self.horizontalLayout.addWidget(self.update)
        self.select_mod = QtGui.QPushButton(self.mods)
        self.select_mod.setObjectName("select_mod")
        self.horizontalLayout.addWidget(self.select_mod)
        self.uninstall_mod = QtGui.QPushButton(self.mods)
        self.uninstall_mod.setObjectName("uninstall_mod")
        self.horizontalLayout.addWidget(self.uninstall_mod)
        self.install_mod = QtGui.QPushButton(self.mods)
        self.install_mod.setObjectName("install_mod")
        self.horizontalLayout.addWidget(self.install_mod)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.tabs.addTab(self.mods, "")
        self.verticalLayout.addWidget(self.tabs)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 421, 19))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Mod Manager", None, QtGui.QApplication.UnicodeUTF8))
        self.gogextract.setText(QtGui.QApplication.translate("MainWindow", "Install FS2 with the GOG installer", None, QtGui.QApplication.UnicodeUTF8))
        self.select.setText(QtGui.QApplication.translate("MainWindow", "Select installed FS2 (Open)", None, QtGui.QApplication.UnicodeUTF8))
        self.tabs.setTabText(self.tabs.indexOf(self.fs2), QtGui.QApplication.translate("MainWindow", "FS2", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("MainWindow", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("MainWindow", "Version", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("MainWindow", "Status", None, QtGui.QApplication.UnicodeUTF8))
        self.update.setText(QtGui.QApplication.translate("MainWindow", "Update List", None, QtGui.QApplication.UnicodeUTF8))
        self.select_mod.setText(QtGui.QApplication.translate("MainWindow", "Select Mod", None, QtGui.QApplication.UnicodeUTF8))
        self.uninstall_mod.setText(QtGui.QApplication.translate("MainWindow", "Uninstall Mod", None, QtGui.QApplication.UnicodeUTF8))
        self.install_mod.setText(QtGui.QApplication.translate("MainWindow", "Install Mod", None, QtGui.QApplication.UnicodeUTF8))
        self.tabs.setTabText(self.tabs.indexOf(self.mods), QtGui.QApplication.translate("MainWindow", "Mods", None, QtGui.QApplication.UnicodeUTF8))
