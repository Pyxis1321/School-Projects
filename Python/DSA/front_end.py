import sys
import string
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox, QStyleFactory, QWidget, QDialog, QFileDialog, QApplication
from back_end import *
import base64
from zipfile import ZipFile
import os
import time

qtcreator_file  = "./gui.ui" # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    key_ok = True
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.g_box.setEnabled(False)
        self.g_box.setVisible(False)
        self.info_box.setEnabled(False)
        self.info_box.setVisible(False)
        self.generate_button.clicked.connect(self.get_Keys)
        self.browse1.clicked.connect(self.Get_Input_File)
        self.encript.clicked.connect(self.Encript)
        self.browse2.clicked.connect(self.Get_E)
        self.browse3.clicked.connect(self.Get_D)
        self.browse4.clicked.connect(self.Get_N)
        self.browse5.clicked.connect(self.Get_Orig_File)
        self.browse6.clicked.connect(self.Get_Enc_File)
        self.decrypt_button.clicked.connect(self.Decrypt_File)
        self.control_button.clicked.connect(self.Control)
        self.browse7.clicked.connect(self.Get_Zip)
        self.unzip.clicked.connect(self.Unzip)
        self.info_button.clicked.connect(self.Show_File_Info)
        self.exit_button.clicked.connect(self.Hide_File_Info)
        self.info_button_2.clicked.connect(self.Show_Info)
        self.exit_button_2.clicked.connect(self.Hide_Info)


    def get_Keys(self):
        p,q,e,n,d = Generate_Keys()
        self.e_box.setText(str(e))
        self.d_box.setText(str(d))
        self.n_box.setText(str(n))

    def Get_Input_File(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', './')
        self.input_file.setText(fname[0])
        file = open(fname[0], 'rb')
        try:
            to_read = file.read()
            self.input_box.setText(str(to_read))
            hash = Get_Hash(fname[0])
            self.input_box_2.setText(hash)
        except:
            print(traceback.format_exc())
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("This file doesn't wotk, try different format.")
            x = msg.exec_()
        

    def Get_E(self):
        E_path = QFileDialog.getOpenFileName(self, 'Open file', './', '*.priv')
        self.e_box_2.setText(E_path[0])
    def Get_D(self):
        D_path = QFileDialog.getOpenFileName(self, 'Open file', './', '*.pub')
        self.d_box_2.setText(D_path[0])
    def Get_N(self):
        E_path = QFileDialog.getOpenFileName(self, 'Open file', './', '*.key')
        self.n_box_2.setText(E_path[0])
    def Get_Orig_File(self):
        orig_file = QFileDialog.getOpenFileName(self, 'Open file', './')
        self.original_file.setText(orig_file[0])
    def Get_Enc_File(self):
        enc_file = QFileDialog.getOpenFileName(self, 'Open file', './', '*.sign')
        self.encrypted_file.setText(enc_file[0])
    def Get_Zip(self):
        zip_file = QFileDialog.getOpenFileName(self, 'Open file', './', '*.zip')
        self.zip_box.setText(zip_file[0])
    def Unzip(self):
        zip = ZipFile(self.zip_box.toPlainText())
        zip.extractall()
    def Show_File_Info(self):
        output = self.decrypted_data.toPlainText()

        if(len(output) == 0):
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("First enter all required data bellow and decrypt")
            x = msg.exec_()
        else:
            self.g_box.setEnabled(True)
            self.g_box.setVisible(True)
    def Hide_File_Info(self):
        self.g_box.setEnabled(False)
        self.g_box.setVisible(False)
    def Show_Info(self):
        self.info_box.setEnabled(True)
        self.info_box.setVisible(True)
    def Hide_Info(self):
        self.info_box.setEnabled(False)
        self.info_box.setVisible(False)

    def Encript(self):
        e = self.e_box.toPlainText()
        n = self.n_box.toPlainText()
        d = self.d_box.toPlainText()
        path = self.input_file.toPlainText()
        if(len(e) == 0 or len(n) == 0 or len(d) == 0):
            msg = QMessageBox()
            msg.setWindowTitle("Empty key")
            msg.setText("You need to fill out all the keys")
            x = msg.exec_()

        if(len(path) == 0):
            msg = QMessageBox()
            msg.setWindowTitle("Invalid path")
            msg.setText("Please select path to your file")
            x = msg.exec_()

        else:
            enc_hash = Encrypt(self.input_box_2.toPlainText(), e,int(n),int(d))

            Save_Data(e,d,n,enc_hash)

            for i in range(len(enc_hash)):
                enc_hash[i] = str(enc_hash[i])
        
            enc_hash = " ".join(enc_hash)


            hash_base = base64.b64encode(enc_hash.encode())
            self.output_box.setText(enc_hash)
            self.output_box_2.setText(str(hash_base))

            msg = QMessageBox()
            msg.setWindowTitle("Saved")
            msg.setText("Your keys and encrypted data were saved in .zip file")
            x = msg.exec_()

    def Decrypt_File(self):
        e_path = self.e_box_2.toPlainText()
        n_path = self.n_box_2.toPlainText()
        d_path = self.d_box_2.toPlainText()
        enc_data = self.encrypted_file.toPlainText()

        if((len(e_path) == 0 or e_path[0].isdigit()) or (len(n_path) == 0 or n_path[0].isdigit()) or (len(d_path) == 0 or d_path[0].isdigit()) or (len(enc_data) == 0 or enc_data[0].isdigit())):
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("You keys or encypted file are either missing or in wrong format")
            x = msg.exec_()
        else:
            try:
                self.name1.setText(os.path.basename(e_path))
                self.path1.setText(e_path)
                name,ext = os.path.splitext(e_path)
                self.type1.setText(ext)
                self.size1.setText(str(os.path.getsize(e_path)))
                e_mod = os.path.getctime(e_path)
                modificationTime = time.ctime(e_mod)
                self.modified1.setText(modificationTime)

                self.name2.setText(os.path.basename(d_path))
                self.path2.setText(d_path)
                name,ext = os.path.splitext(d_path)
                self.type2.setText(ext)
                self.size2.setText(str(os.path.getsize(d_path)))
                d_mod = os.path.getctime(d_path)
                modificationTime = time.ctime(d_mod)
                self.modified2.setText(modificationTime)

                self.name3.setText(os.path.basename(n_path))
                self.path3.setText(n_path)
                name,ext = os.path.splitext(n_path)
                self.type3.setText(ext)
                self.size3.setText(str(os.path.getsize(n_path)))
                n_mod = os.path.getctime(n_path)
                modificationTime = time.ctime(n_mod)
                self.modified3.setText(modificationTime)

                self.name4.setText(os.path.basename(enc_data))
                self.path4.setText(enc_data)
                name,ext = os.path.splitext(enc_data)
                self.type4.setText(ext)
                self.size4.setText(str(os.path.getsize(enc_data)))
                data_mod = os.path.getctime(enc_data)
                modificationTime = time.ctime(data_mod)
                self.modified4.setText(modificationTime)

                e,n,d,data = Decrypt_Base64(e_path, n_path, d_path,enc_data)
                self.e_box_2.setText(e)
                self.d_box_2.setText(d)
                self.n_box_2.setText(n)
                self.encrypted_file.setText(data)

                data = data.split()
                for i in range(len(data)):
                    data[i] = int(data[i])
                decrypted = Decrypt(data,int(n),int(e))
                self.decrypted_data.setText(decrypted)
            except:
                    msg = QMessageBox()
                    msg.setWindowTitle("Error")
                    msg.setText("Something went wrong, please try again.")
                    x = msg.exec_()

    def Control(self):
        orig_file = self.original_file.toPlainText()
        dec_file = self.decrypted_data.toPlainText()

        if((len(orig_file) == 0 or orig_file[0].isdigit()) or len(dec_file) == 0 ):
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Path to file is either missing or in wrong format")
            x = msg.exec_()
        else:
            try:
                orig_oppened = open(orig_file, 'rb').read()
                to_hash = hashlib.sha512(orig_oppened).hexdigest()

                check = Control_Data(dec_file, to_hash)
                if(check):
                    msg = QMessageBox()
                    msg.setWindowTitle("Match")
                    msg.setText("Your original and encrypted file match")
                    x = msg.exec_()
                if(check == False):
                    msg = QMessageBox()
                    msg.setWindowTitle("Missmatch")
                    msg.setText("Your file migh have been tempered with or corupted")
                    x = msg.exec_()
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