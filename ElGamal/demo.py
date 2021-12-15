from Alice import Alice
from Bob import Bob
from tkinter import * 
from tkinter import ttk

class MultiWindows():
   def __init__(self, master):
      self.master = master
      self.frame = ttk.Frame(master)
      self.alice_window_status = False
      self.bob_window_status = False
      frame = self.frame
      my_canvas = Canvas(frame, width=350, height=1, bg='black')
      frame.grid()
      button_alice = ttk.Button(frame, text='Decryption', command=self.alice_window)
      button_bob = ttk.Button(frame, text='Encryption', command=self.bob_window)
      button_clear = ttk.Button(frame, text='Quit', command=master.destroy)

      button_alice.grid(row=0, column=0)
      button_bob.grid(row=1, column=0)
      button_clear.grid(row=2, column=0)
      my_canvas.grid(row=3, column=0)

   def alice_window(self):
      if self.alice_window_status == False:
         self.alice_window_status = True
         Alice(self.frame)

   def bob_window(self):
      if self.bob_window_status == False:
         self.bob_window_status = True
         Bob(self.frame)
if __name__ == '__main__':
   root = Tk()
   root.title('Demo')
   demo = MultiWindows(root)
   root.mainloop()