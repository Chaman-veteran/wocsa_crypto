from Crypto.Util.number import getPrime
from flag import FLAG
from pwn import listen

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
            if rep != b'yes':
                break
            else:
                p = getPrime(512)
                q = getPrime(512)
                N = p*q
                flag = pow(FLAG, self.e, p*q)

                N = ('0' if len(hex(N))%2 != 0 else'')+hex(N)[2:]
                flag = ('0' if len(hex(flag))%2 != 0 else'')+hex(flag)[2:]

                c.sendline(str(N).encode())
                c.sendline(str(flag).encode())

Challenge().challenge()
