import requests
from copy import deepcopy
import heapq
import re

# ==========================
# 1️⃣ Récupération du puzzle
# ==========================
BASE_URL = "https://cyber-learning.fr/cyber-challenge/programmation/pushpush/"
session = requests.session()

puzzle_response = session.get(BASE_URL + "init_puzzle.php")
puzzle_data = puzzle_response.json()

positions = puzzle_data['positions']  # état initial
labels = puzzle_data['labels']        # texte sur chaque tuile (15 éléments)
signature = puzzle_data['signature']  # signature pour validation

print("Puzzle initial :", positions)
print("Labels :", labels)
print("Signature :", signature)

# ==========================
# 2️⃣ Fonctions utilitaires
# ==========================
goal = list(range(16))  # état final du puzzle

def manhattan(state):
    distance = 0
    for i, val in enumerate(state):
        if val == 15:  # tuile vide
            continue
        x1, y1 = i % 4, i // 4
        x2, y2 = val % 4, val // 4
        distance += abs(x1 - x2) + abs(y1 - y2)
    return distance

def neighbors(state):
    i = state.index(15)
    x, y = i % 4, i // 4
    moves = []
    for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        nx, ny = x+dx, y+dy
        if 0 <= nx < 4 and 0 <= ny < 4:
            nstate = state.copy()
            ni = ny*4 + nx
            nstate[i], nstate[ni] = nstate[ni], nstate[i]
            moves.append(nstate)
    return moves

# ==========================
# 3️⃣ Résolution du puzzle
# ==========================
def solve_puzzle(start):
    heap = [(manhattan(start), 0, start)]
    visited = set()
    visited.add(tuple(start))

    while heap:
        f, g, state = heapq.heappop(heap)
        if state == goal:
            return state
        for n in neighbors(state):
            t = tuple(n)
            if t not in visited:
                visited.add(t)
                heapq.heappush(heap, (g+1+manhattan(n), g+1, n))

solution = solve_puzzle(positions)
print("Puzzle résolu :", solution)

# ==========================
# 4️⃣ Labels dans l'ordre final
# ==========================
solved_labels = [labels[i] if i != 15 else " " for i in solution]
print("Labels dans le bon ordre :", solved_labels)

# ==========================
# 5️⃣ Soumission au serveur
# ==========================
submit_url = BASE_URL + "submit_puzzle.php"  # adapter selon le site

# Préparer le payload. Selon le site, il peut attendre 'solution' ou 'labels'
payload = {
    "solution": solution,      # ou "labels": solved_labels
    "signature": signature
}

response = session.post(submit_url, json=payload)
print("Réponse brute du serveur :", response.text)

# ==========================
# 6️⃣ Recherche automatique du flag
# ==========================
match = re.search(r'FLAG\{.*?\}', response.text)
if match:
    print("Flag trouvé :", match.group(0))
else:
    print("Flag non trouvé dans la réponse")
