import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QHeaderView, QVBoxLayout, QWidget,QDesktopWidget
from DataBase import *
from PyQt5.QtGui import QPalette, QColor
class TableExample(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
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

        # Calculate the desired height (80% of screen height) and convert it to an integer
        screen_geometry = QDesktopWidget().availableGeometry()
        table_height = int(screen_geometry.height() * 0.8)
        tableWidget.setGeometry(0, 0, screen_geometry.width(), table_height)

        central_widget.setLayout(layout)

        tuplesForPrint = makeTuplesForPrint(signal_info)
        data = list()
        data.extend(tuplesForPrint)

        for row, item in enumerate(data):
            tableWidget.insertRow(row)
            for col, text in enumerate(item):
                tableWidget.setItem(row, col, QTableWidgetItem(text))

        # Adjust column widths to fill the available space
        header = tableWidget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)
        """
        if isConnected:
            connected_label = QLabel("CONNECTED")
            connected_label.setAlignment(Qt.AlignCenter)
            palette = QPalette()
            palette.setColor(QPalette.WindowText, QColor(255, 255, 255))
            palette.setColor(QPalette.Window, QColor(0, 128, 0))  # Dark green background
            connected_label.setPalette(palette)
            layout.addWidget(connected_label)
        """
        central_widget.setLayout(layout)
        self.show()

def main():
    app = QApplication(sys.argv)
    ex = TableExample()
    sys.exit(app.exec_())

