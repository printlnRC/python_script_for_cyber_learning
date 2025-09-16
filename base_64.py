import requests
import base64

URL = "https://cyber-learning.fr/cyber-challenge/programmation/b64/sujet.php?jeton=51XMXTrmtc18"

# 1. Connexion au serveur
session = requests.session()
reponse = session.get(URL)

# 2. Récupération du code HTML
codeHTML = reponse.text
print("Page reçue :\n", codeHTML)

# 3. Extraction de la chaîne base64 (jusqu’au <br>)
positionCode = codeHTML.find("Décodez : ") + len("Décodez : ")
finCode = codeHTML.find("<br>", positionCode)
code_b64 = codeHTML[positionCode:finCode].strip()
print("Code encodé (base64) :", code_b64)

# 4. Décodage base64
decoded = base64.b64decode(code_b64).decode("utf-8")
print("Décodé brut :", decoded)

# 5. Récupération uniquement de la valeur après "FLAG = "
if "FLAG" in decoded:
    code_final = decoded.split("=")[1].strip()
else:
    code_final = decoded.strip()

print("Code final à renvoyer :", code_final)

# 6. Envoi de la réponse
data = {"resultat": code_final}   # ⚠️ ici le champ du formulaire s'appelle "resultat"
post_reponse = session.post(URL, data=data)

# 7. Réponse du serveur
print("Réponse du serveur :\n", post_reponse.text)
