from PyQt6.QtCore import Qt
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
        self.setFixedSize(200, 250)

        # create widgets
        convert_from_label = QLabel("Convert From")
        convert_from = QComboBox()
        convert_to_label = QLabel("Convert To")
        convert_to = QComboBox()
        temperature = QLineEdit()
        temperature.setToolTip("Temperature to convert")
        temperature.setAlignment(Qt.AlignmentFlag.AlignCenter)
        conversion = QLabel("Converted temperature")
        conversion.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # add items to each QComboBox
        convert_from.addItem("Celsius")
        convert_from.addItem("Fahrenheit")
        convert_from.addItem("Kelvin")

        convert_to.addItem("Celsius")
        convert_to.addItem("Fahrenheit")
        convert_to.addItem("Kelvin")

        # add widgets to a layout
        layout = QVBoxLayout()
        layout.addWidget(convert_from_label)
        layout.addWidget(convert_from)
        layout.addWidget(convert_to_label)
        layout.addWidget(convert_to)
        layout.addWidget(temperature)
        layout.addWidget(conversion)

        # display the layout
        main_widget = QWidget()
        main_widget.setLayout(layout)
        self.setCentralWidget(main_widget)

        app.setStyleSheet("""
            QComboBox {
                color: white;
                font-size: 16px;
            }
            QLabel {
                color: white;
                font-size: 16px;
            }
            QLineEdit {
                color: white;
                font-size: 16px;
            }
        """)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()