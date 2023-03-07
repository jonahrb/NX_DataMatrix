from PyQt5.QtWidgets import QDialog, QVBoxLayout, QGroupBox, QLineEdit, QLabel, QSpacerItem, QPushButton, QFormLayout, QApplication
from PyQt5.QtGui import QPixmap, QIcon
import sys
import os
from pylibdmtx.pylibdmtx import encode
from PIL import Image


class Window(QDialog):

    def __init__(self):
        super(Window, self).__init__()
        self.setWindowIcon(QIcon('logo.ico'))
        self.setWindowTitle("Neuplex DataMatrix Generator")
        self.setGeometry(100, 100, 600, 900)

        mainLayout = QVBoxLayout()

        self.formGroupBox = QGroupBox("Enter Values:")

        self.lot_number_field = QLineEdit()
        self.lot_number_field.setMaxLength(20)
        self.lot_number_label = QLabel()
        self.spacer1 = QSpacerItem(0, 0)

        self.operator_id_field = QLineEdit()
        self.lot_number_field.setMaxLength(20)
        self.operator_id_label = QLabel()
        self.spacer2 = QSpacerItem(0, 0)

        self.part_number_field = QLineEdit()
        self.lot_number_field.setMaxLength(20)
        self.part_number_label = QLabel()

        self.createForm()

        self.generate_button = QPushButton("Generate", self)
        self.generate_button.geometry()
        self.generate_button.clicked.connect(self.generate)

        mainLayout.addWidget(self.generate_button)
        mainLayout.addWidget(self.formGroupBox)

        self.setLayout(mainLayout)

    def generate(self):

        lot_number_text = self.lot_number_field.text()
        operator_id_text = self.operator_id_field.text()
        part_number_text = self.part_number_field.text()

        self.create_data_matrices(
            lot_number_text, operator_id_text, part_number_text)

        self.lot_number_dm = QPixmap("./WF4.png").scaled(150, 150)
        self.lot_number_label.setPixmap(self.lot_number_dm)
        self.spacer1.changeSize(0, 100)

        self.operator_id_dm = QPixmap("./WF5.png").scaled(150, 150)
        self.operator_id_label.setPixmap(self.operator_id_dm)
        self.spacer2.changeSize(0, 100)

        self.part_number_dm = QPixmap("./WF10.png").scaled(150, 150)
        self.part_number_label.setPixmap(self.part_number_dm)

    def createForm(self):

        layout = QFormLayout()

        layout.addRow(QLabel("Lot Number"), self.lot_number_field)
        layout.addWidget(self.lot_number_label)
        layout.addItem(self.spacer1)

        layout.addRow(QLabel("ID"), self.operator_id_field)
        layout.addWidget(self.operator_id_label)
        layout.addItem(self.spacer2)

        layout.addRow(QLabel("Part Number"), self.part_number_field)
        layout.addWidget(self.part_number_label)

        self.formGroupBox.setLayout(layout)

    def create_data_matrices(self, str1="", str2="", str3=""):
        if str1 != "":
            try:
                encoded = encode(f'WF4-{str1}'.encode('utf8'))
                img = Image.frombytes(
                    'RGB', (encoded.width, encoded.height), encoded.pixels)
                img.save('WF4.png')
            except:
                print("Failed to generate lot number datamatrix.")

        if str2 != "":
            try:
                encoded = encode(f'WF5-{str2}'.encode('utf8'))
                img = Image.frombytes(
                    'RGB', (encoded.width, encoded.height), encoded.pixels)
                img.save('WF5.png')
            except:
                print("Failed to generate lot number datamatrix.")
        if str3 != "":
            try:
                encoded = encode(f'WF10-{str3}'.encode('utf8'))
                img = Image.frombytes(
                    'RGB', (encoded.width, encoded.height), encoded.pixels)
                img.save('WF10.png')
            except:
                print("Failed to generate text datamatrix.")


def cleanup():
    if os.path.exists("WF4.png"):
        os.remove("WF4.png")
    if os.path.exists("WF5.png"):
        os.remove("WF5.png")
    if os.path.exists("WF10.png"):
        os.remove("WF10.png")


if __name__ == '__main__':

    cleanup()

    app = QApplication(sys.argv)

    window = Window()
    window.show()

    app.exec()

    cleanup()

    sys.exit(0)
