import requests # bibliothèque spécialisée pour les échanges http/https

URL = "https://cyber-learning.fr/cyber-challenge/programmation/calcul50/sujet.php?jeton=5CY2Bp7Jf310"

# 1. On se connecte au serveur
session = requests.session() # Il est capital de garder la session pour renvoyer la réponse
reponse = session.get(URL)
# 2. On récupère le texte du code HTML
codeHTML = reponse.text   
print(codeHTML)