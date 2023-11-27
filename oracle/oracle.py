from Crypto.Util.number import getPrime, inverse, long_to_bytes
from flag import FLAG
from pwn import listen
from math import gcd

l = listen(port=13374)
c = l.wait_for_connection()

class Challenge():
    def __init__(self):
        self.motd = b'Welcome. I can give you as many ciphertexts as you want, RSA is secure, so what can you do?.'
        self.e = 7


    def challenge(self):
        c.sendline(self.motd)
        while True:
            c.sendline(b'Do you want me to give you a ciphertext?')
            rep = c.recvline(keepends=False)
            print(rep)
            if rep != b'yes':
                break
            else:
                p = getPrime(512)
                q = getPrime(512)
                while gcd(self.e, (p-1)*(q-1)) != 1:
                    p = getPrime(512)
                    q = getPrime(512)
                d = inverse(self.e, (p-1)*(q-1))
                N = p*q
                c.sendline(long_to_bytes(N))
                c.sendline(long_to_bytes(pow(FLAG, d, p*q)))

Challenge().challenge()
