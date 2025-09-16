import requests
import re

URL = "https://cyber-learning.fr/cyber-challenge/programmation/calcul50/sujet.php?jeton=5CY2Bp7Jf310"

session = requests.Session()
response = session.get(URL)
codeHTML = response.text

while True:
    # Cherche un calcul du type "nombre x nombre" dans la page
    match = re.search(r'(\d+)\s*x\s*(\d+)', codeHTML)
    
    if match:
        a = int(match.group(1))
        b = int(match.group(2))
        calcul = a * b

        print(f"Expression trouvée : {a} x {b}")
        print(f"Résultat : {calcul}")

        # Envoi de la réponse au serveur
        data = {"resultat": str(calcul)}
        post_response = session.post(URL, data=data)
        codeHTML = post_response.text

        # Vérification du retour
        if "Pas mal... continuons" in codeHTML:
            print("Bonne réponse, on continue !\n")

    else:
        # Aucun calcul trouvé → fin du défi
        print("=== Message final du serveur ===")
        print(codeHTML)
        break
