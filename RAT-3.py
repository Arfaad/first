def caesar(plaintext, key):
    ct = ''
    for i in range(len(plaintext)):
        c = plaintext[i
        if c == ' ':
            ct += ' '
        elif c.isupper():  # Corrected this line
            ct += chr((ord(c) + key - 65) % 26 + 65)

        elif c.islower():  # Added this condition
            ct += chr((ord(c) + key - 97) % 26 + 97)
    return ct
pt = input("Enter the plaintext: ")
k = int(input("Enter the key value: "))
enc = caesar(pt, k)
print("The encrypted Caesar cipher:", enc)





def caesar_decrypt(ciphertext, key):
    pt = ''
    for i in range(len(ciphertext)):
        t = ciphertext[i]

        if t == ' ':
            pt += ' '
        elif t.isupper():
            pt += chr((ord(t) - key - 65) % 26 + 65)
        elif t.islower():
            pt += chr((ord(t) - key - 97) % 26 + 97)
    return pt
ct = input("Enter the ciphertext: ")
k = int(input("Enter the key value: "))
dec = caesar_decrypt(ct, k)
print("The decrypted text:", dec)