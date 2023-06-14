import hashlib
import random
import math
def SHA512(data):
    sha512_hash = hashlib.sha512()
    sha512_hash.update(data.encode('utf-8'))
    hex_digest = sha512_hash.hexdigest()
    return hex_digest


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def key_Generation(g, p, x):
    return pow(g, x, p)


def findPrimitiveRoot(p):
    if not is_prime(p):
        return -1
    phi = p - 1
    for g in range(2, p):
        if(pow(g,phi,p) == 1):
            return g
        else: return -1
def non_prime_Primitive_root(non_prime):
    i = 2
    list = []
    while i<=math.sqrt(non_prime):
        if non_prime%i == 0:
            list.append(i)
        else:
            i += 1
            while not is_prime(i):
                i += 1
    phi_n = 0
    while i in range(len(list)):
        phin = phi_n + list[i]
    while i in range(2,non_prime):
        if pow(i,phi_n,non_prime) == 1:
            return i


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def el_gamal_sign_generator(message, g_root, prime, private_key_x, k_rnd):
    r = pow(g_root, k_rnd, prime)
    if pow(k_rnd, -1, prime - 1) is None:
        print("No valid modular inverse found.")
        exit()
    s = ((message - private_key_x * r) * pow(k_rnd, -1, prime - 1)) % (prime - 1)
    return  r , s


def el_gamal_sign_verification(message, y_public, r, s, prime, g_root):
    v1 = (pow(y_public, r, prime) * pow(r, s, prime)) % prime
    v2 = pow(g_root, message, prime)
    return v1 == v2


prime = int(input("Enter a prime number (p): "))
g_root = findPrimitiveRoot(prime)

private_key_x = int(input("Enter the private key (x): "))
message = int(input("Enter the message: "))

y_public = key_Generation(g_root, prime, private_key_x)
print("Public key (y):", y_public)

k_rnd = int(input("Enter a random number (k): "))

r , s = el_gamal_sign_generator(message, g_root, prime, private_key_x, k_rnd)
signature = r, s
verification = el_gamal_sign_verification(message, y_public, r, s, prime, g_root)

print("Message:", message)
print("Signature:", signature)
print("Verification:", verification)
