from Crypto.Util.number import getPrime, inverse
from Crypto.PublicKey import RSA
from math import gcd

e = 65537
nbSecurite = 2048
p = getPrime(50)
q = getPrime(nbSecurite-50)
while gcd(e,(p-1)*(q-1)) != 1:
    p = getPrime(100)
    q = getPrime(nbSecurite-100)

N = p*q
K = RSA.construct((N,e))
 
with open('rsa_1/pubkey.pem','wb') as f:
    f.write(K.export_key('OpenSSH'))
