from Crypto.Util.number import getPrime, inverse
from Crypto.PublicKey import RSA
from math import gcd

e = 65537
p = getPrime(100)
q = getPrime(100)
while gcd(e,(p-1)*(q-1)) != 1:
    p = getPrime(100)
    q = getPrime(100)

d = inverse(e,(p-1)*(q-1))
N = p*q

K = RSA.construct((N,e,d))
with open('rsa_1/privkey.pem','wb') as f:
    f.write(K.export_key())

with open('rsa_1/pubkey.pem','wb') as f:
    f.write(K.public_key().export_key())
