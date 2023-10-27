import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QHeaderView, QVBoxLayout, QWidget,QDesktopWidget
from DataBase import *
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout, QLabel, QWidget, QHBoxLayout
from PyQt5.QtGui import QGuiApplication, QFont
from PyQt5.QtCore import Qt, QTimer, QDateTime, QTimeZone
import sys
from Connection import *
import socket
from DataBase import *

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
isConnected = connect(client,base_info)
class TableExample(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI(isConnected)

    def initUI(self, isConnected):
        self.setGeometry(100, 100, 1024, 768)
        self.setWindowTitle('SCADA-HMI')

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        # Create a QTableWidget with 5 columns
        tableWidget = QTableWidget(0, 5)
        tableWidget.setHorizontalHeaderLabels(["Name", "Type", "Address", "Value", "Alarm"])

        # Make the table non-editable
        tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)

        layout.addWidget(tableWidget)

        # Calculate the desired height (70% of screen height) and convert it to an integer
        screen_geometry = QGuiApplication.primaryScreen().availableGeometry()
        table_height = int(screen_geometry.height() * 0.7)
        tableWidget.setGeometry(0, 0, screen_geometry.width(), table_height)

        central_widget.setLayout(layout)

        tuplesForPrint = makeTuplesForPrint(signal_info)
        data = list()
        data.extend(tuplesForPrint)

        for row, item in enumerate(data):
            tableWidget.insertRow(row)
            for col, text in enumerate(item):
                tableWidget.setItem(row, col, QTableWidgetItem(text))

        # Create a QHBoxLayout to place the "CONNECTED" label and the time label side by side
        hbox = QHBoxLayout()

        # Create the "CONNECTED" label
        label = QLabel("CONNECTED")
        label.setFont(QFont("Helvetica", 10, QFont.Bold))
        label.setAlignment(Qt.AlignCenter)
        if isConnected:
            label.setStyleSheet("background-color: green;")
        else:
            label.setStyleSheet("background-color: red")

        # Set a fixed height for the label
        label.setFixedHeight(30)

        # Create a label for the current time
        time_label = QLabel("text")
        time_label.setFont(QFont("Helvetica", 10))
        time_label.setAlignment(Qt.AlignCenter)

        # Create a QTimer to update the time label


        hbox.addWidget(label)
        hbox.addSpacing(20)  # Add some spacing between labels
        hbox.addWidget(time_label)

        layout.addLayout(hbox)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TableExample()
    sys.exit(app.exec_())


def main():
    app = QApplication(sys.argv)
    ex = TableExample()
    sys.exit(app.exec_())

