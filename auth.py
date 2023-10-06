from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QCheckBox, QVBoxLayout, QHBoxLayout, QComboBox

from home import *

class LogIn(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.settings()
        self.connects()
        self.show()
    
    def initUI(self):
        self.username_input = QLineEdit()
        self.passcode = QLineEdit()
        self.submit1 = QPushButton("Log In")
        
      
        self.master = QVBoxLayout()
        row1 = QHBoxLayout()
        row2 = QHBoxLayout()
        
        row1.addWidget(QLabel("Username:"))
        row1.addWidget(self.username_input)
        row2.addWidget(QLabel("Passcode:"))
        row2.addWidget(self.passcode)
        
        self.master.addLayout(row1)
        self.master.addLayout(row2)
        self.master.addWidget(self.submit1)
        self.setLayout(self.master)
        
    
    def settings(self):
        self.setWindowTitle("UrbanClimber")
        self.setGeometry(500,500,300,500)
        
    def next(self):
        self.hide()
        self.user_screen = UserScreen()
    
    def connects(self):
        self.submit1.clicked.connect(self.next)
        
        
class SignUp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.settings()
        self.connects()
        self.show()
        
    def initUI(self):
        self.name_input = QLineEdit()
        self.age = QLineEdit()
        self.email = QLineEdit()
        self.submit = QPushButton("Create Account")
        
        self.master = QVBoxLayout()
        
        row1 = QHBoxLayout()
        row2 = QHBoxLayout()
        row3 = QHBoxLayout()
        
        row1.addWidget(QLabel("Name:"))
        row1.addWidget(self.name_input)
        row2.addWidget(QLabel("Age:"))
        row2.addWidget(self.age)
        row3.addWidget(QLabel("Email Address:"))
        row3.addWidget(self.email)
        
        self.master.addLayout(row1)
        self.master.addLayout(row2)
        self.master.addLayout(row3)
        self.master.addWidget(self.submit)
        
        self.setLayout(self.master)
        
    def settings(self):
        self.setWindowTitle("UrbanClimber")
        self.setGeometry(500,500,300,500)
        
    def next(self):
        self.hide()
        self.user_screen = UserScreen()
        
    def connects(self):
        self.submit.clicked.connect(self.next)
        