#Ben's a Douche #Ben's a Douche #Ben's a Douche #Ben's a Douche #Ben's a Douche #Ben's a Douche #Ben's a Douche #Ben's a Douche #Ben's a Douche
#Ben's a Douche #Ben's a Douche #Ben's a Douche #Ben's a Douche #Ben's a Douche #Ben's a Douche #Ben's a Douche #Ben's a Douche #Ben's a Douche
#Ben's a Douche #Ben's a Douche #Ben's a Douche #Ben's a Douche #Ben's a Douche #Ben's a Douche #Ben's a Douche #Ben's a Douche #Ben's a Douche
#Ben's a Douche #Ben's a Douche #Ben's a Douche #Ben's a Douche #Ben's a Douche #Ben's a Douche #Ben's a Douche #Ben's a Douche #Ben's a Douche
import sys

from database_add_dialog_class import *
from database_add_dialog_class2 import *
from database_delete_dialog_class import *

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class AppWindow(QMainWindow):
    """creates the main window"""

    #constructor
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Teacher Database Thing - also Ben Sucks") # set window title

        #toolbars
        self.name_textbox = QLineEdit("Name")
        self.id_textbox = QLineEdit("ID")
        self.add_database_push_button = QPushButton("Add")
        self.delete_database_push_button = QPushButton("Delele")
        
        #layout
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.name_textbox)
        self.layout.addWidget(self.id_textbox)
        self.layout.addWidget(self.add_database_push_button)
        self.layout.addWidget(self.delete_database_push_button)
       

        self.main_widget = QWidget()
        self.main_widget.setLayout(self.layout)
        self.setCentralWidget(self.main_widget)

        #connections
        self.add_database_push_button.clicked.connect(self.add)
        self.delete_database_push_button.clicked.connect(self.delete)


    def add(self):
        try:
            AddToDatabase.main(self)
        except sqlite3.OperationalError:
            values = AddToDatabase2.main(self,self.id_textbox.text(),self.name_textbox.text())
            AddToDatabase2.insert_data(self,values)

    def delete(self):
        data = DeleteFromDatabase.main(self,self.id_textbox.text())
        DeleteFromDatabase.delete_teacher(self,data)

def main():
    database_application = QApplication(sys.argv) #create the application
    app_window = AppWindow() #creates a new instance of the main window
    app_window.show()
    app_window.raise_()
    database_application.exec_()

if __name__ == "__main__":
    main()

#Ben's a Douche #Ben's a Douche #Ben's a Douche #Ben's a Douche #Ben's a Douche #Ben's a Douche #Ben's a Douche #Ben's a Douche 
#Ben's a Douche #Ben's a Douche #Ben's a Douche #Ben's a Douche #Ben's a Douche #Ben's a Douche #Ben's a Douche #Ben's a Douche
    #Ben's a Douche #Ben's a Douche #Ben's a Douche #Ben's a Douche #Ben's a Douche #Ben's a Douche #Ben's a Douche 
