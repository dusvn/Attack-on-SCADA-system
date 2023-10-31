import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QHeaderView, QVBoxLayout, QWidget,QDesktopWidget
from DataBase import *
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout, QLabel, QWidget, QHBoxLayout
from PyQt5.QtGui import QGuiApplication, QFont
from PyQt5.QtCore import Qt, QTimer, QDateTime, QTimeZone
from Connection import *
import socket
from Acquisition import *
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)

class TableExample(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(100, 100,1280, 1024)
        self.setWindowTitle('SCADA-HMI')

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()

        # Create a QTableWidget with 5 columns and make it an instance variable
        self.tableWidget = QTableWidget(0, 5)
        self.tableWidget.setHorizontalHeaderLabels(["Name", "Type", "Address", "Value", "Alarm"])

        # Make the table non-editable
        self.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)

        layout.addWidget(self.tableWidget)

        # Calculate the desired height (70% of screen height) and convert it to an integer

        screen_geometry = QGuiApplication.primaryScreen().availableGeometry()
        table_height = int(screen_geometry.height() * 0.7)
        self.tableWidget.setGeometry(0, 0, screen_geometry.width(), table_height)

        central_widget.setLayout(layout)

        for col in range(self.tableWidget.columnCount()):
            self.tableWidget.horizontalHeader().setSectionResizeMode(col, QHeaderView.Stretch)

        tuplesForPrint = makeTuplesForPrint(signal_info)
        data = list()
        data.extend(tuplesForPrint)

        for row, item in enumerate(data):
            self.tableWidget.insertRow(row)
            for col, text in enumerate(item):
                self.tableWidget.setItem(row, col, QTableWidgetItem(text))

        self.show()

        # Create a QHBoxLayout to place the "CONNECTED" label and the time label side by side
        hbox = QHBoxLayout()

        # Create the "CONNECTED" label
        label = QLabel("CONNECTED")
        label.setFont(QFont("Helvetica", 10, QFont.Bold))
        label.setAlignment(Qt.AlignCenter)
        # Set a fixed height for the label
        label.setFixedHeight(30)
        showConnected(client, base_info, label)
        hbox.addWidget(label)

        layout.addLayout(hbox)

        #okida na svake 0.5 sek update tabele
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateTable)
        self.timer.start(500)
    def updateTable(self):
            tuples = makeTuplesForPrint(signal_info) # fresh info
            data = list()
            data.extend(tuples)
            self.tableWidget.setRowCount(0) # brise poslednje podatke
            for row, item in enumerate(data): #update
                self.tableWidget.insertRow(row)
                for col, text in enumerate(item):
                    self.tableWidget.setItem(row, col, QTableWidgetItem(text))

def main():
    app = QApplication(sys.argv)
    ex = TableExample()
    acquisition_thread = threading.Thread(target=Acquisition, args=(base_info, signal_info, client))
    acquisition_thread.daemon = True #koristi se za niti koje rade u pozadini
    acquisition_thread.start()
    sys.exit(app.exec_())

def showConnected(client,base_info,label):
    isConnected = connect(client, base_info)
    if isConnected:
        label.setStyleSheet("background-color: green;")
    else:
        label.setStyleSheet("background-color: red")

if __name__ == '__main__':
    main()
