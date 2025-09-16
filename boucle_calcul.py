import requests

URL = "https://cyber-learning.fr/cyber-challenge/programmation/calcul50/sujet.php?jeton=5CY2Bp7Jf310"

session = requests.session()
reponse = session.get(URL)
codeHTML = reponse.text

while True:
    if "Combien font" not in codeHTML:
        # Pas de nouveau calcul → fin du défi
        print("=== Message final du serveur ===")
        print(codeHTML)
        break

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

    # Envoi de la réponse
    data = {"resultat": calcul}
    post_reponse = session.post(URL, data=data)
    codeHTML = post_reponse.text

    # Retour intermédiaire
    if "Pas mal... continuons" in codeHTML:
        print("Bonne réponse, on continue !\n")
