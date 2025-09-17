import requests
import re
import base64
from PIL import Image
import pytesseract
from io import BytesIO

URL = "https://cyber-learning.fr/cyber-challenge/programmation/captcha/sujet.php?jeton=E3XIzQVjEM15"

# 1. Connexion au serveur
session = requests.Session()
response = session.get(URL)
codeHTML = response.text

# 2. Extraction de l'image CAPTCHA en base64
match = re.search(r'<img src="data:image/png;base64,(.*?)"', codeHTML, re.DOTALL)
if not match:
    print("Pas de CAPTCHA trouvé dans le HTML")
    exit()

img_base64 = match.group(1)
img_data = base64.b64decode(img_base64)

# 3. Conversion en image
image = Image.open(BytesIO(img_data))
image.save("captcha.png")  # optionnel : pour vérifier le captcha manuellement

# 4. Lecture du texte du CAPTCHA avec pytesseract
captcha_text = pytesseract.image_to_string(image, config='--psm 7').strip()
print("Texte du CAPTCHA :", captcha_text)

# 5. Envoi de la réponse au serveur
data = {"captcha": captcha_text}
post_response = session.post(URL, data=data)
print("Réponse du serveur :")
print(post_response.text)
