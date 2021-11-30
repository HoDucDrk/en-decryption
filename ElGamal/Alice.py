from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter.filedialog import askopenfile
from tkinter import filedialog
import script as sp
from tkinter import ttk
from pathlib import Path
from PIL import Image
import os
import glob
import json

def send_key():
   global buttonClick
   if(buttonClick == False):
      buttonClick = not buttonClick
      open('./ciphertext/status.txt', 'w+')
      Label(frm ,text="Thành công!").grid(column=2, row=1)
   return buttonClick
   
buttonClick = False

def getFilePath():
   filetype = (
      ('text files', '*.txt'),
      ('All files', '*.*')
   )
   folder_selected = filedialog.askopenfilename(filetypes=filetype)
   file_Plaintext.set(folder_selected)

def open_crip():
   file = file_Plaintext.get()
   osCommandString = "notepad.exe " + file
   os.system(osCommandString)

def open_dec():
   file = k.get()
   print(file)
   if Path('./ciphertext/isPhoto.txt').is_file() == True:
      x = Image.open(file + '.png').show()
   else:
      osCommandString = "notepad.exe " + file
      os.system(osCommandString)

def decd():
   file_out = k.get()
   check_photo = Path('./ciphertext/isPhoto.txt')
   try:
      if file_Plaintext.get() != '':
         if check_photo.is_file() == True:
            sp.decode_photo(file_Plaintext.get(), file_out)
         else:
            sp.dec(file_Plaintext.get(), file_out)
         Label(frm, text="Thành công!", width=10).grid(column=3, row=10)
   except:
      Label(frm, text="Lỗi!", width=10).grid(column=3, row=10)

def save_key():
   sp.key_generation() 
   p = sp.__init__.toInt(json.loads(sp.open_file("./keys/public_key.txt")))
   Label(frm ,text="public key: ").grid(column=3, row=0)
   Label(frm ,text="p: " + str(p["q"]) + ", a: " + str(p["a"])).grid(column=4, row=0)

def remove_file():
   try:
      files = glob.glob("./ciphertext/*")
      files_key = glob.glob("./keys/*")
      for f in files: os.remove(f)
      for f in files_key: os.remove(f)
      Label(frm ,text="Thành công!").grid(column=3, row=10)
   except:
      print('')

a= Tk()

a.title("Alice")
file_Plaintext = StringVar()
a.minsize(500, 200)
frm = ttk.Frame(a, padding=5)
frm.grid()
   
Button(frm, text="sinh khoa", width = 20,command=save_key).grid(column=1, row=0)
Button(frm, text="Gửi khóa công khai", width=20, command=send_key).grid(column=2, row=0)
Label(frm ,text="Chọn bản mã").grid(column=1, row=2)
Button(frm, text="Văn bản", width=20, command=getFilePath).grid(column=2, row=2)
Entry(frm, textvariable=file_Plaintext).grid(column=2, row=3)
Button(frm, text="Mở bản mã", width=20, command=open_crip).grid(column=1, row=3)
Label(frm, text="Đặt têm file: ", width=20).grid(column=1, row=4)
k = Entry(frm)
k.insert(10, "banro")
k.grid(column=2, row=4)
Button(frm, text="Giải mã", width=20, command=decd).grid(column=1, row=5)
Button(frm, text="Mở bản rõ", width=20, command=open_dec).grid(column=2, row=5)
Button(frm, text="Xóa file", width=20, command=remove_file).grid(column=1, row=6)
Button(frm, text="Quit", width = 20, command=a.destroy).grid(column=1, row=7)
Label(frm ,text="Status: ").grid(column=2, row=10)
a.mainloop()