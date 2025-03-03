import imaplib
import email
from email.header import decode_header

def fetch_emails(imap_server, email_address, password, limit=10):
    try:
        mail = imaplib.IMAP4_SSL(imap_server)
        mail.login(email_address, password)
        mail.select("inbox")
        
        status, messages = mail.search(None, "ALL")
        email_ids = messages[0].split()[-limit:]

        emails = []
        for email_id in email_ids:
            res, msg = mail.fetch(email_id, "(RFC822)")
            for response in msg:
                if isinstance(response, tuple):
                    msg = email.message_from_bytes(response[1])
                    subject, encoding = decode_header(msg["Subject"])[0]
                    if isinstance(subject, bytes):
                        subject = subject.decode(encoding if encoding else "utf-8")
                    body = None
                    if msg.is_multipart():
                        for part in msg.walk():
                            content_type = part.get_content_type()
                            if content_type == "text/plain":
                                body = part.get_payload(decode=True).decode()
                                break
                    else:
                        body = msg.get_payload(decode=True).decode()
                    body = body.replace('"', '')
                    subject = subject.replace('"', '')
                    emails.append({"subject": subject, "body": body})
        mail.logout()
        return emails
    except Exception as e:
        print(f"Erreur lors de la lecture des e-mails : {e}")
        return []
