import openai

def extract_event_details(email_subject, email_body, api_key, model):
    openai.api_key = api_key
    
    # Définir le prompt avec les instructions claires
    prompt = (
        f"Voici un e-mail avec les informations suivantes :\n"
        f"- Objet : {email_subject}\n"
        f"- Contenu : {email_body}\n\n"
        "Filtre : Analysez le contenu et ne retenez que les événements liés a l emploi ou à la formation "
        "qui concernent Le Havre et ses alentours. Si aucun événement ne correspond à ces critères, "
        "répondez exactement avec : {}\n\n"
        "Retournez un JSON structuré avec des doubles quotes comme suit, uniquement si un événement correspondant est trouvé :\n"
        "{\n"
        '  "title": "<titre de l événement>",\n'
        '  "place": "<lieu de l évenement>",\n'
        '  "event_type": "<type (conférence, salon, emploi, etc.)>",\n'
        '  "date_begin": "<date début (format YYYY-MM-DD)>",\n'
        '  "date_end": "<date fin (format YYYY-MM-DD)>",\n'
        '  "description": "<description (maximum 2 phrases)>"\n'
        '  "organisators": "<le ou les organisateurs de l événement"\n'
        "}"
    )
    
    try:
        # Appel à l'API OpenAI
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": "Vous êtes un assistant intelligent et précis. Répondez uniquement avec des JSON valides."},
                {"role": "user", "content": prompt}
            ],
            response_format = {"type": "json_object"}
        )

        # Extraire le contenu textuel de la réponse
        structured_output = response["choices"][0]["message"]["content"]
        
        # Vérifier et éventuellement corriger les apostrophes
        #structured_output = structured_output.replace("'", '"')
        
        return structured_output
    
    except openai.error.OpenAIError as e:
        print(f"Erreur lors de l'appel à l'API : {e}")
        return None
