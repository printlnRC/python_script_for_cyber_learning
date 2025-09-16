import base64

code_b64 = "PCFTAQGTNWUOGQDVNUVU"
decoded = base64.b64decode(code_b64)

print("Octets bruts :", decoded)
print("En hexadécimal :", decoded.hex())
