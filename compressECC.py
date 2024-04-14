'''
Function module name: compressECC.py
Python module needed for ECC DHP implementation
To be used with: EllipticCurve-DHP.py
Module: 5 (Cryptography & PKI) by Dr. Naresh Kshetri
'''

# Function to calculate Elliptic curves compress point
def compressECC(publicKey):
    x1 = hex(publicKey.x)   # hex function convert an integer into hexadecimal
    y1 = hex(publicKey.y % 2) # stores remainder as 2 is divisor, publicKey.y is dividend
    return x1 + y1 [2: ]   # return the value, x1 + y1, retrieving all slice from index 2 
