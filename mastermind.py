import requests
import json
import re

URL = "https://cyber-learning.fr/cyber-challenge/programmation/blockchain/index.php?jeton=t1gJ7fBPbP11"

session = requests.session()
reponse = session.get(URL)
codeHTML = reponse.text

# Extraction du JSON
json_match = re.search(r'\[.*\]', codeHTML, re.DOTALL)
if json_match:
    blockchain_json = json_match.group()
    blockchain = json.loads(blockchain_json)
    
    # Dernier bloc
    dernier_bloc = blockchain[-1]
    
    # On prend exactement le contenu du champ 'data'
    derniere_transaction = dernier_bloc['data']
    
    # Envoi immédiat au serveur
    data = {"copie": derniere_transaction}
    reponse_finale = session.post(URL, data=data)
    
    # Affichage brut de la réponse
    print(reponse_finale.text)
