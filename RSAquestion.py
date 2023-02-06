import random


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def generate_primes():
    p = random.randint(10 ** 3, 10 ** 4)
    q = random.randint(10 ** 3, 10 ** 4)
    while not all(gcd(p, i) == 1 for i in range(2, p)) or not all(gcd(q, i) == 1 for i in range(2, q)):
        p = random.randint(10 ** 3, 10 ** 4)
        q = random.randint(10 ** 3, 10 ** 4)
    return p, q


p, q = generate_primes()

# Modulus
n = p * q

# Totient
phi = (p - 1) * (q - 1)

# Public exponent
e = random.randint(2, phi - 1)
while gcd(e, phi) != 1:
    e = random.randint(2, phi - 1)

# Private exponent
d = 1
while (d * e) % phi != 1:
    d += 1

print("p: ", p)
print("q: ", q)
print("n: ", n)
print("phi: ", phi)
print("e: ", e)
print("d: ", d)
