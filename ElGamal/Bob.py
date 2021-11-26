from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter.filedialog import askopenfile
from tkinter import filedialog
import script as sp
from tkinter import ttk
from pathlib import Path
import os
import json

public_key = ''

def getFilePath():
   filetype = (
      ('text files', '*.txt'),
      ('All files', '*.*')
   )
   file_selected = filedialog.askopenfilename(filetypes=filetype)
   filePath.set(file_selected)

def setFilePath():
   file = filePath.get()
   osCommandString = "notepad.exe " + file
   os.system(osCommandString)

def take_file_name():
   print(t.get())

def encd():
   if filePath.get() != '':
      try:
         sp.enc(filePath.get(), t.get(), public_key)
         Label(frm1, text="Thành công!", width=10).grid(column=3, row=10)
      except:
         Label(frm1, text="Lỗi!", width=10).grid(column=3, row=10)
   else: 
      Label(frm1, text="Thất bại!", width=10).grid(column=3, row=10)

def open_crip():
   file = "./ciphertext/" + t.get() + ".txt"
   osCommandString = "notepad.exe " + file
   os.system(osCommandString)

def private_key():
   global public_key
   buttonClick = Path('./ciphertext/status.txt')
   if buttonClick.is_file() == False: 
      Label(frm1, text="Thất bại!").grid(column=2, row=0)
   elif buttonClick.is_file() == True :
      public_key = sp.__init__.toInt(json.loads(sp.open_file("./keys/public_key.txt")))
      Label(frm1,text="Thanh cong!" ).grid(column=2, row=0)       
      Label(frm1,text="p: " + str(public_key["q"]) + ", a: " + str(public_key["a"]) + ", y: " + str(public_key["y"])).grid(column=3, row=0)       

buttonClick = True

from tkinter import filedialog
import os
b = Tk()
b.title("Bob")
frm1 = ttk.Frame(b, padding=10)
frm1.grid()
filePath = StringVar()

b.minsize(500, 200)
Button(frm1, text="nhận khóa",width=10, command=private_key).grid(column=1, row=0)
Entry(frm1, textvariable=filePath).grid(column=2, row=1)
Button(frm1, text="Nhập bản gốc",width=10, command=getFilePath).grid(column=1, row=1)
Button(frm1, text="Open file",width=10, command=setFilePath).grid(column=1, row=2)
t = ttk.Entry(frm1)
t.insert(10, "mahoa")
t.grid(column=2, row=3)
Button(frm1, text="Đặt tên", width=10, command=take_file_name).grid(column=1, row=3)
Button(frm1, text="Mã hóa", width=10, command=encd).grid(column=1, row=4)
Button(frm1, text="Mở file mã hóa", width=10, command=open_crip).grid(column=2, row=4)
Button(frm1, text="Đóng",width=10, command=b.destroy).grid(column=1, row=5)
Label(frm1, text="Status: ").grid(column=2, row=10)

b.mainloop()