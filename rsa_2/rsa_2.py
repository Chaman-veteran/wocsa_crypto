from Crypto.Util.number import getPrime
from math import gcd
from flag import FLAG

e = 3
p = getPrime(2048)
q = getPrime(2048)
while gcd(e,(p-1)*(q-1)) != 1:
    p = getPrime(2048)
    q = getPrime(2048)

N = p*q
flag = pow(FLAG, e, N)
with open('rsa_2/output','w') as f:
    f.write(('0' if len(hex(flag))%2 != 0 else'')+hex(flag)[2:])
