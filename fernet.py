#Cifrado Fernet

#Importamos la libreria Fernet
from cryptography.fernet import Fernet

#Generamos una clave
clave = Fernet.generate_key()

#Creamos la instancia de fernet
f = Fernet(clave)

#Encryptamos el mensaje
token = f.encrypt(b"Mi mensaje secreto")

print(token)
