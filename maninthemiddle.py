import hashlib
import random

def simple_encrypt(message, secret_key):
    """Una función simple para 'encriptar' mensajes usando la clave secreta."""
    encrypted = ''.join(chr((ord(char) + secret_key) % 256) for char in message)
    return encrypted

def simple_decrypt(encrypted_message, secret_key):
    """Una función simple para 'desencriptar' mensajes usando la clave secreta."""
    decrypted = ''.join(chr((ord(char) - secret_key) % 256) for char in encrypted_message)
    return decrypted

# Parámetros del algoritmo Diffie-Hellman
g = 2
p = 2410312426921032588552076022197566074856950548502459942654116941958108831682612228890093858261341614673227141477904012196503648957050582631942730706805009223062734745341073406696246014589361659774041027169249453200378729434170325843778659198143763193776859869524088940195577346119843545301547043747207749969763750084308926339295559968882457872412993810129130294592999947926365264059284647209730384947211681434464714438488520940127459844288859336526896320919633919

# Generación de claves privadas
alice = random.getrandbits(256)
bob = random.getrandbits(256)
eve = random.getrandbits(256)

# Generación de claves públicas y secretas
A = pow(g, alice, p)  # Alice's public key
B = pow(g, bob, p)    # Bob's public key
E_A = pow(g, eve, p)  # Eve's public key sent to Alice
E_B = pow(g, eve, p)  # Eve's public key sent to Bob

s_alice_eve = pow(E_A, alice, p)  # Secret key between Alice and Eve
s_bob_eve = pow(E_B, bob, p)      # Secret key between Bob and Eve

# Simplificación de las claves secretas para usar en la 'encriptación'
# Normalmente, se derivaría una clave más compleja a partir de s_alice_eve y s_bob_eve
secret_key_eve_alice = int(hashlib.sha256(str(s_alice_eve).encode()).hexdigest(), 16) % 256
secret_key_eve_bob = int(hashlib.sha256(str(s_bob_eve).encode()).hexdigest(), 16) % 256

# Simulando el intercambio de mensajes
mensaje_de_bob = "Hola Alice, ¿cómo estás?"
mensaje_de_alice = "Hola Bob, todo bien. ¿Y tú?"

# Eve intercepta, 'descifra' y luego 'cifra' el mensaje de Bob a Alice
mensaje_interceptado_de_bob = simple_encrypt(mensaje_de_bob, secret_key_eve_bob)
respuesta_de_eve_a_bob = simple_decrypt(mensaje_interceptado_de_bob, secret_key_eve_bob)
respuesta_cifrada_de_eve_a_bob = simple_encrypt("Estoy bien, gracias por preguntar. ¿Cómo va tu día?", secret_key_eve_bob)

# Eve intercepta, 'descifra' y luego 'cifra' el mensaje de Alice a Bob
mensaje_interceptado_de_alice = simple_encrypt(mensaje_de_alice, secret_key_eve_alice)
respuesta_de_eve_a_alice = simple_decrypt(mensaje_interceptado_de_alice, secret_key_eve_alice)
respuesta_cifrada_de_eve_a_alice = simple_encrypt("Todo va bien, ¡gracias!", secret_key_eve_alice)

# Mostrar resultados
print(f"Mensaje original de Bob: {mensaje_de_bob}")
print(f"Mensaje interceptado y descifrado por Eve (de Bob): {respuesta_de_eve_a_bob}")
print(f"Respuesta cifrada de Eve a Bob: {respuesta_cifrada_de_eve_a_bob}")

print(f"\nMensaje original de Alice: {mensaje_de_alice}")
print(f"Mensaje interceptado y descifrado por Eve (de Alice): {respuesta_de_eve_a_alice}")
print(f"Respuesta cifrada de Eve a Alice: {respuesta_cifrada_de_eve_a_alice}")
