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
public getFlag
getFlag proc near

var_4= dword ptr -4

push    ebp
mov     ebp, esp
push    ebx
sub     esp, 4
call    __x86_get_pc_thunk_ax
add     eax, 1AEEh
sub     esp, 0Ch
lea     edx, (aCatFlagTxt - 804A000h)[eax] ; "cat flag.txt"
push    edx             ; command
mov     ebx, eax
call    _system
add     esp, 10h
nop
mov     ebx, [ebp+var_4]
leave
retn
```