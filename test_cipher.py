# test_cipher.py
# Test script for cipher.py

from cipher import encrypt, decrypt

# Test case from the lab instructions
plaintext = 'I am just "plain" text ~ 12345.'
password = 'P@55w0rd!~'

#Encrypt the plaintext
ciphertext = encrypt(plaintext, password)
print("Ciphertext:")
print(ciphertext)


#Decrypt the ciphertext
decrypted_text = decrypt(ciphertext, password)
print("\nDecrypted Text:")
print(decrypted_text)

# Compare to original
if decrypted_text == plaintext:
    print("\n Test Passed: Decrypted text matches original plaintext.")
else:
    print("\n Test Failed: Decrypted text does not match original.")
    
    
#------------------------------------------------------------------------    
# Test: Cipher must respond to different passwords
print("\n Test password sensitivity....")

plaintext = "This is a password sensitivity test."

password1 = "SimplePassword123"
password2 = "AnotherOne!@#"

# Encrypt the same plaintext with two different passwords
cipher1 = encrypt(plaintext, password1)
cipher2 = encrypt(plaintext, password2)

# Check that ciphertexts are different
if cipher1 != cipher2:
    print("Passed: Different passwords produce different ciphertext.")
else:
    print("Failed: Different passwords produced the same ciphertext.")
    
# Decrypt using correct passwords
decrypted1 = decrypt(cipher1, password1)
decrypted2 = decrypt(cipher2, password2)

# Check that each decrypts correctly
if decrypted1 == plaintext and decrypted2 == plaintext:
    print("Passed: Each ciphertext decrypted correctly with its password.")
else:
    print("Failed: Decryption did not match original with correct password.")
    
# Try decrypting with the wrong password
wrong_decrypt = decrypt(cipher1, password2)
if wrong_decrypt != plaintext:
    print("Passed: Wrong password failed to decrypt correctly.")
else:
    print("Failed: Wrong password still decrypted correctly.") 
    
    
#--------------------------------------------------------------------------
# Test try many passwords
#-------------------------------------------------------------------------

print("\n Test multiple passwords....")

plaintext = "This is a consistent test message."

passwords = [
    "password123",
    "letmein",
    "OpenSesame!",
    "1234567890",
    "abcDEF123",
    "!@#$%^&*()_+",
    "P@55w)rd!~",
    "spaces are fine",
    "short me" 
    "ThisIsALongerPasswordWithSymbols&Numbers123"
]


for pw in passwords:
    encrypted = encrypt(plaintext, pw)
    decrypted = decrypt(encrypted, pw)
    match = decrypted == plaintext
    print(f"Password: {pw}")
    print(f"Match: {'yes' if match else 'no'}")
    if not match:
        print(f"  Decrypted output: {decrypted}")