from Crypto.Util.number import bytes_to_long, long_to_bytes
from pwn import remote

r = remote('localhost', int(13374))

print(r.recvline())
Ns = list()
flags = list()

for _ in range(2):
    print(r.recvline())
    r.sendline(b'yes')
    Ns.append(bytes_to_long(r.recvline(keepends=False)))
    flags.append(bytes_to_long(r.recvline(keepends=False)))

r.close()

print(long_to_bytes(int(CRT(flags, Ns)).nth_root(7)))

