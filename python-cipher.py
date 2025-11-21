import string

def caesar_encrypt(message, key):
    shift = key % 26
    cipher = str.maketrans(
        string.ascii_lowercase,
        string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift]
    )
    return message.lower().translate(cipher)

def caesar_decrypt(encrypted_message, key):
    shift = 26 - (key % 26)
    cipher = str.maketrans(
        string.ascii_lowercase,
        string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift]
    )
    return encrypted_message.translate(cipher)

# Example usage:
message = "Its Mohamad Fared project"
key = 3

encrypted_message = caesar_encrypt(message, key)
print(f"Encrypted message: {encrypted_message}")

decrypted_message = caesar_decrypt(encrypted_message, key)
print(f"Decrypted message: {decrypted_message}")
