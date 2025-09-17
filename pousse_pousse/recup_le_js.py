import requests

URL_JS = "https://cyber-learning.fr/cyber-challenge/programmation/pushpush/script.js"
reponse_js = requests.get(URL_JS)
js_code = reponse_js.text

# On peut sauvegarder pour l'analyser
with open("script.js", "w", encoding="utf-8") as f:
    f.write(js_code)

print(js_code[:500])  # Affiche les 500 premiers caractères



