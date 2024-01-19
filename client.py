import socket
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton, QMessageBox, QDesktopWidget
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt
from PIL import ImageGrab
import io

class Dekstop(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.device_name_to_ip = {"AsharibPC": "10.1.31.84"}

    def StartThread(self):
        entered_device_name = self.device_name.text()
        if entered_device_name in self.device_name_to_ip:
            try:
                ip_address = self.device_name_to_ip.get(entered_device_name, None)
                sock = socket.socket()
                sock.connect((ip_address, 5001))
                print(f"Connected to {ip_address}")
                while True:
                    img = ImageGrab.grab()
                    img_bytes = io.BytesIO()
                    img.save(img_bytes, format='PNG')
                    sock.send(img_bytes.getvalue())
                sock.close()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Connection failed: {str(e)}")
        else:
            QMessageBox.warning(self, "Invalid Device Name", "Error: Device name not found. Please enter a valid device name.")

    def initUI(self):
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        main_text_label = QLabel("Screen Mirroring", self)
        main_text_label.setAlignment(Qt.AlignCenter)
        font = QFont("Arial", 16, QFont.Bold)
        main_text_label.setFont(font)
        layout.addWidget(main_text_label)

        # Add logo
        logo_label = QLabel(self)
        logo_pixmap = QPixmap("E:\CN\Screen Sharing Project\log.png")
        logo_label.setPixmap(logo_pixmap)
        logo_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(logo_label)

        self.device_name = QLineEdit(self)
        self.device_name.setPlaceholderText("Device Name")

        # Increase the font size for the device name input
        font_device_name = QFont("Times New Roman", 16, QFont.Bold)
        self.device_name.setFont(font_device_name)

        layout.addWidget(self.device_name)

        self.btn = QPushButton("Start Demo", self)
        self.btn.clicked.connect(self.StartThread)
        layout.addWidget(self.btn)

        central_widget.setStyleSheet("""
            QLineEdit {
                padding: 8px;
                font-size: 14px;
                border: 2px solid #3498db;
                border-radius: 5px;
            }
            QPushButton {
                padding: 10px;
                font-size: 16px;
                background-color: #3498db;
                color: #ffffff;
                border: 2px solid #3498db;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #2980b9;
                border: 2px solid #2980b9;
            }
        """)

        # Center the window on the screen
        self.centerWindow()

        self.setWindowTitle("VisualConnect")

    def centerWindow(self):
        # Get the screen geometry
        screen_geometry = QDesktopWidget().screenGeometry()

        # Calculate the center of the screen
        center_x = screen_geometry.width() // 2
        center_y = screen_geometry.height() // 2

        # Set the window position to the center
        self.setGeometry(center_x - self.width() // 2, center_y - self.height() // 2, 400, 250)

if __name__ == '__main__':
    app = QApplication([])
    ex = Dekstop()
    ex.show()
    sys.exit(app.exec())
