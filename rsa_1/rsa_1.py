from Crypto.Util.number import getPrime
from math import gcd

e = 65537
p = getPrime(100)
q = getPrime(100)
while gcd(e,(p-1)*(q-1)) != 1:
    p = getPrime(100)
    q = getPrime(100)

N = p*q

print(N)
