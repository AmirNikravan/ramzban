from PySide6.QtCore import Qt
from ui_main import *
from PySide6.QtWidgets import QMainWindow, QApplication, QFileDialog
import sys, os
import datetime


class mainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.key = b"0KROAyh6qxSWBF2ZDwRD4Ih1C4kqid7NMMY9kpaxCtY="
        self.ui.pushButton_choosefile_encrypt.clicked.connect(
            lambda: self.openfile("encrypt")
        )
        self.ui.pushButton_choosefile_decrpyt.clicked.connect(lambda: self.openfile("decrypt"))
        self.file_encrypt = None
        self.file_decrypt = None
        self.ui.textEdit.insertPlainText("logs : \n")

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
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = mainWindow()
    window.show()
    sys.exit(app.exec())
