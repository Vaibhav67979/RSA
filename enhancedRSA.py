import random

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inv(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def generate_keypair(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randrange(1, phi)

    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    d = mod_inv(e, phi)
    return ((e, n), (d, n))

def encrypt(plaintext, key):
    e, n = key
    cipher = [(ord(char) ** e) % n for char in plaintext]
    print(type(cipher))
    return cipher

def decrypt(ciphertext, key):
    d, n = key
    plain = [chr((char ** d) % n) for char in ciphertext]
    return ''.join(plain)

if _name_ == '_main_':
    p = int(input("Enter a prime number (17, 19, 23, etc): "))
    q = int(input("Enter another prime number (Not one you entered above): "))
    print("Generating your public/private keypairs now . . .")
    public, private = generate_keypair(p, q)
    print("Your public key is ", public, " and your private key is ", private)
    message = input("Enter a message to encrypt with your public key: ")
    encrypted_msg = encrypt(message, public)
    print("Your encrypted message is: ")
    print(''.join(map(lambda x: str(x), encrypted_msg)))
    print("Decrypting message with private key . . .")
    print("Your message is:")
    print(decrypt(encrypted_msg, private))
