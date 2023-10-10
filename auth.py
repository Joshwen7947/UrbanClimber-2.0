from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QCheckBox, QVBoxLayout, QHBoxLayout, QComboBox, QSpinBox

from home import *
from users_db import *

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
        self.submit1.clicked.connect(self.executeSearch)
          
    def searchDatabase(self, value1, value2):
        query = QSqlQuery()
        query.prepare("SELECT * FROM user_database WHERE username = :value1 AND password = :value2")
        query.bindValue(":value1", value1)
        query.bindValue(":value2",value2)
        query.exec_()
        
        try:
            res = []
            while query.next():
                col1_value = query.value(4)
                col2_value = query.value(5)
                
                res.append((col1_value, col2_value))
                print(res)
                
            return res
    
        except:
            QMessageBox.critical(self, "Query ERROR", "Execution failed!")
            return []
        
    def executeSearch(self):
        username = self.username_input.text()
        password = self.passcode.text()
        
        result = self.searchDatabase(username, password)
        
        if result:
            self.hide()
            self.home = UserScreen()
        else:
            QMessageBox.warning(self,"No User","User Not Found!")
        
        
    
        
        
class SignUp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.settings()
        self.connects()
        self.show()
        
        self.submit.clicked.connect(self.add_user)
        
    def initUI(self):
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Enter you Full Name...")
        self.username = QLineEdit()
        self.username.setPlaceholderText("Enter you a username...")
        self.create_password = QLineEdit()
        self.create_password.setPlaceholderText("Create a Password...")
        self.age = QSpinBox()
        self.email = QLineEdit()
        self.email.setPlaceholderText("Enter you Email...")
        self.submit = QPushButton("Create Account")
        
        self.master = QVBoxLayout()
        
        
        row1 = QHBoxLayout()
        row2 = QHBoxLayout()
        row3 = QHBoxLayout()
        row4 = QHBoxLayout()
        row5 = QHBoxLayout()
        
        row1.addWidget(QLabel("Name:"))
        row1.addWidget(self.name_input)
        row2.addWidget(QLabel("Username:"))
        row2.addWidget(self.username)
        row3.addWidget(QLabel("Password:"))
        row3.addWidget(self.create_password)
        row4.addWidget(QLabel("Age:"))
        row4.addWidget(self.age)
        row5.addWidget(QLabel("Email Address:"))
        row5.addWidget(self.email)
        
        self.master.addLayout(row1)
        self.master.addLayout(row2)
        self.master.addLayout(row3)
        self.master.addLayout(row4) 
        self.master.addLayout(row5)
        self.master.addWidget(self.submit)
        
        self.setLayout(self.master)
        
    def settings(self):
        self.setWindowTitle("UrbanClimber")
        self.setGeometry(500,500,300,500)
        
    def next(self):
        self.hide()
        self.user_screen = UserScreen()
        
    def connects(self):
        self.submit.clicked.connect(self.add_user)
        
        
    def add_user(self):
        name = self.name_input.text()
        age = self.age.value()
        email = self.email.text()
        username = self.username.text()
        password = self.create_password.text()
        
        query = QSqlQuery()
        query.prepare("""
            INSERT INTO user_database (name, age, email, username, password)
            VALUES (?, ?, ?, ?, ?)
        """)     
           
        query.addBindValue(name)
        query.addBindValue(age)
        query.addBindValue(email)
        query.addBindValue(username)
        query.addBindValue(password)
        print("All Values Binded")
        query.exec_()
        print("Query has been executed")
        
        
        self.name_input.clear()
        self.age.clear()
        self.email.clear()
        self.username.clear()
        self.create_password.clear()
        
        self.next()
        print("next() function has been called")