'''
Elliptic curve cryptography Diffie-Hellman Protocol (ECDH) Implementation (in Python)
Main file (main.py) or EllipticCurve-DHP.py, Key agreement algorithm
Prereq: ECDHP, Cryptography techniques, & Python programming basics
Other file needed for this program: N/A
Module: 5 (Cryptography and PKI) by Dr. Naresh Kshetri
'''

# Import libraries needed, tinyec is a tiny library to perform arithmetic operations on elliptic curves
from tinyec import registry as rg     # registry module to obtain keys and values from registry hives
import secrets as sc                  # secrets module to generate cryptographically strong random numbers
import compressECC as cp              # function module to calculate Elliptic curves compress point  

curve = rg.get_curve('brainpoolP256r1') # elliptic curve used for ECDH calculations
 
print("**** Implementation of ECC Diffie-Hellman Protocol (ECDH) key agreement algorithm via Python ****")
# Generation of secret key and public key 
Ka = sc.randbelow(curve.field.n)    # randbelow (n) function returns a random integer in range [0, n).
SecretKeyA = Ka * curve.g    # secret key of Alice
print("\nAlice secret key A, SecretKeyA: \n", cp.compressECC(SecretKeyA))

Kb = sc.randbelow(curve.field.n) # secrets module provide access to secure randomness source
SecretKeyB = Kb * curve.g    # secret key of Bob
print("Bob secret key B, SecretKeyB: \n", cp.compressECC(SecretKeyB))

print("\nCurrently exchanged public key between Alice and Bob (e.g., through Internet)\n") 
#(SharedKeyA): represents user Alice/A, (SharedKeyB): represents user Bob/B 
SharedKeyA = Ka * SecretKeyB 
print("Key shared by Alice (A), SharedKeyA: \n", cp.compressECC(SharedKeyA))
SharedKeyB = Kb * SecretKeyA 
print("Key shared by Bob (B), SharedKeyB: \n",cp.compressECC(SharedKeyB))
print("\nEqual shared keys (SharedKeyA, SharedKeyB) with both users (Alice & Bob): ", SharedKeyA == SharedKeyB)
print("Shared keys are equal, message exchange success !") 
