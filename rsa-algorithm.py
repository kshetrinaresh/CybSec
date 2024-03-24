# RSA algorithm, implementation in Python
# main file (main.py), rsa-algorithm.py
# other files needed (1), RivestShamirAdleman.py
# Module: 5 (Cryptography and PKI) by Naresh Kshetri
# RSA algorithm is named after its creators, Ron Rivest, Adi Shamir, and Leonard Adleman
# Popular algorithm in cryptography, implement Enc. & Dec. of data via Python
# Developed in 1977, RSA is based on difficulty of factoring prime numbers

import RivestShamirAdleman as rsa

'''
1. Select two prime numbers – p, q (p and q both must be prime, and p != q)
[RivestShamirAdleman( ) function used for RSA approach]
2. Compute n as product of p, q; i.e., n= p X q 
[3rd number calculated as n; this “n” is made public]
3. Compute totient (4th number), t = (p - 1) X (q - 1)    
4. Public key, e using gcd (t, e) = 1, where 1 < e < t
[import python math module, if math.gcd (i, t) == 1: e = i]
5. Calculate private key, d using (d * e mod t = 1)
6. Encryption, Ct = (msg ^ e) mod n, where msg < n
7. Decryption, Pt = (Ct ^ d) mod n
'''

print ("*** Implementation of RSA algorithm via Python ***\n") # S1. Select two prime numbers, p and q
print ("RSA Function call I \n- - - - - - - - - - - - - - - - - - - - - - - -")
rsa.RivestShamirAdleman(3, 7, 16)      # Function call 1, where p = 3, q = 7, Pt = 16
print ("RSA Function call II \n- - - - - - - - - - - - - - - - - - - - - - - -")
rsa.RivestShamirAdleman(53, 59, 890)   # Function call 2, where p = 53, q = 59, Pt = 890