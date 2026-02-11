import hashlib
import sys

print("Bem vindo ao sistema")

def get_hash(file_path):
    try:
        with open(file_path, "rb") as f:
            file_bytes = f.read()
            return hashlib.sha256(file_bytes).hexdigest()
    except FileNotFoundError:
        return "Arquivo não foi encontrado."

#Validação de args
if len(sys.argv) > 1:
    print(f"sha256: {get_hash(sys.argv[1])}")
else:
    print("Uso: python script.py <caminho_do_arquivo>")