import json
import os
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.pipeline import make_pipeline
from joblib import dump, load
from email_processor import preprocess_email
from to_json import save_results_to_json

nlp = spacy.load("fr_dep_news_trf")

def train_and_classify_emails(emails_data, mode, model_file="trained_model.joblib", json_file="results.json"):
    if mode == "IA trainer":
        # Directories for training data
        path_avec_eve = "mailsAvecEvent"
        path_sans_eve = "mailsSansEvent"

        # Ensure directories exist
        if not os.path.exists(path_avec_eve):
            os.makedirs(path_avec_eve)
        if not os.path.exists(path_sans_eve):
            os.makedirs(path_sans_eve)

        # Charger le modèle existant s'il est disponible
        if os.path.exists(model_file):
            pipeline = load(model_file)
            print(f"Modèle chargé à partir de {model_file}")
        else:
            # Separate emails with and without events
            emails_avec_eve = [email['body'] for email in emails_data if "event" in email['subject'].lower()]
            emails_sans_eve = [email['body'] for email in emails_data if "event" not in email['subject'].lower()]

            # Création des étiquettes
            labels_avec_eve = [1] * len(emails_avec_eve)
            labels_sans_eve = [0] * len(emails_sans_eve)

            emails = emails_avec_eve + emails_sans_eve
            labels = labels_avec_eve + labels_sans_eve

            processed_emails = [preprocess_email(email, nlp) for email in emails]

            # Entraînement du modèle
            pipeline = make_pipeline(
                TfidfVectorizer(),
                SVC(kernel='linear', probability=True)
            )

            pipeline.fit(processed_emails, labels)

            # Sauvegarde du modèle entraîné
            dump(pipeline, model_file)
            print(f"Modèle sauvegardé dans {model_file}")

        # Classification des emails
        emails_avec_eve_test = []
        emails_sans_eve_test = []

        for email in emails_data:
            processed_email = preprocess_email(email['body'], nlp)
            prediction_proba = pipeline.predict_proba([processed_email])[0]
            prediction = prediction_proba.argmax()
            probability = prediction_proba[prediction]

            if prediction == 1:  # Si la prédiction est que l'email contient un événement
                print(f"Email trouvé :")
                print(f"Sujet: {email['subject']}")
                print(f"Corps: {email['body']}")
                print(f"Prédiction actuelle: Contient un événement (Probabilité: {probability:.2f})")
                print("Que souhaitez-vous corriger ?")
                print("1. L'IA a mal classifié cet email (ne contient pas d'événement)")
                print("2. Aucune action nécessaire")

                user_choice = input("Votre choix (1/2) : ")
                if user_choice == "1":
                    emails_sans_eve_test.append((email['subject'], probability))
                elif user_choice == "2":
                    emails_avec_eve_test.append((email['subject'], probability))
            else:  # Si la prédiction est que l'email ne contient pas un événement
                print(f"Email trouvé :")
                print(f"Sujet: {email['subject']}")
                print(f"Corps: {email['body']}")
                print(f"Prédiction actuelle: Ne contient pas d'événement (Probabilité: {probability:.2f})")
                print("Que souhaitez-vous corriger ?")
                print("1. L'IA a mal classifié cet email (contient un événement)")
                print("2. Aucune action nécessaire")

                user_choice = input("Votre choix (1/2) : ")
                if user_choice == "1":
                    emails_avec_eve_test.append((email['subject'], probability))
                elif user_choice == "2":
                    emails_sans_eve_test.append((email['subject'], probability))

        # Sauvegarde des résultats dans un fichier JSON
        save_results_to_json(json_file, emails_avec_eve_test, emails_sans_eve_test)

    elif mode == "utilisateur lambda":
        if not os.path.exists(model_file):
            print(f"Le modèle {model_file} n'existe pas. Impossible de classifier les emails.")
            return
        
        pipeline = load(model_file)
        print(f"Modèle chargé à partir de {model_file}")

        emails_avec_eve_test = []
        emails_sans_eve_test = []

        for email in emails_data:
            processed_email = preprocess_email(email['body'], nlp)
            prediction_proba = pipeline.predict_proba([processed_email])[0]
            prediction = prediction_proba.argmax()
            probability = prediction_proba[prediction]

            if prediction == 1:  # Si la prédiction est que l'email contient un événement
                emails_avec_eve_test.append((email['subject'], probability))
            else:  # Si la prédiction est que l'email ne contient pas un événement
                emails_sans_eve_test.append((email['subject'], probability))

        # Sauvegarde des résultats dans un fichier JSON
        save_results_to_json(json_file, emails_avec_eve_test, emails_sans_eve_test)

    else:
        print("Mode invalide. Veuillez choisir entre 'IA trainer' ou 'Utilisateur lambda'.")
