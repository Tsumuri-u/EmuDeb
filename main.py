import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("EmuDeb")

        self.setLayout(qtw.QVBoxLayout())

        my_label = qtw.QLabel("Label")
        my_label.setFont(qtg.QFont('Helvetica', 18))
        self.layout().addWidget(my_label)

        my_entry = qtw.QLineEdit()
        my_entry.setObjectName("name_field")
        # my_entry.setText("placeholder")
        self.layout().addWidget(my_entry)

        my_button = qtw.QPushButton("Button", clicked = lambda: press_it())
        self.layout().addWidget(my_button)

        def press_it():
            my_label.setText(f'Text: {my_entry.text()}')
            my_entry.setText("")

        self.show()

app = qtw.QApplication([])
mw = MainWindow()

app.exec_()