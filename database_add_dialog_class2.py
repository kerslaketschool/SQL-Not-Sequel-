import sqlite3

class AddToDatabase2():

    #constructor
    def __init__(self):
        pass

    def insert_data(self,values):
        with sqlite3.connect("Teacher Database.db") as db:
            cursor = db.cursor()
            sql = "insert into Teacher (TeacherID, Name) values (?,?)"
            cursor.execute(sql,values)
            db.commit()

    def main(self,tid, n):
        teacher = (tid, n)
        return teacher
            

