import configparser
import json
from fetch_emails import fetch_emails
from extract_ia import extract_event_details
import os

# Charger la configuration
config = configparser.ConfigParser()
config.read("config.ini")

# Paramètres
IMAP_SERVER = "imap.gmail.com"
EMAIL = config["email"]["address"]
PASSWORD = config["email"]["password"]
API_URL = "https://api.openai.com/v1/chat/completions"
API_KEY = config["openai"]["api_key"]
MODEL = config["openai"]["model"]
# Récupérer le dossier où enregistrer les fichiers JSON
save_dir = config.get("Settings", "save_directory", fallback="output")

if __name__ == "__main__":

    # Récupérer les emails
    emails = fetch_emails(IMAP_SERVER, EMAIL, PASSWORD)

    event_details_list = []

    for email in emails:
        raw_details = extract_event_details(email["body"], API_URL, API_KEY, MODEL)

        if raw_details and raw_details != "{}":
            event_details_list.append(json.loads(raw_details))

    # Préparer les données à enregistrer
    events_collection = {"events": event_details_list}

    # Construire le chemin du fichier
    file_path = os.path.join(save_dir, "data.json")

    # Enregistrer les données dans le fichier JSON
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(events_collection, file, indent=4, ensure_ascii=False)

    print(f"Event details have been saved to '{file_path}' under the 'events' collection.")