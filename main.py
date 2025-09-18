from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication, 
    QMainWindow,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QComboBox,
    QPushButton,
    QWidget
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Temperature Conversion")
        self.setFixedSize(250, 250)

        # create widgets
        convert_from_label = QLabel("Convert From")
        self.convert_from_combobox = QComboBox()
        convert_to_label = QLabel("Convert To")
        self.convert_to_combobox = QComboBox()
        self.temperature_input = QLineEdit()
        self.temperature_input.setToolTip("Temperature to convert")
        self.temperature_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.convert_button = QPushButton("Convert Temperature")
        self.conversion = QLabel()
        self.conversion.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # add items to each QComboBox
        combobox_items = ['Celsius', 'Fahrenheit', 'Kelvin']
        self.convert_from_combobox.addItems(combobox_items)
        self.convert_to_combobox.addItems(combobox_items)

        # add widgets to a layout
        layout = QVBoxLayout()
        layout.addWidget(convert_from_label)
        layout.addWidget(self.convert_from_combobox)
        layout.addWidget(convert_to_label)
        layout.addWidget(self.convert_to_combobox)
        layout.addWidget(self.temperature_input)
        layout.addWidget(self.convert_button)
        layout.addWidget(self.conversion)

        # display the layout
        main_widget = QWidget()
        main_widget.setLayout(layout)
        self.setCentralWidget(main_widget)

        # global style for the app
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

    # connect signals
        self.convert_button.clicked.connect(self.show_indexes)

    # slots
    def show_indexes(self):
        # get the index value from each combobox
        convert_from_index = self.convert_from_combobox.currentIndex()
        convert_to_index = self.convert_to_combobox.currentIndex()
        #print(f"ComboBox 1 index: {convert_from_index}, ComboBox 2 index: {convert_to_index}")

        # convert temperature based on index (0 = Celsius, 1 = Fahrenheit, 2 = Kelvin)
        # if trying to convert to the same format
        if (convert_from_index == 0 and convert_to_index == 0) or (convert_from_index == 1 and convert_to_index == 1) or (convert_from_index == 2 and convert_to_index == 2):
            self.conversion.setText(self.temperature_input.text())

        elif (convert_from_index == 0 and convert_to_index == 1): # celsius to fahrenheit
            self.celsius_to_fahrenheit(self.temperature_input.text())

        elif (convert_from_index == 1 and convert_to_index == 0): # fahrenheit to celsius
            self.fahrenheit_to_celsius(self.temperature_input.text())

        elif (convert_from_index == 0 and convert_to_index == 2): # celsius to kelvin
            self.celsius_to_kelvin(self.temperature_input.text())

        elif (convert_from_index == 2 and convert_to_index == 0): # kelvin to celsius
            self.kelvin_to_celsius(self.temperature_input.text()) 

        elif (convert_from_index == 1 and convert_to_index == 2): # fahrenheit to kelvin
            self.fahrenheit_to_kelvin(self.temperature_input.text()) 

        elif (convert_from_index == 2 and convert_to_index == 1): # kelvin to fahrenheit
            self.kelvin_to_fahrenheit(self.temperature_input.text())
        else:
            self.conversion.setText("Something went wrong") # default error 

    def celsius_to_fahrenheit(self, temperature):
        value = (float(temperature) * 9/5) + 32
        self.conversion.setText(str(value))

    def fahrenheit_to_celsius(self, temperature):
        pass

    def celsius_to_kelvin(self, temperature):
        pass

    def kelvin_to_celsius(self, temperature):
        pass

    def fahrenheit_to_kelvin(self, temperature):
        pass

    def kelvin_to_fahrenheit(self, temperature):
        pass

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()