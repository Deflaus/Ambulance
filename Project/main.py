from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QApplication, QTableWidgetItem
from PyQt5.QtGui import QPixmap
import sys
import datetime
from view import MainWindow, CreateCallWindow, CallsWindow, BrigadeWindow, Map
from dbaccess import DataBaseAccess

def startMainW():
    MainForm.show()


def startCreatCallW():
    CreateCallForm.show()


def startCallsW():
    CallsForm.show()


def startBrigadeW():
    BrigadeForm.show()
    PrintTableBrigade()

def startMapW():
    MapForm.show()

def PushBtnCreateCall():
    today = datetime.datetime.today()

    date = today.strftime("%d-%m-%Y / %H:%M:%S")
    cause = createCallW.lineEdit_2.text()
    address = createCallW.lineEdit.text()
    priority = str(createCallW.comboBox.currentIndex() + 1)

    DataBaseAccess.insert_call(date, cause, address, priority)

    CreateCallForm.close()

    createCallW.lineEdit.setText("")
    createCallW.lineEdit_2.setText("")


def PrintTableBrigade():
    brigadeW.tableWidget.setColumnCount(2)
    brigadeW.tableWidget.setRowCount(3)
    brigadeW.tableWidget.setVerticalHeaderLabels(('','',''))
    data = DataBaseAccess.parse_alldata_brigade()
    for i, row in enumerate(data):
        for j, col in enumerate(row):
            element = QTableWidgetItem(str(col))
            element.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            brigadeW.tableWidget.setItem(i, j, element)


def PrintMap():
    pixmap = QPixmap("Map.jpg")



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    MainForm = QtWidgets.QWidget()
    CreateCallForm = QtWidgets.QWidget()
    CallsForm = QtWidgets.QWidget()
    BrigadeForm = QtWidgets.QWidget()
    MapForm = QtWidgets.QWidget()

    mainW = MainWindow()
    createCallW = CreateCallWindow()
    callsW = CallsWindow()
    brigadeW = BrigadeWindow()
    mapW = Map()

    mainW.setupUi(MainForm)
    mainW.pushButton.clicked.connect(startCreatCallW)
    mainW.pushButton_2.clicked.connect(startCallsW)
    mainW.pushButton_3.clicked.connect(startMapW)
    mainW.pushButton_4.clicked.connect(startBrigadeW)

    createCallW.setupUi(CreateCallForm)
    createCallW.pushButton.clicked.connect(PushBtnCreateCall)

    callsW.setupUi(CallsForm)

    brigadeW.setupUi(BrigadeForm)

    mapW.setupUi(MapForm)

    startMainW()

    sys.exit(app.exec_())
