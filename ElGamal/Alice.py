from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import filedialog
import script as s
from tkinter import ttk
from pathlib import Path
from PIL import Image, ImageTk
import os
import glob
import json


class Alice():
    def __init__(self, master):
        # configure
        self.master = master
        self.frame = ttk.Frame(master)
        frame = self.frame
        frame.grid()
        my_canvas = Canvas(frame, width=300, height=1, bg='black')
        self.file_ciphertext = StringVar()
        self.buttonClick = False
        # title
        ttk.Label(frame, text='Decryption',
                  foreground='green').grid(row=0, column=0)

        # Button
        sinh_khoa = ttk.Button(frame, text="sinh khóa", command=self.save_key)
        send_key = ttk.Button(frame, text='Gửi khóa', command=self.send_key)
        select_ciphertext = ttk.Button(
            frame, text='Chọn mã', command=self.get_file_path)
        open_ciphertext = ttk.Button(frame, text='Mở', command=self.open_crip)
        decryption = ttk.Button(frame, text='Giải mã', command=self.decd)
        open_plaintext = ttk.Button(
            frame, text='Mở bản rõ', command=self.open_dec)
        delete_file = ttk.Button(frame, text='Clear', command=self.clear)
        # Entry
        path = ttk.Entry(frame, textvariable=self.file_ciphertext, width=27)
        self.set_name = ttk.Entry(frame, width=12)
        self.set_name.insert(15, 'ban_ro')

        # Label setting
        self.public_key_value = StringVar()
        self.public_key_value.set('')

        self.status_value = StringVar()
        self.status_value.set('')
        # label
        display_public_key = ttk.Label(frame, text="Public key:")
        ttk.Label(frame, textvariable=self.public_key_value).grid(
            row=1, column=3, columnspan=2)
        label_rename = ttk.Label(frame, text='Đặt tên')
        status = ttk.Label(frame, text="Status: ")
        set_status = ttk.Label(frame, textvariable=self.status_value)
        ttk.Label(frame, text="Bản mã").grid(row=0, column=5)
        ttk.Label(frame, text=" ").grid(row=0, column=4)
        ttk.Label(frame, text="Bản rõ").grid(row=0, column=10)

        # Text
        self.text_box_plan = Text(frame,  height=12, width=50)
        self.text_box_crip = Text(frame,  height=12, width=50)

        # setting layout
        sinh_khoa.grid(row=1, column=0)
        send_key.grid(row=1, column=1)
        self.text_box_crip.grid(row=1, column=5, columnspan=5, rowspan=5)
        self.text_box_plan.grid(row=1, column=10, columnspan=5, rowspan=5)
        select_ciphertext.grid(row=2, column=0)
        open_ciphertext.grid(row=2, column=3)
        label_rename.grid(row=3, column=0)
        self.set_name.grid(row=3, column=1)
        decryption.grid(row=4, column=0)
        open_plaintext.grid(row=4, column=1)
        delete_file.grid(row=5, column=0)
        display_public_key.grid(row=1, column=2)

        path.grid(row=2, column=1, columnspan=2)

        status.grid(row=10, column=0)
        set_status.grid(row=10, column=1)

        my_canvas.grid(row=11, column=0, columnspan=100)

    def save_key(self):
        s.key_generation()
        get_public_key = s.__init__.toInt(
            json.loads(s.open_file("./keys/public_key.txt")))
        public_key_value = "p: " + \
            str(get_public_key["q"]) + ", a: " + str(get_public_key["a"])
        self.public_key_value.set(public_key_value)

    def send_key(self):
        if(self.buttonClick == False):
            self.buttonClick = not self.buttonClick
            open('./ciphertext/controller/status.txt', 'w+')
            self.status_value.set('Thành Công!')

    def get_file_path(self):
        filetype = (
            ('text files', '*.txt'),
            ('All files', '*.*')
        )
        self.file_ciphertext.set(askopenfilename(filetypes=filetype))

    def open_crip(self):
        file = self.file_ciphertext.get()
        cipher = open(file, 'r', encoding='utf-8')

        def character_limit(entry_text):
            if len(entry_text) > 0:
                entry_text = entry_text[:10000]
            return entry_text
        text = character_limit(cipher.read())
        self.text_box_crip.insert('end', text)

    def clear(self):
        try:
            files = glob.glob("./ciphertext/controller/*")
            files_t = glob.glob("./ciphertext/*.txt")
            files_key = glob.glob("./keys/*")
            for f in files:
                os.remove(f)
            for f in files_t:
                os.remove(f)
            for f in files_key:
                os.remove(f)
            self.public_key_value.set('')
            self.file_ciphertext.set('')
            self.status_value.set('')
            self.text_box_crip.delete('1.0', END)
            self.text_box_plan.delete('1.0', END)
            self.buttonClick = False
        except:
            self.status_value.set('Lỗi!')

    def decd(self):
        file_name = self.set_name.get()
        check_photo = Path('./ciphertext/controller/isPhoto.txt')
        # try:
        if self.file_ciphertext.get() != '':
            if check_photo.is_file() == True:
                s.decode_photo(self.file_ciphertext.get(), file_name)
            else:
                s.dec(self.file_ciphertext.get(), file_name)
                self.status_value.set('Thành công!')
        else:
            self.status_value.set('Sai đường dẫn!')
        # except:
            # self.status_value.set('Lỗi!')

    def open_dec(self):
        file = self.set_name.get()
        if Path('./ciphertext/controller/isPhoto.txt').is_file() == True:
            Image.open(file + '.png').show()
        else:
            plan = open(file + '.txt', "r", encoding='utf-8')
            self.text_box_plan.insert('end', plan.read())
