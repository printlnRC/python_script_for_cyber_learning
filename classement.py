import requests
import re

URL = "https://cyber-learning.fr/cyber-challenge/programmation/parcoursup/index.php?jeton=jhBd1NBHRy12"

# 1. Connexion au serveur
session = requests.Session()
response = session.get(URL)
codeHTML = response.text

# 2. Extraction des prénoms
prenoms = re.findall(r'<span class="prenom">(.*?)</span>', codeHTML)
print("Prénoms :", prenoms)

# 3. Extraction des notes pour chaque élève
notes_raw = re.findall(r'<div class="notes">(.*?)</div>', codeHTML, re.DOTALL)
liste_notes = []
for notes_div in notes_raw:
    notes = [int(n) for n in re.findall(r'<span class="note">(\d+)</span>', notes_div)]
    liste_notes.append(notes)
print("Notes :", liste_notes)

# 4. Extraction des coefficients
coeffs = [int(c) for c in re.findall(r'<span class="coef">(\d+)</span>', codeHTML)]
print("Coefficients :", coeffs)

# 5. Calcul des moyennes pondérées
moyennes = []
for notes in liste_notes:
    moyenne = sum(n*c for n, c in zip(notes, coeffs)) / sum(coeffs)
    moyennes.append(moyenne)

# 6. Classement des élèves par moyenne décroissante
eleves_classes = [x for _, x in sorted(zip(moyennes, prenoms), reverse=True)]
initiales = "".join([prenom[0] for prenom in eleves_classes])
print("Classement final (initiales) :", initiales)

# 7. Envoi de la réponse au serveur
data = {"resultat": initiales}
post_response = session.post(URL, data=data)
print("Réponse du serveur :")
print(post_response.text)
