from Crypto.Util.number import getPrime, inverse
from Crypto.PublicKey import RSA
from math import gcd

e = 65537
p = getPrime(100)
q = getPrime(100)
while gcd(e,(p-1)*(q-1)) != 1:
    p = getPrime(100)
    q = getPrime(100)

N = p*q
K = RSA.construct((N,e))

with open('rsa_1/pubkey.pem','wb') as f:
    f.write(K.export_key('OpenSSH'))

# FOR DEBUG ONLY -ez writeup x)-
with open('rsa_1/privkey.pem', 'wb') as f:
    f.write(RSA.construct((N,e,inverse(e,(p-1)*(q-1)))).export_key(pkcs=8))
