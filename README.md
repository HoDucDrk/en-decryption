# en-decryption
### Mã hóa & Giải mã Elgamal
**yêu cầu:**
- Python 3.9
- Tkinter
- base64

Cài Tkinter: 
```sh
pip install tk
```

Cài base64: 
```sh
pip install pybase64
```

Cài PIP
```sh
pip install pillow
```

#### copy folder Elgamal ra Desktop

**Cách sử dụng**
- Chạy file main.py
- Nhấn chọn Decryption và Encryption
- Tại Deccryption
  - Ấn `sinh khóa`
  - `Gửi khóa`

***Mã hóa***

Tại Encryption
- Nhấn `Nhận khóa`
- Ấn `Văn bản` hoặc `Ảnh` để chọn bản rõ
- `Open file` để xem trước bản rõ
- `Select path` để chọn đường dẫn và tùy chọn đặt tên file (Mặc định: ma_hoa)
- Nhấn `Mã hóa` rồi `Open file` để xem bản mã

***Giải mã***

Tại Decryption
- Nhấn `Chọn mã` để chọn file mã hóa vừa nhận.
- Ấn `Mở` để xem bản mã
- Ấn `Save file` để chọn đường dẫn lưu file. Tùy chọn đặt tên file (Mặc định: ban_ro)
- Nhấn `Giải mã` rồi `Mở bản rõ` để xem
- Ấn `Clear`
