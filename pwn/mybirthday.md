# Đề bài
```c
int __cdecl main(int argc, const char **argv, const char **envp)
{
  int v3; // ebx
  int v4; // ebp
  int v6; // [esp-3Ch] [ebp-3Ch]
  int v7; // [esp-38h] [ebp-38h]
  int v8; // [esp-34h] [ebp-34h]
  int v9; // [esp-30h] [ebp-30h]
  int v10; // [esp-2Ch] [ebp-2Ch]
  int v11; // [esp-28h] [ebp-28h]
  int v12; // [esp-24h] [ebp-24h]
  int v13; // [esp-20h] [ebp-20h]
  signed int v14; // [esp-14h] [ebp-14h]
  int *v15; // [esp-10h] [ebp-10h]
  int v16; // [esp-Ch] [ebp-Ch]
  int v17; // [esp-8h] [ebp-8h]
  void *v18; // [esp-4h] [ebp-4h]
  void *retaddr; // [esp+0h] [ebp+0h]

  __asm { endbr32 }
  v18 = retaddr;
  v17 = v4;
  v16 = v3;
  v15 = &argc;
  setup();
  sub_80490B0("Tell me your birthday?", v6, v7, v8, v9, v10, v11, v12, v13);
  v14 = 30;
  sub_80490A0(0, &v10);
  if ( v14 == 0xCABBFEFF )
    run_cmd("/bin/bash");
  else
    run_cmd("/bin/date");
  return 0;
}
```