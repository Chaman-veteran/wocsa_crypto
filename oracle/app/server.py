from Crypto.Util.number import getPrime
from flag import FLAG

class Challenge():
    def __init__(self):
        self.motd = b'Welcome. I can give you as many ciphertexts as you want, RSA is secure, so what can you do?.'
        self.e = 7

    def challenge(self):
        print(self.motd)
        while True:
            print(b'Do you want me to give you a ciphertext?')
            rep = input()
            if not 'yes' in rep:
                break
            else:
                p = getPrime(512)
                q = getPrime(512)
                N = p*q
                flag = pow(FLAG, self.e, p*q)

                N = ('0' if len(hex(N))%2 != 0 else'')+hex(N)[2:]
                flag = ('0' if len(hex(flag))%2 != 0 else'')+hex(flag)[2:]

                print(N)
                print(flag)

if __name__ == '__main__':
    try:
        Challenge().challenge()
    except:
        exit()
