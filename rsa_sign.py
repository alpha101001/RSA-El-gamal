import hashlib
import random

def rsa_public_key_e(phi):
    while True:
        e = random.randrange(2, phi)
        if gcd(e, phi) == 1:
            return e

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

def rsa_sign_generator(message, private_key_d, n):
    return pow(message, private_key_d, n)

def rsa_sign_verification(message, signature, public_key_e, n):
    decrypted_signature = pow(signature, public_key_e, n)
    return decrypted_signature == message

prime_p = int(input("Enter a prime number (p): "))
prime_q = int(input("Enter a prime number (q): "))
n = prime_p * prime_q
phi_n = (prime_p - 1) * (prime_q - 1)
public_key_e = rsa_public_key_e(phi_n)
private_key_d = pow(public_key_e, -1, phi_n)
if private_key_d is None:
    print("No valid private key found.")
    exit()
message = int(input("Enter the message: "))

signature = rsa_sign_generator(message, private_key_d, n)
verification = rsa_sign_verification(message, signature, public_key_e, n)

print("Message:", message)
print("Signature:", signature)
print("Verification:", verification)
