from PIL import Image
import pytesseract
import os

def ocr_core(filename):
    """
    Cette fonction va traiter l'image et renvoyer le texte
    """
    text = pytesseract.image_to_string(Image.open(filename))
    return text

def get_text_from_images(directory_path, output_path):
    """
    Cette fonction va lire les images dans un répertoire et écrire le texte extrait dans un fichier
    """
    if not os.path.exists(directory_path):
        print(f"Le répertoire {directory_path} n'existe pas.")
        return

    with open(output_path, "w", encoding="utf-8") as output_file:
        for image_file in os.listdir(directory_path):
            if image_file.lower().endswith(('png', 'jpg', 'jpeg', 'tiff', 'bmp', 'gif')):
                image_path = os.path.join(directory_path, image_file)
                text = ocr_core(image_path)
                output_file.write(f"Texte extrait de l'image {image_file}:\n{text}\n\n")

if __name__ == "__main__":
    directory_path = "chemin_vers_votre_dossier_d_images"
    output_path = "chemin_vers_le_fichier_de_sortie.txt"
    get_text_from_images(directory_path, output_path)