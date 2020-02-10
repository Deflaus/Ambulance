from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QHBoxLayout, QWidget, QLabel
from PyQt5.QtGui import QPixmap

class MainWindow(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(380, 172)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 2, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 3, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_3.setText(_translate("Form", "Карта"))
        self.pushButton_2.setText(_translate("Form", "Вызовы"))
        self.pushButton.setText(_translate("Form", "Сделать вызов"))
        self.pushButton_4.setText(_translate("Form", "Бригады"))


class CreateCallWindow(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(347, 211)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 5, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 7, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 3, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 6, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.comboBox.setItemText(0, _translate("Form", "Неотложная помощь"))
        self.comboBox.setItemText(1, _translate("Form", "Экстренная перевозка"))
        self.pushButton.setText(_translate("Form", "Сделать вызов"))
        self.label_2.setText(_translate("Form", "Причина"))
        self.label_3.setText(_translate("Form", "Важность"))
        self.label.setText(_translate("Form", "Адрес"))


class CallsWindow(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(650, 241)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setMinimumSize(QtCore.QSize(381, 0))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Дата/время"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Причина "))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Адрес"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Важность"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Бригада"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Маршрут"))


class BrigadeWindow(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(370, 227)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "№"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Текущий адрес"))

class Map(object):
    def setupUi(self, Form):
        self.hbox = QHBoxLayout()
        self.pixmapBack = QPixmap("Map.png")
        self.pixmap1 = QPixmap("адреса/Декабристов-1.png")
        self.pixmap2 = QPixmap("адреса/СибгатаХакима-2.png")
        self.pixmap3 = QPixmap("адреса/Четаева-3.png")

        Form.setObjectName("Form")
        Form.resize(651, 403)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.labelBack = QtWidgets.QLabel(Form)
        self.label1 = QtWidgets.QLabel(Form)
        self.label2 = QtWidgets.QLabel(Form)
        self.label3 = QtWidgets.QLabel(Form)

        self.labelBack.setPixmap(self.pixmapBack)
        self.label1.setPixmap(self.pixmap1)
        self.label2.setPixmap(self.pixmap2)
        self.label3.setPixmap(self.pixmap3)

        self.hbox.addWidget(self.labelBack)
        self.hbox.addWidget(self.label1)
        self.hbox.addWidget(self.label2)
        self.hbox.addWidget(self.label3)


        self.labelBack.setObjectName("labelBack")
        self.label1.setObjectName("label1")
        self.label2.setObjectName("label2")
        self.label3.setObjectName("label3")
        self.gridLayout.addWidget(self.labelBack, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.label1, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.label2, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.label3, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))


class Way(object):
    def setupUi(self, Form):
        self.hbox = QHBoxLayout()
        self.pixmapBack = QPixmap()

        Form.setObjectName("Form")
        Form.resize(651, 403)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.labelBack = QtWidgets.QLabel(Form)

        self.labelBack.setPixmap(self.pixmapBack)

        self.hbox.addWidget(self.labelBack)


        self.labelBack.setObjectName("labelBack")
        self.gridLayout.addWidget(self.labelBack, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
