from cryptography.fernet import Fernet

def decrypt_message(encrypted_message, key):
    """Decrypt an encrypted message using the provided key."""
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_message.encode()).decode()

def main():
    # Input the key shared by you
    key = input("Enter the decryption key: ")

    # Input the encrypted message received
    encrypted_message = input("Enter the encrypted message: ")

    # Decrypt the message
    try:
        decrypted_message = decrypt_message(encrypted_message, key)
        print(f"Decrypted message: {decrypted_message}")
    except Exception as e:
        print(f"An error occurred during decryption: {e}")

if __name__ == "__main__":
    main()
