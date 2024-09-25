# Caesar Cipher code, implementation of encryption (Pt - Ct)
# Main file, caesar_cipher.py
# Other file(s) needed: None
# Cryptography and PKI by Naresh Kshetri

print(" - - - - - Caesar Cipher Test - - - - - ")


def encrypt_letter(letter, shift):  # function to encrypt the letter provided
    ascii = ord(letter)             # Convert the letter to ASCII value, use ord() function
    add_ascii = ascii + shift       # Add the shift value to the converted ASCII value
    conv_char = chr(add_ascii)      # Convert back final value to character, use chr() function
    return conv_char                # return the converted character


def encrypt_message(pt, shift):     # function to encrypt message with help of encrypt_letter( )
    print 'Plaintext is:', pt       # prints the plaintext message
    ct = ''                         # declare ciphertext as empty string in the beginning
    i = 0                           # declare counter i as zero in the beginning
    while i < len(pt):              # while loop until condition, counter i is less than plaintext length
        letter = encrypt_letter(pt[i], shift)  # encrypt character one by one, pt[0], pt[1] ...
        ct = ct + letter            # concatenate it (letter) to ciphertext
        i = i + 1                   # counter variable i increment by 1
    print 'Ciphertext is:', ct      # prints the output ciphertext in the end, KHOOR


encrypt_message('ABC', 3)       # function call with plaintext 'ABC' and shift value 3
encrypt_message('HELLO', 3)     # function call with plaintext 'HELLO' and shift value 3
