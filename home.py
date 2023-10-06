from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QLabel,QVBoxLayout,QLineEdit,QComboBox, QHBoxLayout, QTableWidget, QTableWidgetItem,QDateEdit, QHeaderView
from PyQt5.QtCore import Qt, QDate
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtGui import QStandardItem, QStandardItemModel

from climbs_DB import *

class UserScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.settings()
        self.initUI()
        self.show()
        
        
    def initUI(self):
        self.route_name = QLineEdit()
        self.grade = QComboBox()
        self.grade.addItems(["V0","V1","V2","V3","V4","V5"])
        self.status_box = QComboBox()
        self.status_box.addItems(["Sent","Not Sent"])
        self.description = QLineEdit()
        self.table = QTableWidget()
        self.submit = QPushButton("Submit")
        self.delete = QPushButton("Delete")
        self.reset = QPushButton("Reset")
        self.date_box = QDateEdit()
        self.date_box.setDate(QDate.currentDate())
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["ID","Date","Grade","Status","Route"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.sortByColumn(1, Qt.DescendingOrder)
        
        
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.submit
        
        
        self.submit.clicked.connect(self.add_climb)
        self.delete.clicked.connect(self.del_climb)
        self.master = QHBoxLayout()
        self.col1 = QVBoxLayout()
        self.col2 = QVBoxLayout()
        row0 = QHBoxLayout()
        row1 = QHBoxLayout()
        row2 = QHBoxLayout()
        row3 = QHBoxLayout()
        row4 = QHBoxLayout()
        row5 = QHBoxLayout()
        row6=QHBoxLayout()
        
        row0.addWidget(QLabel("Date:"))
        row0.addWidget(self.date_box)
        row1.addWidget(QLabel("Route:"))
        row1.addWidget(self.route_name)
        row2.addWidget(QLabel("Grade:"))
        row2.addWidget(self.grade)
        row3.addWidget(QLabel("Sent Status:"))
        row3.addWidget(self.status_box)
        row4.addWidget(QLabel("Notes:"))
        row4.addWidget(self.description)
        row5.addWidget(self.delete)
        row5.addWidget(self.reset)
        
        
        self.col1.addWidget(QLabel("Enter your Send Info"))
        self.col1.addLayout(row1)
        self.col1.addLayout(row2)
        self.col1.addLayout(row3)
        self.col1.addLayout(row4)
        self.col1.addLayout(row5)
        self.col1.addWidget(self.submit)
        
        self.col2.addWidget(self.canvas)
        self.col2.addWidget(self.table)
        
        self.master.addLayout(self.col1,30)
        self.master.addLayout(self.col2,70)
        
        self.setLayout(self.master)
        

    
    def settings(self):
        self.setWindowTitle("UrbanClimber")
        self.setGeometry(500,500,800,500)
    
    def add_climb(self):
        route = self.route_name.text()
        grade = self.grade.currentText()
        #notes = self.description.text()
        date = self.date_box.date().toString("MM-dd")
        status = self.status_box.currentText()
        
        query = QSqlQuery()
        query.prepare("""
            INSERT INTO climb_database (date, grade, status, route)
            VALUES (?, ?, ?, ?)
        """)
        
        query.addBindValue(date)
        query.addBindValue(grade)
        query.addBindValue(status)
        query.addBindValue(route)
        query.exec_()
        
        self.date_box.setDate(QDate.currentDate())
        self.grade.setCurrentIndex(0)
        self.route_name.clear()
        self.status_box.setCurrentIndex(0)
        
        self.past_climbs()
        
    def del_climb(self):
        selected_row =self.table.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "No Climb Selected!","Please choose a climb to remove!")
            return

        climb_id = int(self.table.item(selected_row,0).text())
        
        confirm = QMessageBox.question(self, "Confirm?", "Are you sure?", QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.No:
            return
        
        query = QSqlQuery()
        query.prepare("DELETE FROM climb_database WHERE id = ?")
        query.addBindValue(climb_id)
        query.exec_()
        
        self.past_climbs()


    def past_climbs(self):
        self.table.setRowCount(0)
        
        query = QSqlQuery("SELECT * FROM climb_database")
        row = 0
        
        while query.next():
            climb_id = query.value(0)
            date = query.value(1)
            grade = query.value(2)
            status = query.value(3)
            route = query.value(4)
            
            delete_button = QPushButton('Delete')
            delete_button.clicked.connect(self.del_climb)
            
            self.table.insertRow(row)
            self.table.setItem(row, 0, QTableWidgetItem(str(climb_id)))
            self.table.setItem(row, 1, QTableWidgetItem(date))
            self.table.setItem(row, 2, QTableWidgetItem(grade))
            self.table.setItem(row, 3, QTableWidgetItem(status))
            self.table.setItem(row, 4, QTableWidgetItem(route))
            self.table.setCellWidget(row, 5, delete_button)
            
            row +=1
            
            
            
            
            
            
        
    
    
    