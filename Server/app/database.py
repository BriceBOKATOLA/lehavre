# Create CRUD for Database in SQLite3
import sqlite3
from sqlite3 import Error

class DataBase:
    def sql_connection(db_path):
        try:
            db = sqlite3.connect(db_path)
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
            print(f"Utilisateur {data[0]} ajouté")
        except Error as e:
            print(f"Erreur lors de l'ajout de l'utilisateur: {e}")

    def DeleteUser(con, id):
        query = "DELETE FROM user WHERE id = ? RETURNING username"
        try:
            cur = con.cursor()
            cur.execute(query, (id,))
            result = cur.fetchone()

            if result:
                con.commit()
                print(f"Utilisateur {result[0]} supprimé.")
        except Error as e:
            print(f"Erreur lors de la suppression de l'utilisateur: {e}")

    def UpdateUser(con, data, id):
        query = "UPDATE user SET username = ?, pwd = ?  WHERE id = ?"
        try:
            cur = con.cursor()
            cur.execute(query, (*data, id))
            con.commit()
            print(f"Utilisateur {data[0]} modifié.")
        except Error as e:
            print(f"Erreur lors de la modification de l'utilisateur: {e}")

    def CreateEvenement(con, data):
        query = ("INSERT OR IGNORE INTO event (title, date_begin, date_end, place, event_type, organisators, description) "
                 "VALUES(?,?,?,?,?,?,?)")
        try:
            cur = con.cursor()
             # Check if the event was actually inserted
            cur.execute("SELECT EXISTS(SELECT 1 FROM event WHERE title = ? AND date_begin = ? AND place = ?)", 
                        (data[0], data[1], data[3]))
            exists = cur.fetchone()[0]  # fetchone returns a tuple
            if exists:
                print(f"L'évenement {data[0]} existe déja.")

            else:
                cur.execute(query, data)
                con.commit()
                print(f"Evenement {data[0]} a été ajouté.")
                
        except Error as e:
            print(f"Erreur lors de l'ajout de l'évenement: {e}")

    def DeleteEvenement(con, id):
        query = "DELETE FROM event WHERE id = ? RETURNING title"
        try:
            cur = con.cursor()
            cur.execute(query, (id,))
            result = cur.fetchone()

            if result:
                con.commit()
                print(f"Evenement {result[0]} supprimé.")
        except Error as e:
            print(f"Erreur lors de la suppression de l'évenement: {e}")

    def UpdateEvenement(con, data, id):
        query = "UPDATE event SET title = ?, date_begin = ? ,date_end = ? ,place = ? ,event_type = ? ,organisators = ? ,description = ?  WHERE id = ?"
        try:
            cur = con.cursor()
            cur.execute(query, (*data, id))
            con.commit()
            print(f"Evenement {data[0]} modifié.")
        except Error as e:
            print(f"Erreur lors de la modification de l'évenement: {e}")