from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QLabel,QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from auth import *


class startScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.settings()
        self.connects()
        self.show()
        
        
    def initUI(self):
        self.title = QLabel("UrbanClimber")
        self.title.setFont(QFont("Arial",45,5))
        self.text = QLabel("Are you ready to send it?")
        self.options = QLabel("Please make a selection to continue")
        self.btn_login = QPushButton("Log In")
        self.signup = QPushButton("Sign Up")
        
        self.master = QVBoxLayout()
        row = QHBoxLayout()
        self.master.addWidget(self.title,alignment=Qt.AlignCenter)
        self.master.addWidget(self.text, alignment=Qt.AlignCenter)
        self.master.addWidget(self.options, alignment=Qt.AlignCenter)
        row.addWidget(self.btn_login)
        row.addWidget(self.signup)
        self.master.addLayout(row)
        self.setLayout(self.master)
        
    
    def login_screen(self):
        self.hide()
        self.grade_screen = LogIn()
        
    def signup_screen(self):
        self.hide()
        self.next1 = SignUp()
        
    def connects(self):
        self.btn_login.clicked.connect(self.login_screen)
        self.signup.clicked.connect(self.signup_screen)
        
    def settings(self):
        self.setWindowTitle("UrbanClimber")
        self.setGeometry(500,500,300,500)
    
