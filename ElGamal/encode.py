from tkinter import *
from tkinter.filedialog import askopenfilename, askdirectory
from tkinter import filedialog
import script as s
from tkinter import ttk
from pathlib import Path
from PIL import Image, ImageTk
import os
import json

class encode():
   def __init__(self, master):
      self.master = master
      frame = ttk.Frame(master)
      self.frame = frame
      frame.grid()
      my_canvas = Canvas(frame, width=500, height=1, bg='black')
      self.selection_photo = False
      self.file_path = StringVar()
      self.folder_path = StringVar()
      self.file_path.set('')
      self.public_key = ''
      self.status_encryp = False
      #title
      ttk.Label(frame, text='Encryption', foreground='red').grid(row=0, column=0)

      #Button
      get_key = ttk.Button(frame, text='Nhận khóa', command=self.private_key)
      select_text = ttk.Button(frame, text='Văn bản', command=lambda: self.get_file_path(''))
      select_photo = ttk.Button(frame, text='Ảnh', command=lambda: self.get_file_path('photo'))
      open_file = ttk.Button(frame, text='Open file', command=self.open_file)
      encode = ttk.Button(frame, text='Mã hóa', command=self.encd)
      open_ciphertext = ttk.Button(frame, text='Open file', command=self.open_crip)
      clear_window = ttk.Button(frame, text='Clear', command=self.clear)
      select_path = ttk.Button(frame, text="Select path", command=self.select_folder_path)

      #Label Configure
      self.key_value = StringVar()
      self.key_value.set('')
      self.status_value = StringVar()
      self.status_value.set('')

      #Label
      display_key_value = ttk.Label(frame, textvariable=self.key_value)
      ttk.Label(frame, text="Chọn").grid(row=2, column=0)
      ttk.Label(frame, text="Path").grid(row=3, column=0)
      label_rename = ttk.Label(frame, text='Đặt tên')
      status = ttk.Label(frame, text='Status: ')
      ttk.Label(frame, text="Bản rõ").grid(row=0, column=5)
      ttk.Label(frame, text=" ").grid(row=0, column=4)
      ttk.Label(frame, text="Bản mã").grid(row=0, column=10)
      display_status_value = ttk.Label(frame, textvariable=self.status_value)


      #Entry
      entry_path = ttk.Entry(frame, textvariable=self.file_path, width=27)
      self.entry_folder_path = ttk.Entry(frame, textvariable=self.folder_path)
      self.rename_file = ttk.Entry(frame, width=11)
      self.rename_file.insert(15, 'ma_hoa')

      #text box
      self.text_box_plan = Text(frame,  height=12, width=50)
      self.text_box_crip = Text(frame,  height=12, width=50)
      #Layout
      get_key.grid(row=1, column=0)
      display_key_value.grid(row=1, column=1, columnspan=2)
      select_text.grid(row=2, column=1)
      select_photo.grid(row=2, column=2)
      entry_path.grid(row=3, column=1, columnspan=2)
      open_file.grid(row=3, column=3)
      select_path.grid(row=4, column=0)
      self.entry_folder_path.grid(row=4, column=1, columnspan=2)
      label_rename.grid(row=4, column=3)
      self.rename_file.grid(row=4, column=4)
      self.text_box_plan.grid(row=1, column=5, columnspan=5, rowspan=5)
      self.text_box_crip.grid(row=1, column=10, columnspan=5, rowspan=5)
      encode.grid(row=5, column=0)
      open_ciphertext.grid(row=5, column=1)
      clear_window.grid(row=6, column=0)
      status.grid(row=10, column=0)
      display_status_value.grid(row=10, column=1, columnspan=2)
      my_canvas.grid(row=11, column=0, columnspan=11)

   def select_folder_path(self):
      self.folder_path.set(askdirectory())

   def private_key(self):
      buttonClick = Path('./ciphertext/controller/status.txt')
      if buttonClick.is_file() == False: 
         self.key_value.set('Thất bại!')
      elif buttonClick.is_file() == True :
         self.public_key = s.__init__.toInt(json.loads(s.open_file("./keys/public_key.txt")))
         self.key_value.set("p: " + str(self.public_key["q"]) + ", a: " + str(self.public_key["a"]) + ", y: " + str(self.public_key["y"]))
         
   def get_file_path(self, module):
      if module == 'photo':
         self.selection_photo = True
         filetype = (
            ('photo files', '*.png *jpg'),
            ('All files', '*.*')
         )
         file_selected = askopenfilename(filetypes=filetype)
      else:
         self.selection_photo = False
         filetype = (
            ('file files', '*.txt'),
            ('All files', '*.*')
         )
         file_selected = askopenfilename(filetypes=filetype)
      self.file_path.set(file_selected)

   def open_file(self):
      file = self.file_path.get()
      if self.selection_photo == True:
         img = Image.open(file)
         img.show()

   
      else:
         file = open(self.file_path.get(), "r", encoding='utf-8')
         self.text_box_plan.insert('end', file.read())

   def encd(self):
      if self.status_encryp == False:
         file_path = self.folder_path.get() + "/" + self.rename_file.get()
         if self.file_path.get() != '':
            try:
               if self.selection_photo == True:
                  s.enc(self.file_path.get(), file_path, self.public_key, 'p')
                  open('./ciphertext/controller/isPhoto.txt', 'w+')
               else:
                  s.enc(self.file_path.get(), file_path, self.public_key, '')
               self.status_value.set('Thành công!')
               self.status_encryp = True
            except:
               self.status_value.set('Lỗi! TryAgain!')
         else: 
            self.status_value.set('Thất bại!')
   
   def open_crip(self):
      file = open( self.folder_path.get() + "/" + self.rename_file.get() + ".txt", "r", encoding="utf-8")
      def character_limit(entry_text):
         if len(entry_text) > 0:
            entry_text = entry_text[:10000]
         return entry_text
      text = character_limit(file.read())
      self.text_box_crip.insert('end', text)
   
   def clear(self):
      self.key_value.set('')
      self.file_path.set('')
      self.status_value.set('')
      self.text_box_crip.delete('1.0', END)
      self.text_box_plan.delete('1.0', END)
      self.folder_path.set('')
      self.status_encryp = False
