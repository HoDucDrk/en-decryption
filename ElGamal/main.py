import script

i = 0
while True:
   print("1. sinh khoa\n2.ma hoa\n3.giai ma\n0.thoat")
   i = 0
   lc = int(input("Enter lc: "))
   if lc == 0: 
      break 
   elif (lc == 1 and i == 0):
      script.key_generation()
      i = 1
   elif lc == 2:
      script.enc()
   elif lc == 3: 
      script.dec()
