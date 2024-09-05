from PySide6.QtCore import Qt
from ui_main import *
from PySide6.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
import sys, os
import datetime

from cryptography.fernet import Fernet


class mainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.key = None
        self.ui.pushButton_choosefile_encrypt.clicked.connect(
            lambda: self.openfile("encrypt")
        )
        self.ui.pushButton_choosefile_decrpyt.clicked.connect(
            lambda: self.openfile("decrypt")
        )
        self.ui.pushButton_encrypt.clicked.connect(self.encrypt)
        self.ui.pushButton_randomkey.clicked.connect(self.create_key)
        self.ui.pushButton_decrypt.clicked.connect(self.decrypt)
        self.file_encrypt = None
        self.file_decrypt = None
        self.ui.textEdit.insertPlainText("logs : \n")
        
    def create_key(self):
        self.ui.lineEdit.clear()
        self.key = Fernet.generate_key()
        self.ui.lineEdit.setText(self.key.decode())

    def encrypt(self):
        if not self.file_encrypt:
            QMessageBox.critical(self, "هشدار", "فایلی برای رمزگذاری انتخاب نشده است.")
            return
        self.key = self.ui.lineEdit.text().strip().encode()
        if not self.is_valid_key(self.key):
            QMessageBox.critical(self, "هشدار", "فرمت کلید نادرست میباشد")
            return
            # Initialize Fernet with the key
        cipher_suite = Fernet(self.key)
        self.directory("en")
        for i in self.file_encrypt:
            with open(i, "rb") as file:
                file_data = file.read()
            encrypted_data = cipher_suite.encrypt(file_data)
            with open(f"./encrypted/encrypted_{ os.path.basename(i)}", "wb") as file:
                file.write(encrypted_data)
    def decrypt(self):
        if not self.file_decrypt:
            QMessageBox.critical(self, "هشدار", "فایلی برای رمزگشایی انتخاب نشده است.")
            return
        self.key = self.ui.lineEdit.text().strip().encode()
        if not self.is_valid_key(self.key):
            QMessageBox.critical(self, "هشدار", "فرمت کلید نادرست میباشد")
            return
            # Initialize Fernet with the key
        cipher_suite = Fernet(self.key)
        self.directory("de")
        for i in self.file_decrypt:
            with open(i, "rb") as file:
                file_data = file.read()
            decrpyted_file = cipher_suite.decrypt(file_data)
            with open(f"./decrypted/decrypted_{ os.path.basename(i)}", "wb") as file:
                file.write(decrpyted_file)
    def directory(self, dir):
        if dir == "en":
            if not os.path.exists("./encrypted"):
                os.mkdir("./encrypted")
        if dir == "de":
            if not os.path.exists("./decrypted"):
                os.mkdir("./decrypted")

    def openfile(self, str):
        if str == "encrypt":
            self.file_encrypt, _ = QFileDialog.getOpenFileNames(
                self, "فایل مورد نظر را انتخاب کنید"
            )
            self.ui.listWidget_filename_encrpyt.clear()
            self.ui.listWidget_fileaddress_encrypt.clear()
            # print(self.file_encrypt)
            for file_path in self.file_encrypt:
                file_name = os.path.basename(file_path)
                self.ui.listWidget_filename_encrpyt.addItem(file_name)
                self.ui.listWidget_fileaddress_encrypt.addItem(file_path)
            log_entry = (
                f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} :: "
                f"<span style='color: green;'>Encrypt Files imported Successfully</span><br>"
            )

            # Insert the HTML formatted text
            self.ui.textEdit.insertHtml(log_entry)
        if str == "decrypt":
            self.file_decrypt, _ = QFileDialog.getOpenFileNames(
                self, "فایل مورد نظر را انتخاب کنید"
            )
            self.ui.listWidget_filename_decrypt.clear()
            self.ui.listWidget_fileaddress_decrypt.clear()
            # print(self.file_encrypt)
            for file_path in self.file_decrypt:
                file_name = os.path.basename(file_path)
                self.ui.listWidget_filename_decrypt.addItem(file_name)
                self.ui.listWidget_fileaddress_decrypt.addItem(file_path)
            log_entry = (
                f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} :: "
                f"<span style='color: green;'>Decrypt Files imported Successfully</span><br>"
            )

            # Insert the HTML formatted text
            self.ui.textEdit.insertHtml(log_entry)

    def is_valid_key(self, key):
        try:
            # Ensure the key is base64-encoded and has correct length
            Fernet(key)
            return True
        except (ValueError, TypeError):
            return False


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = mainWindow()
    window.show()
    sys.exit(app.exec())
