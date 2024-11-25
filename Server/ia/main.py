import json
import time
from imap_email_fetcher import connect_to_mail, fetch_unseen_emails, process_emails
from email_classifier import train_and_classify_emails

def main():
    print("Bonjour, êtes-vous Trainer ou souhaitez-vous juste classifier les emails ?")
    print("Tapez '1' pour le mode 'Utilisateur lambda' ou '2' pour le mode 'IA trainer'.")

    user_choice = input("Votre choix (1/2) : ")
    
    if user_choice == "1":
        mode = "utilisateur lambda"
        print("Mode 'Utilisateur lambda' sélectionné.")
    elif user_choice == "2":
        mode = "IA trainer"
        print("Mode 'IA trainer' sélectionné.")
    else:
        print("Choix invalide. Le programme va utiliser le mode 'Classification' par défaut.")
        mode = "utilisateur lambda"

    while True:
        # Connexion au serveur de messagerie
        mail = connect_to_mail()
        if not mail:
            print("Erreur: Impossible de se connecter au serveur de messagerie.")
        else:
            try:
                # Récupération des nouveaux emails non lus
                email_ids = fetch_unseen_emails(mail)
                print(f"Email IDs récupérés : {email_ids}")

                # Traitement des emails récupérés et récupération des informations des emails
                if email_ids:
                    emails_data = process_emails(mail, email_ids)
                    print(f"Emails récupérés : {email_ids}")

                    if not emails_data:
                        print("Aucun email n'a été traité ou les données sont vides.")
                    else:
                        # Appel de la fonction d'entraînement et de classification
                        path_avec_eve = "mailsAvecEvent"
                        path_sans_eve = "mailsSansEvent"
                        train_and_classify_emails(emails_data, mode=mode)

            finally:
                # Fermeture de la connexion et déconnexion du serveur
                mail.close()
                mail.logout()

        # Demander à l'utilisateur s'il souhaite quitter le programme
        user_exit = input("Souhaitez-vous quitter le programme ? (oui/non) : ").strip().lower()

        if user_exit == "oui":
            print("Le programme va se fermer.")
            break
        else:
            print("Le programme va continuer dans 30 minutes.")
            # Attendre 30 minutes avant la prochaine exécution
            time.sleep(1800)

if __name__ == "__main__":
    main()
