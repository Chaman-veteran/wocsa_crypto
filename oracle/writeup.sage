from Crypto.Util.number import long_to_bytes
from pwn import remote

r = remote('192.168.9.57', int(9999))

print(r.recvline())

e = 7
flags = 1
Ns = 1

while True:
    print(r.recvline())
    r.sendline(b'yes')
    N = r.recvline(keepends=False).decode()
    flag = r.recvline(keepends=False).decode()
    flags = CRT([flags, int(flag,16)], [Ns, int(N,16)])
    try:
        flags.nth_root(e)
        break
    except:
        pass
    Ns *= int(N, 16)

r.close()

print(long_to_bytes(flags.nth_root(e)))
