import requests
import json
import re

URL = "https://cyber-learning.fr/cyber-challenge/programmation/blockchain/index.php?jeton=t1gJ7fBPbP11"

# Connexion au serveur
session = requests.session()
reponse = session.get(URL)
codeHTML = reponse.text

# Extraction du JSON de la blockchain avec regex
json_match = re.search(r'\[.*\]', codeHTML, re.DOTALL)
if json_match:
    blockchain_json = json_match.group()
    
    # Conversion en liste Python
    blockchain = json.loads(blockchain_json)
    
    # Récupération du dernier bloc
    dernier_bloc = blockchain[-1]
    print("Dernière transaction :", dernier_bloc['data'])
else:
    print("Impossible de trouver la blockchain dans le HTML")
