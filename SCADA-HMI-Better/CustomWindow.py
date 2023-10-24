import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QHeaderView, QVBoxLayout, QWidget

class TableExample(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 800, 400)
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

        central_widget.setLayout(layout)

        # Populate the table with sample data
        data = [
            ("Item1", "Type1", "Address1", "Value1", "Alarm1"),
            ("Item2", "Type2", "Address2", "Value2", "Alarm2"),
            ("Item3", "Type3", "Address3", "Value3", "Alarm3"),
            ("Item4", "Type4", "Address4", "Value4", "Alarm4")
        ]

        for row, item in enumerate(data):
            tableWidget.insertRow(row)
            for col, text in enumerate(item):
                tableWidget.setItem(row, col, QTableWidgetItem(text))

        # Adjust column widths to fill the available space
        header = tableWidget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)

        self.show()

def main():
    app = QApplication(sys.argv)
    ex = TableExample()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
