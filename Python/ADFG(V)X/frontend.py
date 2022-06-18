import sys
import string
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QComboBox, QMessageBox, QRadioButton, QStyleFactory, QWidget
from back_end import *

qtcreator_file  = "gui.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    grid = ''
    generated_grid = False
    generated_grid_dec = False
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.label_5.setVisible(False)
        self.grid_input_2.setEnabled(False)
        self.grid_input_2.setVisible(False)
        self.random_2.setEnabled(False)
        self.random_2.setVisible(False)
        self.enter_2.setEnabled(False)
        self.enter_2.setVisible(False)
        self.tittle_4.setVisible(False)
        self.tittle_2.setEnabled(False)
        self.tittle_2.setVisible(False)
        self.label_5.setVisible(False)
        self.grid_input_2.setEnabled(False)
        self.grid_input_2.setVisible(False)
        self.random_2.setEnabled(False)
        self.random_2.setVisible(False)
        self.enter_2.setEnabled(False)
        self.enter_2.setVisible(False)
        self.print_grid_2.setEnabled(False)
        self.print_grid_2.setVisible(False)
        self.tittle_2.setEnabled(False)
        self.tittle_2.setVisible(False)
        self.label_12.setVisible(False)
        self.grid_input_dec_2.setEnabled(False)
        self.grid_input_dec_2.setVisible(False)
        self.dec_enter_2.setEnabled(False)
        self.dec_enter_2.setVisible(False)
        self.print_grid_4.setEnabled(False)
        self.print_grid_4.setVisible(False)
        self.groupBox_3.setEnabled(False)
        self.groupBox_3.setVisible(False)
        self.groupBox_4.setEnabled(False)
        self.groupBox_4.setVisible(False)
        self.button_1.clicked.connect(self.Enable_5x5)
        self.button_2.clicked.connect(self.Enable_6x6)
        self.enter_1.clicked.connect(self.Manual_1)
        self.random_1.clicked.connect(self.Random_1)
        self.enter_2.clicked.connect(self.Manual_2)
        self.random_2.clicked.connect(self.Random_2)
        self.enc_button.clicked.connect(self.Encode)
        self.dec_button.clicked.connect(self.Decode)
        self.button_3.clicked.connect(self.Enable_5x5_Dec)
        self.button_4.clicked.connect(self.Enable_6x6_Dec)
        self.dec_enter_1.clicked.connect(self.Manual_3)
        self.dec_enter_2.clicked.connect(self.Manual_4)
        self.button_5.clicked.connect(self.Info_1)
        self.button_6.clicked.connect(self.Info_2)
        self.exit.clicked.connect(self.Exit_Info_1)
        self.exit_2.clicked.connect(self.Exit_Info_2)

    def Info_1(self):
        self.groupBox_3.setEnabled(True)
        self.groupBox_3.setVisible(True)

    def Info_2(self):
        self.groupBox_4.setEnabled(True)
        self.groupBox_4.setVisible(True)

    def Exit_Info_1(self):
        self.groupBox_3.setEnabled(False)
        self.groupBox_3.setVisible(False)

    def Exit_Info_2(self):
        self.groupBox_4.setEnabled(False)
        self.groupBox_4.setVisible(False)

    def Enable_5x5(self):
        self.label_5.setVisible(False)
        self.grid_input_2.setEnabled(False)
        self.grid_input_2.setVisible(False)
        self.random_2.setEnabled(False)
        self.random_2.setVisible(False)
        self.enter_2.setEnabled(False)
        self.enter_2.setVisible(False)
        self.print_grid_2.setEnabled(False)
        self.print_grid_2.setVisible(False)
        self.tittle_2.setEnabled(False)
        self.tittle_2.setVisible(False)
        self.label_4.setVisible(True)
        self.grid_input.setEnabled(True)
        self.grid_input.setVisible(True)
        self.random_1.setEnabled(True)
        self.random_1.setVisible(True)
        self.enter_1.setEnabled(True)
        self.enter_1.setVisible(True)
        self.grid_1.setEnabled(True)
        self.grid_1.setVisible(True)
        self.tittle_1.setEnabled(True)
        self.tittle_1.setVisible(True)
    
    def Enable_6x6(self):
        self.label_4.setVisible(False)
        self.grid_input.setEnabled(False)
        self.grid_input.setVisible(False)
        self.random_1.setEnabled(False)
        self.random_1.setVisible(False)
        self.enter_1.setEnabled(False)
        self.enter_1.setVisible(False)
        self.grid_1.setEnabled(False)
        self.grid_1.setVisible(False)
        self.tittle_1.setEnabled(False)
        self.tittle_1.setVisible(False)
        self.label_5.setVisible(True)
        self.grid_input_2.setEnabled(True)
        self.grid_input_2.setVisible(True)
        self.random_2.setEnabled(True)
        self.random_2.setVisible(True)
        self.enter_2.setEnabled(True)
        self.enter_2.setVisible(True)
        self.print_grid_2.setEnabled(True)
        self.print_grid_2.setVisible(True)
        self.tittle_2.setEnabled(True)
        self.tittle_2.setVisible(True)

    def Enable_5x5_Dec(self):
        self.label_12.setVisible(False)
        self.grid_input_dec_2.setEnabled(False)
        self.grid_input_dec_2.setVisible(False)
        self.dec_enter_2.setEnabled(False)
        self.dec_enter_2.setVisible(False)
        self.print_grid_4.setEnabled(False)
        self.print_grid_4.setVisible(False)
        self.tittle_4.setEnabled(False)
        self.tittle_4.setVisible(False)
        self.label_11.setVisible(True)
        self.grid_input_dec_1.setEnabled(True)
        self.grid_input_dec_1.setVisible(True)
        self.dec_enter_1.setEnabled(True)
        self.dec_enter_1.setVisible(True)
        self.print_grid_3.setEnabled(True)
        self.print_grid_3.setVisible(True)
        self.tittle_3.setEnabled(True)
        self.tittle_3.setVisible(True)

    def Enable_6x6_Dec(self):
        self.label_12.setVisible(True)
        self.grid_input_dec_2.setEnabled(True)
        self.grid_input_dec_2.setVisible(True)
        self.dec_enter_2.setEnabled(True)
        self.dec_enter_2.setVisible(True)
        self.print_grid_4.setEnabled(True)
        self.print_grid_4.setVisible(True)
        self.tittle_4.setEnabled(True)
        self.tittle_4.setVisible(True)
        self.label_11.setVisible(False)
        self.grid_input_dec_1.setEnabled(False)
        self.grid_input_dec_1.setVisible(False)
        self.dec_enter_1.setEnabled(False)
        self.dec_enter_1.setVisible(False)
        self.print_grid_3.setEnabled(False)
        self.print_grid_3.setVisible(False)
        self.tittle_3.setEnabled(False)
        self.tittle_3.setVisible(False)

    def Manual_1(self):
        self.grid = self.grid_input.toPlainText()
        if len(self.grid) == 0:
            msg = QMessageBox();msg.setWindowTitle("Empty");msg.setText("Please input grid");x = msg.exec_()
        else:
            if self.check_1.isChecked():
                number,print_grid = Check_Grid(self.grid,'5x5')
                match number:
                    case 1: msg = QMessageBox();msg.setWindowTitle("Duplicates");msg.setText("There is duplicate in the grid, please remove it");x = msg.exec_()
                    case 2: msg = QMessageBox();msg.setWindowTitle("Number");msg.setText("There is number in the grid, please remove it");x = msg.exec_()
                    case 3: msg = QMessageBox();length = len(self.grid);msg.setWindowTitle("Length");msg.setText(f"Wrong length of grid, length should be 25 letters. Current length is: {length}");x = msg.exec_()
                    case 0: msg = self.grid = Fill_Grid('EN', '5x5', 'man', print_grid);self.grid_input_dec_1.setText(print_grid);print_grid = Print_Grid(print_grid,'5x5', 'man'); self.grid_1.setText(print_grid); self.generated_grid = True

            if self.check_2.isChecked():
                number,print_grid = Check_Grid(self.grid,'5x5')
                match number:
                    case 1: msg = QMessageBox();msg.setWindowTitle("Duplicates");msg.setText("There is duplicate in the grid, please remove it");x = msg.exec_()
                    case 2: msg = QMessageBox();msg.setWindowTitle("Number");msg.setText("There is number in the grid, please remove it");x = msg.exec_()
                    case 3: msg = QMessageBox();length = len(self.grid);msg.setWindowTitle("Length");msg.setText(f"Wrong length of grid, length should be 25 letters. Current length is: {length}");x = msg.exec_()
                    case 0: msg = msg = self.grid = Fill_Grid('CZ', '5x5', 'man', print_grid);self.grid_input_dec_1.setText(print_grid);print_grid = Print_Grid(print_grid,'5x5', 'man'); self.grid_1.setText(print_grid); self.generated_grid = True
           
    def Manual_2(self):
        self.grid = self.grid_input_2.toPlainText()
        if len(self.grid) == 0:
            msg = QMessageBox();msg.setWindowTitle("Empty");msg.setText("Please input grid");x = msg.exec_()
        else:
            if self.check_1.isChecked():
                number,print_grid = Check_Grid(self.grid,'6x6')
                match number:
                    case 1: msg = QMessageBox();msg.setWindowTitle("Duplicates");msg.setText("There is duplicate in the grid, please remove it");x = msg.exec_()
                    case 4: msg = QMessageBox();length = len(self.grid);msg.setWindowTitle("Length");msg.setText(f"Wrong length of grid, length should be 36 letters. Current length is: {length}");x = msg.exec_()
                    case 0: msg = msg = self.grid = Fill_Grid('EN', '6x6', 'man', print_grid);self.grid_input_dec_2.setText(print_grid); print_grid = Print_Grid(print_grid,'6x6', 'man');self.print_grid_2.setText(print_grid); self.generated_grid = True

            if self.check_2.isChecked():
                number,print_grid = Check_Grid(self.grid,'6x6')
                match number:
                    case 1: msg = QMessageBox();msg.setWindowTitle("Duplicates");msg.setText("There is duplicate in the grid, please remove it");x = msg.exec_()
                    case 4: msg = QMessageBox();length = len(self.grid);msg.setWindowTitle("Length");msg.setText(f"Wrong length of grid, length should be 36 letters. Current length is: {length}");x = msg.exec_()
                    case 0: msg = msg = self.grid = Fill_Grid('CZ', '6x6', 'man', print_grid);self.grid_input_dec_2.setText(print_grid); print_grid = Print_Grid(print_grid,'6x6', 'man');self.print_grid_2.setText(print_grid); self.generated_grid = True

    def Random_1(self):
        text = self.grid_input.toPlainText()
        if self.check_1.isChecked():
            print_grid = Fill_Grid('EN', '5x5', 'auto', text)
            for_label = ''.join(print_grid)
            self.grid_input.setText(for_label)
            self.grid = print_grid
            self.grid_input_dec_1.setText(''.join(print_grid))
            print_grid = Print_Grid(print_grid,'5x5', 'auto')
            self.grid_1.setText(print_grid)
            self.generated_grid = True
        if self.check_2.isChecked():
            print_grid = Fill_Grid('CZ', '5x5', 'auto', text)
            for_label = ''.join(print_grid)
            self.grid_input.setText(for_label)
            self.grid = print_grid
            self.grid_input_dec_1.setText(''.join(print_grid))
            print_grid = Print_Grid(print_grid,'5x5', 'auto')
            self.grid_1.setText(print_grid)
            self.generated_grid = True

    def Random_2(self):
        text = self.grid_input.toPlainText()
        if self.check_1.isChecked():   
            print_grid = Fill_Grid('EN', '6x6', 'auto', text)
            for_label = ''.join(print_grid)
            self.grid_input_2.setText(for_label)
            self.grid = print_grid
            self.grid_input_dec_2.setText(''.join(print_grid))
            print_grid = Print_Grid(print_grid,'6x6', 'auto')
            self.print_grid_2.setText(print_grid)
            self.generated_grid = True
        if self.check_2.isChecked():
            print_grid = Fill_Grid('CZ', '6x6', 'auto', text)
            for_label = ''.join(print_grid)
            self.grid_input_2.setText(for_label)
            self.grid = print_grid
            self.grid_input_dec_2.setText(''.join(print_grid))
            print_grid = Print_Grid(print_grid,'6x6', 'auto')
            self.print_grid_2.setText(print_grid)
            self.generated_grid = True

    def Encode(self):
        if len(self.grid) == 0:
            msg = QMessageBox()
            msg.setWindowTitle("Missing grid")
            msg.setText("You need to generate grid first")
            x = msg.exec_()
        if Check_Key_Length(self.input_box.toPlainText(), self.key_box_1.toPlainText()):
            print('kokot')
            msg = QMessageBox()
            msg.setWindowTitle("Wrong Key")
            msg.setText("You have inserted wrong key, for more information visit Info window and try again")
            x = msg.exec_()
        else:
            if self.check_1.isChecked():
                if(Invalid_Key(self.key_box_1.toPlainText())):
                    msg = QMessageBox()
                    msg.setWindowTitle("Wrong Key")
                    msg.setText("You have inserted wrong key, for more information visit Info window and try again")
                    x = msg.exec_()
                else:
                    input = self.input_box.toPlainText()
                    key = self.key_box_1.toPlainText()
                    subs = Substitution(input, 'EN', self.grid)
                    output = Transpose(subs, key)
                    self.output_box.setText(output)
                    self.input_box_2.setText(output)
                    self.key_box_2.setText(key)
            if self.check_2.isChecked():
                if(Invalid_Key(self.key_box_1.toPlainText())):
                    msg = QMessageBox()
                    msg.setWindowTitle("Wrong Key")
                    msg.setText("You have inserted wrong key, for more information visit Info window and try again")
                    x = msg.exec_()
                else:
                    input = self.input_box.toPlainText()
                    key = self.key_box_1.toPlainText()
                    subs = Substitution(input, 'CZ', self.grid)
                    output = Transpose(subs, key)
                    self.output_box.setText(output)
                    self.input_box_2.setText(output)
                    self.key_box_2.setText(key)

    def Manual_3(self):
        self.grid = self.grid_input_dec_1.toPlainText()
        if len(self.grid) == 0:
            msg = QMessageBox();msg.setWindowTitle("Empty");msg.setText("Please input grid");x = msg.exec_()
        else:
            if self.check_3.isChecked():
                number,print_grid = Check_Grid(self.grid,'5x5')
                match number:
                    case 1: msg = QMessageBox();msg.setWindowTitle("Duplicates");msg.setText("There is duplicate in the grid, please remove it");x = msg.exec_()
                    case 2: msg = QMessageBox();msg.setWindowTitle("Number");msg.setText("There is number in the grid, please remove it");x = msg.exec_()
                    case 3: msg = QMessageBox();length = len(self.grid);msg.setWindowTitle("Length");msg.setText(f"Wrong length of grid, length should be 25 letters. Current length is: {length}");x = msg.exec_()
                    case 0: msg = self.grid = Fill_Grid('EN', '5x5', 'man', print_grid);print_grid = Print_Grid(print_grid,'5x5', 'man'); self.print_grid_3.setText(print_grid); self.generated_grid_dec = True

            if self.check_4.isChecked():
                number,print_grid = Check_Grid(self.grid,'5x5')
                match number:
                    case 1: msg = QMessageBox();msg.setWindowTitle("Duplicates");msg.setText("There is duplicate in the grid, please remove it");x = msg.exec_()
                    case 2: msg = QMessageBox();msg.setWindowTitle("Number");msg.setText("There is number in the grid, please remove it");x = msg.exec_()
                    case 3: msg = QMessageBox();length = len(self.grid);msg.setWindowTitle("Length");msg.setText(f"Wrong length of grid, length should be 25 letters. Current length is: {length}");x = msg.exec_()
                    case 0: msg = msg = self.grid = Fill_Grid('CZ', '5x5', 'man', print_grid); print_grid = Print_Grid(print_grid,'5x5', 'man'); self.print_grid_3.setText(print_grid); self.generated_grid_dec = True

    def Manual_4(self):
        self.grid = self.grid_input_dec_2.toPlainText()
        if len(self.grid) == 0:
            msg = QMessageBox();msg.setWindowTitle("Empty");msg.setText("Please input grid");x = msg.exec_()
        else:
            if self.check_3.isChecked():
                number,print_grid = Check_Grid(self.grid,'6x6')
                match number:
                    case 1: msg = QMessageBox();msg.setWindowTitle("Duplicates");msg.setText("There is duplicate in the grid, please remove it");x = msg.exec_()
                    case 4: msg = QMessageBox();length = len(self.grid);msg.setWindowTitle("Length");msg.setText(f"Wrong length of grid, length should be 36 letters. Current length is: {length}");x = msg.exec_()
                    case 0: msg = self.grid = Fill_Grid('EN', '6x6', 'man', print_grid);print_grid = Print_Grid(print_grid,'6x6', 'man'); self.print_grid_4.setText(print_grid); self.generated_grid_dec = True

            if self.check_4.isChecked():
                number,print_grid = Check_Grid(self.grid,'6x6')
                match number:
                    case 1: msg = QMessageBox();msg.setWindowTitle("Duplicates");msg.setText("There is duplicate in the grid, please remove it");x = msg.exec_()
                    case 4: msg = QMessageBox();length = len(self.grid);msg.setWindowTitle("Length");msg.setText(f"Wrong length of grid, length should be 36 letters. Current length is: {length}");x = msg.exec_()
                    case 0: msg = msg = self.grid = Fill_Grid('CZ', '6x6', 'man', print_grid); print_grid = Print_Grid(print_grid,'6x6', 'man'); self.print_grid_4.setText(print_grid); self.generated_grid_dec = True

    def Decode(self):
        input = self.input_box_2.toPlainText()
        key = self.key_box_2.toPlainText()
        output = Decipher(input, self.grid, key)
        self.output_box_2.setText(output)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())