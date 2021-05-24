# NiceEars
## Đề bài
Tác giả cho 2 file `secret.zip` và `key.mp3`, vì `secret.zip` có đặt mật khẩu, nên dự đoán rằng password giải nén được giấu trong file `key.mp3`
## Hướng giải
- Sử dụng phần mềm `Sonic Visualiser` để mở file, sử dụng mode `Spectrogram` thì có thể thấy được mật khẩu là `M0nK3y_doNkeY`
![Screenshot (25)](https://user-images.githubusercontent.com/41907864/119344280-a8b3d580-bcc1-11eb-8c17-0969d303e3aa.png)
- Sử dụng mật khẩu này để giải nén file `secret.zip` để lấy flag

Flag: HCMUS-CTF{Just_give_you_some_points_from_audio_stuff}