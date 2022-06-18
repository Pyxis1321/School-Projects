import sys
import string
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox, QStyleFactory, QWidget
from a_c import *

qtcreator_file  = "./gui.ui" # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    key_ok = True
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #self.enter_box_c.clicked.connect(self.Cipher_UI)
        self.enter_box_d.clicked.connect(self.Decipher_UI)
        self.enter_box_c.clicked.connect(self.Check_Key)

    """
    def Cipher_UI(self):
        output = Cypher(self.input_box_c.toPlainText(), self.key_a_c.value(), self.key_b_c.value())
        self.output_box_c.setText(output)
        self.key_a_d.setValue(self.key_a_c.value())
        self.key_b_d.setValue(self.key_b_c.value())
    """
    def Decipher_UI(self):
        output = Decypher(self.input_box_d.toPlainText(), self.key_a_d.value(), self.key_b_d.value())
        self.output_box_d.setText(output)

    def Check_Key(self, item):
        if(Key_Control(self.key_a_c.value())):
            msg = QMessageBox()
            msg.setWindowTitle("Wrong Input")
            msg.setText("You have inputed wrong a key, for more information visit Info window and try again")
            key_ok = False
            x = msg.exec_()
        else:
            output = Cypher(self.input_box_c.toPlainText(), self.key_a_c.value(), self.key_b_c.value())
            self.output_box_c.setText(output)
            self.key_a_d.setValue(self.key_a_c.value())
            self.key_b_d.setValue(self.key_b_c.value()) 
            #self.enter_box_c.clicked.connect(self.Cipher_UI)
            n_text = Normalize_Data(self.input_box_c.toPlainText())
            self.normalized_text.setText(n_text)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())