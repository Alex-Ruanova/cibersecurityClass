from cryptography.fernet import Fernet

def generate_key():
    """Generate and return a Fernet key."""
    return Fernet.generate_key()

def encrypt_message(message, key):
    """Encrypt a message using the provided key."""
    fernet = Fernet(key)
    # Ensure the message is converted to bytes
    return fernet.encrypt(message.encode())

def main():
    # Generate a key
    key = generate_key()

    # Print the key; you'll need to share this with your friend securely
    print("Key:", key.decode())

    # Input the message to encrypt
    message = input("Enter the message to encrypt: ")

    # Encrypt the message
    encrypted_message = encrypt_message(message, key)

    # Print the encrypted message in a format that is easy to copy
    print("Encrypted Message:", encrypted_message.decode())

if __name__ == "__main__":
    main()
