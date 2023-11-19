from Crypto.Cipher import Twofish
from Crypto.Random import get_random_bytes

# Create a Twofish cipher object with a random key
key = get_random_bytes(16)  # 16 bytes for a 128-bit key
cipher = Twofish.new(key, Twofish.MODE_ECB)

# The plaintext data you want to encrypt
plaintext = b'Hello, Twofish!'

# Encrypt the data
ciphertext = cipher.encrypt(plaintext)
print("Ciphertext:", ciphertext)

# Decrypt the data
decrypted_text = cipher.decrypt(ciphertext)
print("Decrypted text:", decrypted_text.decode('utf-8'))
