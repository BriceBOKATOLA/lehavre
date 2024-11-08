import json
import sqlite3
import pandas as pd
 
"""
Classe DataExtractor pour extraire les donnees
"""
class DataExtractor () :
 
    """
    Constructeur de la classe DataExtractor
    """    
    def __init__(self, 
                 file_path_json, db_path) :
        self.file_path_json = file_path_json
        self.db_path = db_path
        self.data = self.load_json ()
       
    """
    Methode load_json pour charger les donnees du fichier JSON
    """
    def load_json (self) :
        print ("\n -------------------------------------------------------------------------")
        print (f"\n Loading data from JSON file : {self.file_path_json} ...")
        try : 
            with open (self.file_path_json, 'r') as file :
                data = json.load (file)
            print (f"\n Data loaded from JSON file")
            return data
        except FileNotFoundError :
            print (f"\n Error: The file {self.file_path_json} was not found")
            return None
        except json.JSONDecodeError as exception :
            print(f"\n Error failed to decode JSON file : \n {str (exception)}")
            return None
        except Exception as exception :
            print(f"\n Error an unexpected error occurred {str (exception)}")
            return None
        
    def get_data(self):
        if self.data is None:
            print("No data loaded to insert into the database.")
            return
        
        try:
            # Connexion à la base de données SQLite
            with sqlite3.connect(self.db_path) as conn:
                for table_name, records in self.data.items():
                    # Vérifiez que les données pour la table actuelle sont une liste d'objets
                    if isinstance(records, list):
                        try:
                            # Convertir en DataFrame
                            df = pd.DataFrame(records)
                            # Insérer les données dans la table
                            df.to_sql(table_name, conn, if_exists='replace', index=False)
                            print(f"\n Data successfully inserted into table '{table_name}'")
                        except ValueError as e:
                            print(f"\n Error: Unable to convert data for table '{table_name}' to DataFrame: {e}")
                    else:
                        print(f"\n Warning: Data for '{table_name}' is not a list and was skipped.")
        except sqlite3.Error as e:
            print(f"\n Error while inserting data into database: {e}")
        except Exception as e:
            print(f"\n An unexpected error occurred: {e}")