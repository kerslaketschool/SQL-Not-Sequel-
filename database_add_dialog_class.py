import sqlite3

class AddToDatabase():

    #constructor
    def __init__(self):
       pass 

    def main(self):
        db_name = "Teacher Database.db"
        sql = """create table Teacher
              (TeacherID integer,
              Name text,
              primary key(TeacherID))"""
        with sqlite3.connect(db_name) as db:
            cursor = db.cursor()
            cursor.execute(sql)
            db.commit()
        
