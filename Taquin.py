from bs4 import BeautifulSoup
import requests

URL = "https://cyber-learning.fr/cyber-challenge/programmation/pushpush/index.php?jeton=0NslEBD1CW12"

session = requests.session()
r = session.get(URL)
soup = BeautifulSoup(r.text, "html.parser")

# Extraction des cases
tiles = [div.text.strip() for div in soup.select("#puzzle-container div")]
print(tiles)  # -> ['MNG', 'LUB', 'DNF', 'KTT', ...]
