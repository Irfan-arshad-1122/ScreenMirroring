import socket
from random import randint
import pyautogui
from threading import Thread
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QLabel, QPushButton, QAction, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QRect, Qt


print("[SERVER]: STARTED")
sock = socket.socket()
sock.bind(('10.1.47.110',5001))
sock.listen()
conn, addr = sock.accept()

class Dekstop(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def ChangeImage(self):
        try:
            print("[SERVER]: CONNECTED: {0}!".format(addr[0]))
            while True:
                img_bytes = conn.recv(9999999)
                pixmap = QPixmap()
                pixmap.loadFromData(img_bytes)
                self.label.setScaledContents(True)
                self.label.resize(self.width(), self.height())
                self.label.setPixmap(pixmap)
        except ConnectionResetError:
            QMessageBox.about(self, "ERROR", "[SERVER]: The remote host forcibly terminated the existing connection!")
            conn.close()

    def initUI(self):
        self.pixmap = QPixmap()
        self.label = QLabel(self)
        self.label.resize(self.width(), self.height())
        self.setGeometry(QRect(0, 0, pyautogui.size()[0], pyautogui.size()[1]))
        #self.setFixedSize(self.width(), self.height())
        self.setWindowTitle("Wireless Screen Sharing Application")  # Updated title here
        self.start = Thread(target=self.ChangeImage, daemon=True)
        self.start.start()

        # Enable maximize and minimize buttons
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, True)
        self.setWindowFlag(Qt.WindowMinimizeButtonHint, True)
        self.setWindowState(Qt.WindowMaximized)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Dekstop()
    ex.show()
    sys.exit(app.exec())