# metadata
## Hướng giải
- Tác giả nói rằng đã tạo 1 docker container và có đường dẫn là `vinhph2/hcmus-ctf-2021`
- Thông thường thì các container sẽ được chia sẻ lên docker hub, thử truy cập `https://hub.docker.com/r/vinhph2/hcmus-ctf-2021` thì thấy container này tồn tại

![Screenshot 2021-05-24 190548](https://user-images.githubusercontent.com/41907864/119345497-29bf9c80-bcc3-11eb-8ddc-f19462fe00de.png)

- Tiếp tục truy cập vào `Tags` mới nhất để xem `Image layers`

![Screenshot 2021-05-24 190738](https://user-images.githubusercontent.com/41907864/119345619-52e02d00-bcc3-11eb-9db0-8effb0051651.png)

- Trong `Image layers`chứa khá nhiều thông tin, trong đó có flag fake và flag thật

Flag: HCMUS-CTF{d0ck6r_1mag6_1nsp6ct}