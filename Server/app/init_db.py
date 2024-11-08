import sqlite3

# Connexion à la base de données SQLite (ou création si elle n'existe pas encore)
class InitDb:
    @staticmethod
    def table_exists(con, table_name):
        cursor = con.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
        return cursor.fetchone() is None

    @staticmethod
    def init_db():
        conn = sqlite3.connect("../DataBase/LHSM_events.db")
        cursor = conn.cursor()
        
        # Création de la table `user`
        if InitDb.table_exists(conn, "user"):
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS user (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username VARCHAR(50) UNIQUE NOT NULL,
                pwd TEXT NOT NULL -- Hachage du mot de passe stocké en tant que texte
            )
            ''')
            print("Table 'user' créée.")
        else:
            print("Table 'user' existe déjà.")

        # Création de la table `event`
        if InitDb.table_exists(conn, "events"):
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS events (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title VARCHAR(100) NOT NULL,
                date_begin DATETIME NOT NULL,
                date_end DATETIME NOT NULL,
                place VARCHAR(100) NOT NULL,
                event_type VARCHAR(50) NOT NULL,
                organisators TEXT NOT NULL,
                description TEXT,
                UNIQUE(title, date_begin, place)
            )
            ''')
            print("Table 'events' créée.")
        else:
            print("Table 'events' existe déjà.")

        # Liste des événements à insérer
        events = [
            ("Concert de Jazz", "2024-11-10 19:00", "2024-11-10 21:00", "Théâtre des Arts", "Concert", "Association Jazz Le Havre", "Un concert avec des musiciens de jazz renommés."),
            ("Exposition d'Art Contemporain", "2024-11-15 10:00", "2024-12-30 18:00", "MuMa - Musée Malraux", "Exposition", "Ville du Havre", "Une exposition mettant en avant des artistes contemporains locaux et internationaux."),
            ("Marché de Noël", "2024-12-01 10:00", "2024-12-24 20:00", "Place de l'Hôtel de Ville", "Marché", "Association des Commerçants du Havre", "Un marché festif avec des produits artisanaux, des décorations et des spécialités culinaires."),
            ("Festival du Cinéma", "2024-11-20 18:00", "2024-11-25 22:00", "Cinéma Le Grand Large", "Festival", "Cinéma Le Grand Large", "Une semaine dédiée à la projection de films indépendants et de documentaires."),
            ("Atelier de Peinture", "2024-11-05 14:00", "2024-11-05 17:00", "Maison de la Culture", "Atelier", "Atelier d'Art Le Havre", "Un atelier pour apprendre les techniques de peinture avec un artiste local."),
        ]

        # Insertion des événements
        cursor.executemany('''
        INSERT OR IGNORE INTO events (title, date_begin, date_end, place, event_type, organisators, description)
        VALUES (?, ?, ?, ?, ?, ?, ?) 
        ''', events)

        # Insertion d'un utilisateur
        cursor.execute('''
        INSERT OR IGNORE INTO user (username, pwd)
        VALUES (?, ?)
        ''', ("admin", "admin_password"))

        # Sauvegarde et fermeture de la connexion
        conn.commit()
        conn.close()
        print("Base de données initialisée avec succès, événements et utilisateur insérés.")

    # Exécution de l'initialisation
    if __name__ == "__main__":
        init_db()
