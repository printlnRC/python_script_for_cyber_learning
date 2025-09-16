import requests

URL = "https://cyber-learning.fr/cyber-challenge/programmation/calcul50/sujet.php?jeton=5CY2Bp7Jf310"

session = requests.session()
reponse = session.get(URL)

codeHTML = reponse.text
print("Page reçue :\n", codeHTML)

# Extraction du texte "Combien font ..."
start = codeHTML.find("Combien font ") + len("Combien font ")
end = codeHTML.find("<br>", start)
expression = codeHTML[start:end].strip()

print("Expression trouvée :", expression)

# Séparation des deux nombres autour du "x"
a_str, b_str = expression.split("x")
a = int(a_str.strip())
b = int(b_str.strip())

# Calcul du produit
calcul = a * b
print("Résultat :", calcul)

# Envoi de la réponse (le champ s'appelle "resultat" dans le formulaire)
data = {"resultat": calcul}
post_reponse = session.post(URL, data=data)

print("Réponse du serveur :\n", post_reponse.text)
