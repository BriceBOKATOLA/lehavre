import os
import html
import imaplib
import email
from email.header import decode_header
import logging
from bs4 import BeautifulSoup
import re
import codecs  # Module pour gérer les encodages

# Configuration de la journalisation
logging.basicConfig(filename='email_processor.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def connect_to_mail():
    try:
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        username = os.getenv("EMAIL_USERNAME")
        password = os.getenv("EMAIL_PASSWORD")
        mail.login(username, password)
        print("Connexion ok")
        return mail
    except imaplib.IMAP4.error as e:
        logging.error(f"Erreur lors de la connexion au serveur de messagerie: {e}")
        return None

def fetch_unseen_emails(mail):
    try:
        mail.select("inbox")
        status, messages = mail.search(None, 'ALL')
        if status != 'OK':
            logging.error("Erreur lors de la recherche des emails non lus.")
            return []
        return messages[0].split()
    except Exception as e:
        logging.error(f"Erreur lors de la récupération des emails non lus: {e}")
        return []

def normalize_whitespace(text):
    # Décoder les entités HTML
    text = html.unescape(text)
    
    # Remplacer les multiples espaces blancs (espaces, tabulations, nouvelles lignes) par un seul espace
    normalized_text = re.sub(r'\s+', ' ', text).strip()
    # Ajouter un saut de ligne à la fin de chaque paragraphe
    normalized_text = re.sub(r'(\.\s)', r'\1\n', normalized_text)
    return normalized_text

def process_emails(mail, email_ids):
    """
    Traite les emails en fonction des ID fournis et extrait les informations importantes.
    
    :param mail: Instance de connexion au serveur de messagerie.
    :param email_ids: Liste des IDs des emails à traiter.
    :return: Liste des emails traités avec leurs informations.
    """
    emails_data = []

    for index, email_id in enumerate(email_ids, start=1):
        try:
            status, msg_data = mail.fetch(email_id, '(RFC822)')
            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])
                    
                    # Décoder le sujet de l'e-mail
                    subject = ""
                    for part, encoding in decode_header(msg["Subject"]):
                        if isinstance(part, bytes):
                            subject += part.decode(encoding if encoding else "utf-8")
                        else:
                            subject += part
                            
                    # Remplacer les caractères non valides pour le nom de fichier
                    subject_sanitized = "".join([c if c.isalnum() else "_" for c in subject])
                    
                    # Récupérer l'expéditeur de l'e-mail
                    from_ = msg.get("From")
                    
                    # Initialiser le corps de l'e-mail
                    body = ""
                    
                    # Vérifier si l'e-mail est multipart
                    if msg.is_multipart():
                        for part in msg.walk():
                            content_type = part.get_content_type()
                            content_disposition = str(part.get("Content-Disposition"))
                            if content_type == "text/plain" and "attachment" not in content_disposition:
                                try:
                                    body += part.get_payload(decode=True).decode()
                                except Exception as e:
                                    logging.error(f"Erreur lors de la lecture du corps de l'email (texte brut): {e}")
                            elif content_type == "text/html" and "attachment" not in content_disposition:
                                try:
                                    html = part.get_payload(decode=True).decode()
                                    soup = BeautifulSoup(html, "html.parser")
                                    
                                    # Retirer les liens et les images
                                    for element in soup(["a", "img"]):
                                        element.decompose()
                                        
                                    body += soup.get_text()
                                except Exception as e:
                                    logging.error(f"Erreur lors de la lecture du corps de l'email (HTML): {e}")
                    else:
                        if msg.get_content_type() == "text/plain":
                            body = msg.get_payload(decode=True).decode()
                        elif msg.get_content_type() == "text/html":
                            html = msg.get_payload(decode=True).decode()
                            soup = BeautifulSoup(html, "html.parser")
                            
                            # Retirer les liens et les images
                            for element in soup(["a", "img"]):
                                element.decompose()
                                
                            body = soup.get_text()

                    # Normaliser les espaces blancs dans le corps de l'e-mail
                    body = normalize_whitespace(body)
                    
                    # Ajouter les informations de l'email à la liste
                    email_info = {
                        "index": index,
                        "subject": subject,
                        "from": from_,
                        "body": body
                    }
                    emails_data.append(email_info)

        except Exception as e:
            logging.error(f"Erreur lors du traitement de l'email ID {email_id}: {e}")

    return emails_data