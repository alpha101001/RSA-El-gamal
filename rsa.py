import math
import random

import rsa_sign


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

# def power_mod(base, exponent, modulus):
#     result = 1
#     base %= modulus
#     base, exponent = abs(base), abs(exponent)
#     while exponent > 0:
#         if exponent & 1:
#             result = (result * base) % modulus
#         exponent >>= 1
#         base = (base * base) % modulus
#     return result

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# def modular_inverse(a, m):
#     for x in range(1, m):
#         if (a * x) % m == 1:
#             return x


def rsa_encryption(message, e, n):
    return pow(message, e, n)


def rsa_decryption(ciphertext, d, n):
    return pow(ciphertext, d, n)


def rsa_public_key_e(phi):
    while True:
        e = random.randrange(2, phi)
        if gcd(e, phi) == 1:
            return e

prime_p = int(input("Enter a prime number (p): "))
prime_q = int(input("Enter a prime number (q): "))
n = prime_p * prime_q
phi_n = (prime_p - 1) * (prime_q - 1)

public_key_e = rsa_public_key_e(phi_n)

private_key_d = pow(public_key_e,-1,phi_n)
if private_key_d is None:
    print("No valid private key found.")
    exit()

message = int(input("Enter the message: "))

# Encrypt
cipher1 = rsa_encryption(message, public_key_e, n)

# Decrypt
decrypted_msg = rsa_decryption(cipher1, private_key_d, n)

print("Decrypted message:", decrypted_msg)


