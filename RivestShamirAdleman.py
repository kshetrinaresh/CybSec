# Function module name: RivestShamirAdleman.py
# Python Module 2 needed for RSA algorithm (rsa-algorithm.py)
# Module: 5 (Cryptography and PKI) by Naresh Kshetri
import math
def RivestShamirAdleman(p: int, q: int, msg: int): # Function definition for RSA
    n = p * q               # S2. Compute n as pq, n = 3*7 = 21 
    t = (p - 1) * (q - 1)   # S3. Compute totient (t) as (p-1)(q-1), t = (3-1)*(7-1) = 2*6 = 12
    
    for i in range(2, t):       # S4. Public key select (e), where t is totient
        if math.gcd(i, t) == 1:  # gcd(int1, int2) returns greatest common divisor of two integers
            e = i               # gcd (2, 12) = 2, gcd (3, 12) = 3, gcd (4, 12) = 4    
            break               # gcd (5, 12) = 1, condition satisfied, then e = i, e = 5
    
    j = 0           # S5. Private key select (d), where e is public key, t is totient
    while True:     # while loop until condition is true
        if (j * e) % t == 1:    # if(0 * 5) % 12 = 0, (1 * 5) % 12 = 5, (2 * 5) % 12 = 10
            d = j               # (3 * 5) % 12 = 3, (4 * 5) % 12 = 8, (5 * 5) % 12 = 1
            break               # condition satisfied when j=5, so, d = j, d = 5
        j += 1
    
    print(f"Prime number of Alice (p): {p}\n" f"Prime number of Bob (q): {q}")
    print(f"Third computed number (n): {n}\n" f"Forth computed number (t): {t}")
    print(f"Public key selected (e/Pu): {e}\n" f"Private key selected (d/Pr): {d}") # From step 4 & 5
    print(f"\nOriginal plaintext message (oPt): {msg}")
    
    ct = pow(msg, e) % n     # S6. Encryption, Ct = (msg ^ e) modulus n, where msg < n, e is public key
    print(f"Encrypted ciphertext message (eCt): {ct}")   # 16 ^ 5 = 1,048,576 (then, 1048576 % 21 = 4)
    pt = pow(ct, d) % n      # S7. Decryption, Pt = (Ct ^ d) modulus n, where d is private key
    print(f"Decrypted plaintext message (dPt): {pt}\n")  # 4 ^ 5 = 1024 (then, 1024 % 21 = 16)