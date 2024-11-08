# Create CRUD for Database in SQLite3
import sqlite3
from sqlite3 import Error
from datetime import datetime, timedelta

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
        query = "INSERT OR IGNORE INTO user (username, pwd) VALUES(?,?)"
        try:
            cur = con.cursor()
             # Check if the event was actually inserted
            cur.execute("SELECT EXISTS(SELECT 1 FROM user WHERE username = ?)", 
                        (data[0],))
            exists = cur.fetchone()[0]  # fetchone returns a tuple

            if exists:
                print(f"L'utilisateur {data[0]} existe déjà.")
            else:
                cur.execute(query, data)
                con.commit()
                print(f"Utilisateur {data[0]} ajouté")

        except Error as e:
            print(f"Erreur lors de l'ajout de l'utilisateur: {e}")

    def DeleteUser(con, id):
        query = "DELETE FROM user WHERE id = ? RETURNING username"
        try:
            cur = con.cursor()
            cur.execute("SELECT username FROM user WHERE id = ?", (id,))
            resultSelect = cur.fetchone()

            if resultSelect:  # Si l'utilisateur existe
                cur.execute(query, (id,))
                resultDelete = cur.fetchone()

                if resultDelete:
                    con.commit()
                    print(f"Utilisateur {resultDelete[0]} supprimé.")

            else:
                print("L'utilisateur n'existe pas.")

        except Error as e:
            print(f"Erreur lors de la suppression de l'utilisateur: {e}")

    def UpdateUser(con, data, id):
        query = "UPDATE user SET username = ?, pwd = ?  WHERE id = ?"
        try:
            cur = con.cursor()
            cur.execute("SELECT username FROM user WHERE id = ?", (id,))
            resultSelect = cur.fetchone()

            if resultSelect:
                cur.execute(query, (*data, id))
                con.commit()
                print(f"Utilisateur {data[0]} modifié.")
            else:
                print(f"L'utilisateur {data[0]} n'existe pas")
        except Error as e:
            print(f"Erreur lors de la modification de l'utilisateur: {e}")

    def ShowEvents(con):
        query = ("SELECT title, date_begin, date_end, place, event_type, organisators, description FROM event WHERE ")
        try:
            cur = con.cursor()        
            cur.execute(query)
            rows = cur.fetchall()
            return rows

        except Error as e:
            return []
        
    def ShowEventsByWeek(con):
        day = str(datetime.today().strftime('%Y-%m-%dT%H:%M:%S'))
        dt = datetime.strptime(day, '%Y-%m-%dT%H:%M:%S') #"2024-11-06T08:00:00"

        start = dt - timedelta(days=dt.weekday())
        end = start + timedelta(days=6)

        start_str = start.strftime("%Y-%m-%dT%H:%M:%S")        
        end_str = end.strftime("%Y-%m-%dT%H:%M:%S")

        query = (f"SELECT title, date_begin, date_end, place, event_type, organisators, description FROM event WHERE date_begin >= ? AND date_begin <= ?")
        try:
            cur = con.cursor()        
            cur.execute(query, (start_str, end_str))
            rows = cur.fetchall()
            return rows

        except Error as e:
            return []

    def ShowEventByFilter(con, type):
        clause = "WHERE event_type ="
        for i in range(0, len(type)):
            if(i != len(type) - 1):
                clause += f" '{type[i]}' OR event_type ="
            else:
                clause += f" '{type[i]}'"

        query = (f"SELECT title, date_begin, date_end, place, event_type, organisators, description FROM event {clause} ORDER BY date(date_begin) DESC")
        
        try:
            cur = con.cursor()        
            cur.execute(query)
            rows = cur.fetchall()
            return rows

        except Error as e:
            return []

    def CreateEvent(con, data):
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

    def DeleteEvent(con, id):
        query = "DELETE FROM event WHERE id = ? RETURNING title"
        try:
            cur = con.cursor()
            cur.execute("SELECT title FROM event WHERE id = ?", (id,))
            resultSelect = cur.fetchone()

            if resultSelect: 
                cur.execute(query, (id,))
                result = cur.fetchone()

                if result:
                    con.commit()
                    print(f"Evenement {result[0]} supprimé.")

            else:
                print("L'évenement n'existe pas.")

        except Error as e:
            print(f"Erreur lors de la suppression de l'évenement: {e}")

    def UpdateEvent(con, data, id):
        query = "UPDATE event SET title = ?, date_begin = ? ,date_end = ? ,place = ? ,event_type = ? ,organisators = ? ,description = ?  WHERE id = ?"
        try:
            cur = con.cursor()
            cur.execute("SELECT title FROM event WHERE id = ?", (id,))
            resultSelect = cur.fetchone()

            if resultSelect:
                cur.execute(query, (*data, id))
                con.commit()
                print(f"Evenement {data[0]} modifié.")
            else:
                print(f"Evenement {data[0]} n'existe pas.")
        except Error as e:
            print(f"Erreur lors de la modification de l'évenement: {e}")