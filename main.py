from PyQt6.QtWidgets import (
    QApplication, 
    QMainWindow,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QComboBox,
    QWidget
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Temperature Conversion")
        self.setMinimumSize(600, 400)

        # create objects
        convert_from = QComboBox()
        convert_to = QComboBox()
        temperature = QLineEdit("Enter the temperate to convert")
        conversion = QLabel("Converted temperature")

        # add items to each QComboBox
        convert_from.addItem("Celsius")
        convert_from.addItem("Fahrenheit")
        convert_from.addItem("Kelvin")

        convert_to.addItem("Celsius")
        convert_to.addItem("Fahrenheit")
        convert_to.addItem("Kelvin")

        # add objects to a layout
        layout = QVBoxLayout()
        layout.addWidget(convert_from)
        layout.addWidget(convert_to)
        layout.addWidget(temperature)
        layout.addWidget(conversion)

        # display the layout
        main_widget = QWidget()
        main_widget.setLayout(layout)
        self.setCentralWidget(main_widget)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()