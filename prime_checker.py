# Function module name: prime_checker.py
# This is python Module 1 needed for Diffie Hellman code (dh-algorithm.py)
# Python Module 2 needed is primitive_check.py
# Module: 5 (Cryptography and PKI) by Naresh Kshetri
# Function that checks if number entered is prime or not

def prime_checker(p):  
	if p < 1:   return -1
	elif p > 1:
		if p == 2:  return 1
		for i in range(2, p):
			if p % i == 0:	return -1
			return 1