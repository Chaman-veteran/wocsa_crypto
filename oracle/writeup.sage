from Crypto.Util.number import long_to_bytes
from pwn import remote

<<<<<<< Updated upstream
r = remote('localhost', int(9999))
=======
r = remote('192.168.9.57', int(9999))
>>>>>>> Stashed changes

print(r.recvline())
Ns = list()
flags = list()

for _ in range(5):
    print(r.recvline())
    r.sendline(b'yes')
    N = r.recvline(keepends=False).decode()
    Ns.append(int(N, 16))
    flag = r.recvline(keepends=False).decode()
    flags.append(int(flag, 16))

r.close()

print(long_to_bytes(Integer(CRT(flags, Ns)).nth_root(7)))
