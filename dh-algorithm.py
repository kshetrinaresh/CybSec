# Diffie-Hellman Code, implementation of algorithm
# main file, dh-algorithm.py
# other files needed (2), prime_checker.py, primitive_check.py
# Module: 5 (Cryptography and PKI) by Naresh Kshetri

import prime_checker as pc      # alias pc for module prime_checker.py
import primitive_check as pt    # alias pt for module primitive_check.py

l = [ ] #l declared as empty list
print ("\nImplementation of DIFFIE-HELLMAN Key Exchange Algorithm ")
print("1. Alice prime number = P, Bob primitive root = G")
print("2. Alice choose private key = a, Bob choose private key = b")
print("3. Alice calculates A1 & sends to Bob, Bob calculates B1 & sends to Alice")
print("4. Alice computes secret key as k1, Bob computes secret key as k2")
print("5. If k1 = k2, key exchange success, k1 != k2, key exchange unsuccess")
print("\n***************************************************************************")

while 1:
	P = int(input("Please enter public prime number for Alice (P): "))
	if pc.prime_checker(P) == -1:
		print("Sorry, number isn't PRIME, please enter again !")
		continue
	break

while 1:
	G = int(input(f"Please enter primitive root of {P} for Bob (G): ")) 
	if pt.primitive_check(G, P, l) == -1: # prime no. 23 has ten primitive roots as 5, 7, 10, 11, 14, 15, 17, 19, 20, 21
		print(f"Number is not a primitive root of {P}, Please try again!")
		continue
	break

# Private Keys a for Alice and b for Bob
a = int(input("\nPlease choose Alice private key (a): ")) 
b = int(input("Please choose Bob private key (b) : "))
while 1:
	if a >= P or b >= P:
		print(f"Private key of both users should be less than {P}!")
		continue
	break

A1 = pow(G, a) % P      # Alice calculate public key (A1) = G (power a) modulus P [11power3 mod 23 = 20] 
B1 = pow(G, b) % P      # Bob calculate public key (B1) = G (power b) modulus P [11power4 mod 23 = 13]

k1 = pow(B1, a) % P     # Alice compute her secret key (k1) = B1 (power a) mod P [13power3 mod 23 = 12] 
k2 = pow(A1, b) % P     # Bob compute his secret key (k2) = A1 (power b) mod P [20power4 mod 23 = 12] 

print("\n***************************************************************************") 
print(f"Alice public key A1 = G (power a) modulus P: {A1} [send to bob]")  
print(f"Bob public key B1 = G (power b) modulus P: {B1} [send to Alice]")
print(f"\nSecret key (k1) for Alice (P, a, B1) is {k1}")
print(f"Secret key (k2) for Bob (G, b, A1) is {k2}")

if k1 == k2:  print("\nCongratulations (k1 = k2) ... Keys exchange success !")
else:	print("\nSorry (k1 != k2) ... Keys exchange unsuccess")
