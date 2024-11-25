import os
import imaplib
import email
from email.header import decode_header
import chardet
from bs4 import BeautifulSoup

def clean(text):
    # Nettoyer le texte pour éviter les problèmes de système de fichiers
    return "".join(c if c.isalnum() else "_" for c in text)

def decode_bytes(byte_content):
    encoding = chardet.detect(byte_content)['encoding']
    if encoding:
        return byte_content.decode(encoding)
    return byte_content.decode('utf-8', errors='ignore')

def get_emails(username, password, server="imap.gmail.com"):
    # Connexion au serveur IMAP
    mail = imaplib.IMAP4_SSL(server)
    mail.login(username, password)
    mail.select("inbox")
    
    status, messages = mail.search(None, "ALL")
    email_ids = messages[0].split()
    
    emails = []
    
    for email_id in email_ids:
        status, msg_data = mail.fetch(email_id, "(RFC822)")
        msg = email.message_from_bytes(msg_data[0][1])
        
        subject, encoding = decode_header(msg["Subject"])[0]
        if isinstance(subject, bytes):
            subject = subject.decode(encoding if encoding else "utf-8")
        
        # Depuis
        from_ = msg.get("From")
        
        # Texte du mail
        email_content = {"subject": subject, "from": from_, "body": "", "attachments": []}
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    body = part.get_payload(decode=True)
                    body = decode_bytes(body)
                    email_content["body"] = body
                elif part.get_content_type() == "text/html":
                    body = part.get_payload(decode=True)
                    body = decode_bytes(body)
                    soup = BeautifulSoup(body, "html.parser")
                    email_content["body"] = soup.get_text()
                elif part.get_content_type().startswith("image/"):
                    attachment = part.get_payload(decode=True)
                    attachment_name = part.get_filename()
                    email_content.setdefault("images", []).append((attachment_name, attachment))
        else:
            if msg.get_content_type() == "text/plain":
                body = msg.get_payload(decode=True)
                body = decode_bytes(body)
                email_content["body"] = body
            elif msg.get_content_type() == "text/html":
                body = msg.get_payload(decode=True)
                body = decode_bytes(body)
                soup = BeautifulSoup(body, "html.parser")
                email_content["body"] = soup.get_text()
        
        emails.append(email_content)
    
    return emails

def save_emails_to_files(emails, directory_path):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
    
    for email in emails:
        subject_cleaned = clean(email['subject'])
        email_dir = os.path.join(directory_path, subject_cleaned)
        if not os.path.exists(email_dir):
            os.makedirs(email_dir)
        
        email_filepath = os.path.join(email_dir, "email.txt")
        with open(email_filepath, "w", encoding="utf-8") as file:
            file.write(email['body'])

if __name__ == "__main__":
    # Configuration des informations d'email
    EMAIL = "emploiformationlamanu@gmail.com"
    PASSWORD = "uombnbnrcvkbwohx"
    IMAP_SERVER = "imap.gmail.com"
    
    # Définir le chemin du bureau
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "emails_extraits")
    
    emails = get_emails(EMAIL, PASSWORD, IMAP_SERVER)
    
    # Enregistrer les emails dans des fichiers
    save_emails_to_files(emails, desktop_path)
    
    print(f"Tous les emails ont été enregistrés dans le répertoire: {desktop_path}")