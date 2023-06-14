def is_Prime(n):
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



# finding primilitive root with factorization method,,otherwise the code will take huge time
def findPrimitiveRoot(p):
    if not is_Prime(p):
        return -1
    phi = p - 1
    for g in range(2, p):
        if(pow(g,phi,p) == 1):
            return g
    return -1


# def powerMod(base, exponent, modulus):
#     result = 1
#     base %= modulus
#
#     while exponent > 0:
#         if exponent % 2 == 1:
#             result = (result * base) % modulus
#         base = (base * base) % modulus
#         exponent //= 2
#
#     return result


def key_Generation(g, p, x):
    return pow(g, x, p)


def Encryption1(g, p, k):
    return pow(g, k, p)


def Encryption2(y, p, k, msg):
    return (pow(y, k, p) * msg) % p


def Decryption1(cipher1, x, p):
    return pow(cipher1, x, p)


def Decryption2(cipher2, a, p):
    a_inverse = pow(a, p - 2, p)  # Computing modular inverse of 'a'
    return pow(pow(cipher2, 1, p) * a_inverse,1,p)

#10485751877499
# ElGamal algorithm

prime = int(input("Enter a prime number (p): "))
g_root = findPrimitiveRoot(prime)

private_key = int(input("Enter the private key (x): "))
message = int(input("Enter the message: "))

y_public = key_Generation(g_root, prime, private_key)
print("Public key (y):", y_public)

k_rnd = int(input("Enter a random number (k): "))

cipher1 = Encryption1(g_root, prime, k_rnd)
cipher2 = Encryption2(y_public, prime, k_rnd, message)

print("Cipher 1:", cipher1)
print("Cipher 2:", cipher2)

a_helper = Decryption1(cipher1, private_key, prime)
decrypted_msg = Decryption2(cipher2, a_helper, prime)

print("Decrypted message:", decrypted_msg)
