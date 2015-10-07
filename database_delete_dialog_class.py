import sqlite3

class DeleteFromDatabase():

    #constructor

    def __init__(self):
        pass

    def delete_teacher(self,values):
        with sqlite3.connect("Teacher Database.db") as db:
            cursor = db.cursor()
            sql = "delete from Teacher where TeacherID={}".format(values)
            cursor.execute(sql)
            db.commit()
    
    def main(self,datathing):
        data = (datathing)
        return data
