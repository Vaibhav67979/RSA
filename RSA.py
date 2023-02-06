p = int(input("Enter p : "))
q = int(input("Enter q : "))
e = int(input("Enter e : "))
m = int(input("Enter message to encrypt : "))
n = p * q
phi = (p - 1) * (q - 1)


def gcd(a, h):
    temp = 0
    while (1):
        temp = a % h
        if (temp == 0):
            return h
        a = h
        h = temp


if gcd(p,q) == 1:
    d = pow(e, -1, phi)
    print(d)


c = pow(m, e, n)
print(f"encrypted text : {c}")

dec = pow(c, d, n)
print(f"original text : {dec}")
