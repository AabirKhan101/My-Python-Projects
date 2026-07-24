# Encryption refers to hiding a message by uisng different characters instead of each and every letter in the character, decrption refers to bringing the encrypted/ciphered message back into its original readable form
import random
import string

characters = list(" " + string.punctuation + string.digits + string.ascii_letters)
keys = characters.copy()
random.shuffle(keys)


# print(f"Characters : {characters}")
# print(f"Keys       : {keys}")


# ENCRPTION
original_text = input("Enter the message you want to encrypt: ")
ciphered_text = ""
for letter in original_text:
    index = characters.index(letter)
    ciphered_text += keys[index]

print(f"Original text : {original_text}")
print(f"Ciphered text : {ciphered_text}")

# DECRYPTION
while True:
    continuation = input("Do you want to decipher the ciphered text? (Y/N):").upper()
    if continuation == "Y":
        ciphered_text = input("Enter the message you want to decrypt: ")
        original_text = ""
        for letter in ciphered_text:
            index = keys.index(letter)
            original_text += characters[index]

        print(f"Deciphered text : {original_text}")
        break
    elif continuation=="N":
        break
