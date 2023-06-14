import math

def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

def bigmod(a, b, n):
    if b == 0:
        return 1
    x = bigmod(a, b // 2, n) % n
    x = (x * x) % n
    if b % 2 == 1:
        x = (x * a) % n
    return x

msg = "transposition"
key = "oman"
m = math.ceil(len(msg) / len(key))
n = len(key)
matrix1 = [['' for _ in range(n)] for _ in range(m)]

k = 0
for i in range(m):
    for j in range(n):
        if k < len(msg):
            matrix1[i][j] = msg[k]
            k += 1
        else:
            matrix1[i][j] = '*'

for i in range(m):
    for j in range(n):
        print(matrix1[i][j], end='')
    print()

mp = []
for i in range(len(key)):
    t = (ord(key[i]) - ord('a'), i)
    mp.append(t)
mp.sort()

key_ara = [mp[i][1] for i in range(len(key))]

for i in range(len(key)):
    print(key_ara[i], end='')
print()

cipher = ""
for j in range(n):
    for i in range(m):
        cipher += matrix1[i][key_ara[j]]

print(cipher)

matrix2 = [['' for _ in range(n)] for _ in range(m)]

k = 0
for j in range(n):
    for i in range(m):
        matrix2[i][key_ara[j]] = cipher[k]
        k += 1

for i in range(m):
    for j in range(n):
        print(matrix2[i][j], end='')
    print()

dm = ""
for i in range(m):
    for j in range(n):
        if matrix2[i][j] != "*":
            dm += matrix2[i][j]

print(dm)
