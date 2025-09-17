import requests

# URL de base
BASE_URL = "https://cyber-learning.fr/cyber-challenge/programmation/pushpush/"
session = requests.session()

# On récupère le puzzle initial
puzzle_response = session.get(BASE_URL + "init_puzzle.php")
puzzle_data = puzzle_response.json()  # JSON du puzzle

print(puzzle_data)

