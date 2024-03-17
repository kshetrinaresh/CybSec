# Function module name: primitive_check.py
# This is python Module 2 needed for Diffie Hellman code (dh-algorithm.py)
# Python Module 1 needed is prime_checker.py
# Module: 5 (Cryptography and PKI) by Naresh Kshetri
# Function that checks if entered no. is primitive root or not

def primitive_check(g, p, L):	
	for i in range(1, p):	L.append(pow(g, i) % p)
	for i in range(1, p):
		if L.count(i) > 1:
			L.clear()
			return -1
		return 1