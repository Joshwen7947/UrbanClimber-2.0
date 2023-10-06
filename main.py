from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QLabel,QVBoxLayout
from PyQt5.QtCore import Qt
from start_screen import *
from climbs_DB import *

class HomeScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.settings()
        self.connects()
        self.show()
        
        
    def initUI(self):
        self.text = QLabel("Welcome to UrbanClimber!")
        self.submit = QPushButton("Click Me!")
        
        self.master = QVBoxLayout()
        self.master.addWidget(self.text, alignment=Qt.AlignCenter)
        self.master.addWidget(self.submit, alignment=Qt.AlignCenter)
        self.setLayout(self.master)
        
    def settings(self):
        self.setWindowTitle("UrbanClimber")
        self.setGeometry(500,500,300,500)
        
    def connects(self):
        self.submit.clicked.connect(self.next)
        
    
    def next(self):
        self.hide()
        self.scr2 = SecondScreen()
        
        
if __name__ in "__main__":
    app = QApplication([])
    main = HomeScreen()
    main.show()
    app.exec_()