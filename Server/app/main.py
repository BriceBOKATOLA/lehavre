from database import DataBase
from dataExtractor import DataExtractor


class Main:
    def __init__(self):
        self.file_path_json = '.\\Server\\Data\\data.json'
        self.db_path = '..\\Client\\src\\db\\init_db.py'
        self.con = None  # Connexion à la base de données
        self.data_extractor = DataExtractor(self.file_path_json, self.db_path)

    def run(self):
        # Connexion à la base de données
        DataBase.sql_connection(self)
        #print(self.data_extractor.load_json())
        # Charger les données JSON
        data = self.data_extractor.load_json()
        # Exécuter les méthodes CRUD sur les utilisateurs

        for user in data['user']:
            # Créer un utilisateur
            DataBase.CreateUser(self.con, (user['username'], user['pwd']))

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
        self.sql_close()


if __name__ == "__main__":
    main = Main()
    main.run()