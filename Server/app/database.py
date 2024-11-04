# Create CRUD for Database in SQLite3
import sqlite3
from sqlite3 import Error

class DataBase:
    def sql_connection(self):
        try:
            db = sqlite3.connect(self.db_path)
            return db
        except Error:
            print(Error)
    
    def sql_close(con):
        try:
            con.close()
        except Error:
            print(Error)

    def CreateUser(con, data):
        query = "INSERT INTO user (username, pwd) VALUES(?,?)"
        try:
            cur = con.cursor()
            cur.execute(query, data)
            con.commit()
            print("Utilisateur ajouté.")
        except Error:
            print(Error)

    def DeleteUser(con, data):
        query = "DELETE FROM user WHERE username = ?;"
        try:
            cur = con.cursor()
            cur.execute(query, (data,))
            con.commit()
            print("Utilisateur supprimé.")
        except Error:
            print(Error)

    def ModifyUser(con, data, id):
        query = "UPDATE user SET username = ?, pwd = ?  WHERE id = ?"
        try:
            cur = con.cursor()
            cur.execute(query, (data, id))
            con.commit()
            print("Utilisateur modifié.")
        except Error:
            print(Error)

    def CreateEvenement(con, data):
        query = "INSERT INTO event (title, date_begin, date_end, place, event_type, organisators, description) VALUES(?,?,?,?,?,?,?)"
        try:
            cur = con.cursor()
            cur.execute(query, data)
            con.commit()
            print("Evenement ajouté.")
        except Error:
            print(Error)

    def DeleteEvenement(con, id):
        query = "DELETE FROM event WHERE id = ?;"
        try:
            cur = con.cursor()
            cur.execute(query, (id,))
            con.commit()
            print("Evenement supprimé.")
        except Error:
            print(Error)

    def ModifyEvenement(con, data, id):
        query = "UPDATE event SET title = ?, date_begin = ? ,date_end = ? ,place = ? ,event_type = ? ,organisators = ? ,description = ?  WHERE id = ?"
        try:
            cur = con.cursor()
            cur.execute(query, (data, id))
            con.commit()
            print("Evenement modifié.")
        except Error:
            print(Error)