import base64

def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def main_menu():
    print("\n====== PYTHON CIPHER TOOL ======")
    print("1. Encrypt Message")
    print("2. Decrypt Message")
    print("3. Exit")
    print("================================")

def encrypt_menu():
    print("\n--- ENCRYPTION ---")
    text = input("Enter plain text: ")
    shift = int(input("Enter key (number shift): "))
    encrypted = caesar_encrypt(text, shift)
    print(f"\nEncrypted Message: {encrypted}")
    input("\nPress Enter to return to menu...")

def decrypt_menu():
    print("\n--- DECRYPTION ---")
    text = input("Enter encrypted text: ")
    shift = int(input("Enter key (number shift): "))
    decrypted = caesar_decrypt(text, shift)
    print(f"\nDecrypted Message: {decrypted}")
    input("\nPress Enter to return to menu...")

def main():
    while True:
        main_menu()
        choice = input("Select option (1–3): ")

        if choice == "1":
            encrypt_menu()
        elif choice == "2":
            decrypt_menu()
        elif choice == "3":
            print("\nExiting program...")
            break
        else:
            print("\nInvalid option. Try again.")

if __name__ == "__main__":
    main()
