import json
import os

def save_results_to_json(file_path, emails_avec_eve, emails_sans_eve):
    """
    Sauvegarde les résultats dans un fichier JSON. Si le fichier n'existe pas, il est créé.
    
    :param file_path: Chemin du fichier JSON où les résultats seront sauvegardés.
    :param emails_avec_eve: Liste des emails contenant des événements.
    :param emails_sans_eve: Liste des emails ne contenant pas d'événements.
    """
    print(f"Vérification du chemin du fichier : {file_path}")
    print(f"Emails avec événements : {emails_avec_eve[:5]}")  # Affiche les 5 premiers emails pour vérification
    print(f"Emails sans événements : {emails_sans_eve[:5]}")  # Affiche les 5 premiers emails pour vérification

    # Vérifier si le fichier JSON existe
    if not os.path.exists(file_path):
        # Initialiser la structure du fichier JSON
        initial_data = {
            "emails_avec_eve": [],
            "emails_sans_eve": []
        }
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(initial_data, f, ensure_ascii=False, indent=4)
        print(f"Fichier JSON créé à {file_path}")

    # Charger les données existantes
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Ajouter les nouveaux résultats
    data["emails_avec_eve"].extend(emails_avec_eve)
    data["emails_sans_eve"].extend(emails_sans_eve)
    
    # Sauvegarder les résultats mis à jour dans le fichier JSON
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print(f"Résultats sauvegardés dans {file_path}")
