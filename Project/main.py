from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtGui import QPixmap
import sys
import datetime
from view import MainWindow, CreateCallWindow, CallsWindow, BrigadeWindow, Map, Way
from dbaccess import DataBaseAccess

def startMainW():
    MainForm.show()


def startCreatCallW():
    CreateCallForm.show()


def startCallsW():
    CallsForm.show()
    PrinTableCalls()


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

    SwapAddBrig(createCallW.lineEdit.text())

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


def PrintWay():
    wayW.pixmapBack = QPixmap("")
    WayForm.show()

def SolveTask(addOfCall):
    dataOfDist = DataBaseAccess.parse_alldata_distance()
    dataOfAdd = DataBaseAccess.parse_alldata_addresses()
    dataOfBrig = DataBaseAccess.parse_alldata_brigade()

    indBrig = 0
    addOfBrig = ['']*3
    indAddOfBrig = [0]*3
    indAddOfCall = 0
    dist = [0]*3
    way = [0]*3

    for i, row in enumerate(dataOfBrig):
        addOfBrig[i] = row[1]

    for j, row in enumerate(dataOfAdd):
        for i in range(0,3):
            if row[0] == addOfBrig[i]:
                indAddOfBrig[i] = j + 1
        if row[0] == addOfCall:
            indAddOfCall = j + 1

    for row in dataOfDist:
        for k, j in enumerate(indAddOfBrig):
            if (row[0] == int(str(j) + str(indAddOfCall))) or (row[0] == int(str(indAddOfCall) + str(j))):
                dist[k] = row[1]
                way[k] = row[0]

    mindist = dist[0]
    for i in range(1, 3):
        if dist[i] <= mindist:
            mindist = dist[i]
            indBrig = i

    return indBrig


def SwapAddBrig(addOfCall):
    indBrig = SolveTask(addOfCall)
    dataOfBrig = DataBaseAccess.parse_alldata_brigade()
    addOfBrig = [''] * 3
    for i, row in enumerate(dataOfBrig):
        addOfBrig[i] = row[1]
    DataBaseAccess.swap_address_brigade(dataOfBrig[indBrig][0], dataOfBrig[indBrig][1], addOfCall)


def PrinTableCalls():
    addressOfCall = ""
    callsW.tableWidget.setRowCount(DataBaseAccess.count_of_calls())
    data = DataBaseAccess.parse_alldata_calls()
    for i, row in enumerate(data):
        for j, col in enumerate(row):
            if j == 2: addressOfCall = str(col)
            if j != 3:
                element = QTableWidgetItem(str(col))
            else:
                if col == 1:  element = QTableWidgetItem("Неотложная помощь")
                if col == 2:  element = QTableWidgetItem("Экстренная перевозка")
            element.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            callsW.tableWidget.setItem(i, j, element)
        element = QTableWidgetItem(str(SolveTask(addressOfCall) + 1))
        callsW.tableWidget.setItem(i, j + 1, element)
        pushbutton = QtWidgets.QPushButton()
        pushbutton.clicked.connect(PrintWay)
        callsW.tableWidget.setCellWidget(i, j + 2, pushbutton)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    MainForm = QtWidgets.QWidget()
    CreateCallForm = QtWidgets.QWidget()
    CallsForm = QtWidgets.QWidget()
    BrigadeForm = QtWidgets.QWidget()
    MapForm = QtWidgets.QWidget()
    WayForm = QtWidgets.QWidget()

    mainW = MainWindow()
    createCallW = CreateCallWindow()
    callsW = CallsWindow()
    brigadeW = BrigadeWindow()
    mapW = Map()
    wayW = Way()

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

    wayW.setupUi(WayForm)

    startMainW()


    sys.exit(app.exec_())
