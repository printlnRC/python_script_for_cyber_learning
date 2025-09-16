import requests # bibliothèque spécialisée pour les échanges http/https

URL = "https://cyber-learning.fr/cyber-challenge/programmation/socket/sujet.php?jeton=EB0SRa0w5311"

# 1. On se connecte au serveur
session = requests.session() # Il est capital de garder la session pour renvoyer la réponse
reponse = session.get(URL)
# 2. On récupère le texte du code HTML
codeHTML = reponse.text   
print(codeHTML)
# 3. On calcul de la position du code...
positionCode = codeHTML.find("FLAG) : ") + 8
# ... et on récupére la chaine pour le challenge
code = codeHTML[positionCode:positionCode+20]    
print(code)
# 4. Envoyer le résultat au serveur via une requête POST
data = {"copie": code} # mise en forme json du résultat
print(data)
# envoi du resultat avec la même session
post_reponse = session.post(URL, data=data)
# réponse du serveur
print(post_reponse.text)