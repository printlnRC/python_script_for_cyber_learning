import itertools
import string

letters = string.ascii_uppercase  # alphabet majuscule A-Z
counter = 0

with open("passwords.txt", "w") as f:
    for combo in itertools.product(letters, repeat=6):
        f.write("".join(combo) + "\n")
        counter += 1

        # Affiche un message tous les 1 million de lignes pour suivre la progression
        if counter % 1_000_000 == 0:
            print(f"{counter} mots de passe générés...")

print(f"Terminé ! Total = {counter} mots de passe écrits.")
