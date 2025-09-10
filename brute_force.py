from PyPDF2 import PdfReader
import itertools
import string
import time

def essayer_mot_de_passe(pdf_path, mot_de_passe):
    try:
        with open(pdf_path, "rb") as f:
            reader = PdfReader(f)
            return reader.decrypt(mot_de_passe) == 1
    except Exception:
        return False

def brute_force_pdf(pdf_path):
    lettres = string.ascii_uppercase
    combinaisons = itertools.product(lettres, repeat=6)

    compteur = 0
    debut = time.time()
    dernier_affichage = debut

    for c in combinaisons:
        mot_de_passe = ''.join(c)
        compteur += 1

        if essayer_mot_de_passe(pdf_path, mot_de_passe):
            print(f"[✅] Mot de passe trouvé : {mot_de_passe} après {compteur} tentatives")
            break

        maintenant = time.time()
        if maintenant - dernier_affichage >= 1:
            print(f"{compteur} mots de passe testés...")
            dernier_affichage = maintenant
    else:
        print("❌ Mot de passe non trouvé.")

# Remplace par le chemin complet vers ton fichier PDF
pdf_path = "/home/s/sam.coulet/Documents/test_protege.pdf"
brute_force_pdf(pdf_path)
