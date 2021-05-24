# bank1
## Đề bài
- Tác giả chỉ cho IP và port của service mà không cho binary, chắc trêu!!!
- Thử kết nối `netcat` tới service thì nhận được response là `Please enter your name:`
- Thầm nghĩ chắc bài này ez thôi, chắc lại buffer-overflow thôi, thử nhập input thật dài => flag
```
[+] Please enter your name: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
[+] Thanks for the registration, your balance is 1633771873.
HCMUS-CTF{that_was_easy_xd}
```