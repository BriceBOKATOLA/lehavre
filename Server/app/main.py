from database import DataBase
from dataExtractor import DataExtractor
import sys
import os

# Ajouter le chemin vers le dossier racine du projet
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from Client.src.db.init_db import InitDb  # Import de la classe InitDb

class Main:
    def __init__(self):
        self.file_path_json = '..\\Data\\data.json'
        self.db_path = '..\\..\\Client\\src\\db\\LHSM_events.db'
        #self.db_initializer = InitDb
        self.con = DataBase.sql_connection(self.db_path)  # Connexion à la base de données
        self.data_extractor = DataExtractor(self.file_path_json, self.db_path)

    def run(self):
        #self.db_initializer.init_db()
        InitDb.init_db()
        # Connexion à la base de données
        # Charger les données JSON
        data = self.data_extractor.load_json()
        # Exécuter les méthodes CRUD sur les utilisateurs

        for user in data['user']:
            # Créer un utilisateur
            DataBase.CreateUser(self.con, (user['username'], user['pwd']))

        #DataBase.ModifyUser(self.con, ("janedoe2", "securepass4562"), 3)
        
        DataBase.DeleteUser(self.con, 4)
        # Exécuter les méthodes CRUD sur les événements
        for event in data['events']:
            # Créer un événement
            DataBase.CreateEvenement(self.con, (
                event['title'], 
                event['date_begin'], 
                event['date_end'], 
                event['place'], 
                event['event_type'], 
                event['organisators'], 
                event['description']
            ))

        # Fermer la connexion
        DataBase.sql_close(self.con)


if __name__ == "__main__":
    main = Main()
    main.run()