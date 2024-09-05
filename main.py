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
        try:
            self.log("orange", f"generating key")
            self.ui.lineEdit.clear()
            self.key = Fernet.generate_key()
            self.ui.lineEdit.setText(self.key.decode())
            self.log("green", f"key created successfully")
        except Exception as e:
            self.error(f"Generate Key :{e}")

    def encrypt(self):
        try:
            if not self.file_encrypt:
                QMessageBox.critical(
                    self, "هشدار", "فایلی برای رمزگذاری انتخاب نشده است."
                )
                self.log("red", "فایلی برای رمزگذاری وجود ندارد")
                return
            self.key = self.ui.lineEdit.text().strip().encode()
            if not self.is_valid_key(self.key):
                QMessageBox.critical(self, "هشدار", "فرمت کلید نادرست میباشد")
                self.log("red", "فرمت کلید نادرست میباشد")
                return
                # Initialize Fernet with the key
            cipher_suite = Fernet(self.key)
            self.directory("en")
            for i in self.file_encrypt:
                with open(i, "rb") as file:
                    file_data = file.read()
                    self.log("orange", f"loading { os.path.basename(i)}")
                encrypted_data = cipher_suite.encrypt(file_data)
                with open(
                    f"./encrypted/encrypted_{ os.path.basename(i)}", "wb"
                ) as file:
                    self.log("green", f" {os.path.basename(i)} encrypted successfully")
                    file.write(encrypted_data)
            QMessageBox.warning(self, "تایید", "فایل ها با موفقیت رمزگذاری شدند.")
        except Exception as e:
            self.error(f"Encrpyt :{e}")

    def decrypt(self):
        try:
            if not self.file_decrypt:
                QMessageBox.critical(
                    self, "هشدار", "فایلی برای رمزگشایی انتخاب نشده است."
                )
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
                    self.log("orange", f"loading { os.path.basename(i)}")
                    file_data = file.read()
                decrpyted_file = cipher_suite.decrypt(file_data)
                with open(
                    f"./decrypted/decrypted_{ os.path.basename(i)}", "wb"
                ) as file:
                    self.log("green", f" {os.path.basename(i)} decrypted successfully")
                    file.write(decrpyted_file)

        except Exception as e:
            self.error(f"inputed file(s) are not encrpyted{e}")

    def directory(self, dir):
        try:
            if dir == "en":
                if not os.path.exists("./encrypted"):
                    self.log("red", "encrpyted folder not found")
                    self.log("orange", "creating encrypted folder")
                    os.mkdir("./encrypted")
                    self.log("green", "encrypted dir created successfully.")
                    return
                self.log("green", "encrpyted folder found")
            if dir == "de":
                if not os.path.exists("./decrypted"):
                    self.log("red", "decrypted folder not found")
                    self.log("orange", "creating decrypted folder")
                    os.mkdir("./decrypted")
                    self.log("green", "decrypted dir created successfully.")
                    return
                self.log("green", "decrypted folder found")
        except Exception as e:
            self.error(f"Directory {e}")

    def openfile(self, str):
        try:
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
                    self.log("green", f"{file_name}imported Successfully")

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
                    self.log("green", f"{file_name}imported Successfully")

        except Exception as e:
            self.error(f"Open File{e}")

    def is_valid_key(self, key):
        try:
            self.log("orange", "validating input key")
            # Ensure the key is base64-encoded and has correct length
            Fernet(key)
            self.log("green", "key is valid")
            return True
        except (ValueError, TypeError):
            self.log("red", "key is invalid")
            self.error(f"Validation Key")
            return False

    def error(self, msg):
        log_entry = (
            f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : "
            f"<span style='color: red;'>{msg}.</span><br>"
        )
        self.ui.textEdit.insertHtml(log_entry)

    def log(self, color, msg):
        log_entry = (
            f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : "
            f"<span style='color: {color};'>{msg}.</span><br>"
        )
        self.ui.textEdit.insertHtml(log_entry)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = mainWindow()
    window.show()
    sys.exit(app.exec())
