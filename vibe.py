from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os

# Key and IV generation
key = get_random_bytes(16)  # 128-bit key for AES
iv = get_random_bytes(16)   # Initialization vector for AES CBC mode

# Encrypt the script
def encrypt_script(input_file, output_file, key, iv):
    # Read original Python script
    with open(input_file, 'rb') as f:
        data = f.read()
    
    # Pad data to be a multiple of AES block size
    padding_length = AES.block_size - len(data) % AES.block_size
    data += bytes([padding_length]) * padding_length

    # Encrypt data
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(data)

    # Write the encrypted file
    with open(output_file, 'wb') as f:
        f.write(iv + ciphertext)  # Prepend IV for decryption
    print(f"Encrypted script saved as {output_file}")

# Encrypt the script file
encrypt_script('vibration_analysis.py', 'vibration_analysis.enc', key, iv)
