import sys
import string
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox, QStyleFactory, QWidget
from back_end import *
from sympy import *

qtcreator_file  = "gui.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.groupBox_4.setEnabled(False)
        self.groupBox_4.setVisible(False)
        self.generate_button.clicked.connect(self.get_Keys)
        self.enter_button.clicked.connect(self.Enter)
        self.enter_button_2.clicked.connect(self.Info_Enable)
        self.enter_button_3.clicked.connect(self.Info_Dissable)

    def Info_Enable(self):
        self.groupBox_4.setEnabled(True)
        self.groupBox_4.setVisible(True)
        self.enter_button_3.setEnabled(True)
        self.enter_button_3.setVisible(True)

    def Info_Dissable(self):
        self.groupBox_4.setEnabled(False)
        self.groupBox_4.setVisible(False)
        self.enter_button_3.setEnabled(False)
        self.enter_button_3.setVisible(False)

    def get_Keys(self):
        p,q,e,n,d = Generate_Keys()
        self.e_box.setText(str(e))
        self.d_box.setText(str(d))
        self.n_box.setText(str(n))

    def Enter(self):
        user_input = self.input_box.toPlainText()
        e = self.e_box.toPlainText()
        n = self.n_box.toPlainText()
        d = self.d_box.toPlainText()
        if(len(e) == 0 or len(n) == 0 or len(d) == 0):
            msg = QMessageBox()
            msg.setWindowTitle("Missing component")
            msg.setText("Your are missing one of the components for encryption/decryption")
            x = msg.exec_()
        elif len(user_input) < 2:
            msg = QMessageBox()
            msg.setWindowTitle("Wrong length")
            msg.setText("Input needs to be at least 2 characters long")
            x = msg.exec_()
        else:
            if self.encrypt_check.isChecked():
                output = Encrypt(user_input,int(e),int(n),int(d))
                output = ' '.join([str(s) for s in output])
                self.output_box.setText(output)
            if self.decrypt_check.isChecked():
                try:
                    user_input = user_input.split(' ')
                    user_input = [int(s) for s in user_input]
                    output = Decrypt(user_input, int(n),int(d))
                    self.output_box.setText(output)
                except:
                    msg = QMessageBox()
                    msg.setWindowTitle("Error")
                    msg.setText("Something went wrong, please try again.")
                    x = msg.exec_()



        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())