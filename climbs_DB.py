from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtWidgets import QMessageBox
import sys


# Create a connection to the database
database = QSqlDatabase.addDatabase('QSQLITE')
database.setDatabaseName('climb_database.db')
if not database.open():
    QMessageBox.critical(None, 'Error', 'Could not open the database.')
    sys.exit(1)

# Create the expense table if it doesn't exist
query = QSqlQuery()
query.exec_("""
    CREATE TABLE IF NOT EXISTS climb_database (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        grade TEXT,
        status TEXT,
        route TEXT
    )
""")
