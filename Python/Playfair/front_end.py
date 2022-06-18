import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox, QStyleFactory, QWidget
from back_end import *

qtcreator_file = ".\gui.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    key_ok = True
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.enter_box_1.clicked.connect(self.Encrypt)
        self.enter_box_2.clicked.connect(self.Decrypt)

    def Decrypt(self):
        if self.check_d_1.isChecked():
            output = Decipher(self.input_box_2.toPlainText(), 'EN', self.key_box_2.toPlainText())
            self.output_box_2.setText(output)
        if self.check_d_2.isChecked():
            output = Decipher(self.input_box_2.toPlainText(), 'CZ', self.key_box_2.toPlainText())
            self.output_box_2.setText(output)
            
    def Encrypt(self):
        if(Invalid_Input(self.input_box_1.toPlainText())):
            msg = QMessageBox()
            msg.setWindowTitle("Wrong Input")
            msg.setText("You have insrted wrong input, for more information visit Info window and try again")
            x = msg.exec_()
        if(Invalid_Key(self.key_box_1.toPlainText())):
            msg = QMessageBox()
            msg.setWindowTitle("Wrong Key")
            msg.setText("You have inserted wrong key, for more information visit Info window and try again")
            x = msg.exec_()
        else:
            if self.check_e_1.isChecked():
                output,grid = Cipher(self.input_box_1.toPlainText(), 'EN', self.key_box_1.toPlainText())
                self.output_box_1.setText(output)
                text_to_output = self.output_box_1.toPlainText()
                self.input_box_2.setText(text_to_output)
                n_input = Normalize_Data(self.input_box_1.toPlainText())
                self.n_input.setText(n_input)
                n_key = Find_Duplicates(self.key_box_1.toPlainText())
                self.n_key.setText(n_key)
                self.key_box_2.setText(n_key)
                self.label_13.setText(grid)
            elif self.check_e_2.isChecked():
                output,grid = Cipher(self.input_box_1.toPlainText(), 'CZ', self.key_box_1.toPlainText())
                self.output_box_1.setText(output)
                text_to_output = self.output_box_1.toPlainText()
                self.input_box_2.setText(text_to_output)
                n_input = Normalize_Data(self.input_box_1.toPlainText())
                self.n_input.setText(n_input)
                n_key = Find_Duplicates(self.key_box_1.toPlainText())
                self.n_key.setText(n_key)
                self.key_box_2.setText(n_key) 
                self.label_13.setText(grid)
                
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())