import os

def load_emails_from_folder(folder_path):
    emails = []
    filenames = []
    if not os.path.exists(folder_path):
        print(f"Le dossier {folder_path} n'existe pas.")
        return emails, filenames

    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            try:
                with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as file:
                    emails.append(file.read())
                    filenames.append(filename)
            except Exception as e:
                print(f"Erreur lors de la lecture de {filename}: {e}")
    return emails, filenames

def preprocess_email(email, nlp):
    doc = nlp(email)
    return " ".join([token.lemma_ for token in doc if not token.is_stop and not token.is_punct])
