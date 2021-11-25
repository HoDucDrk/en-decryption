from modules.create_key import create_key
from modules.prime import prime
from modules.prmordial_root import primordial_root
from modules.encryp import encrypt
from modules.decryp import decrypt

def convert_string_to_bytes(x):
   k = "".join(list(chr(i) for i in x))
   return k

def reconvert(x):
   k = list(ord(i) for i in x)
   return k

def file_writer(path, mode, x):
   file = open(path, mode)
   if type(x) == bytes:
      w = file.write(x)
   else:
      w = file.write(str(x))
   file.close()
   return file

def open_file(path):
   file = open(path)
   return file.read()

def toInt(dic):
   a = {}
   for key, value in dic.items():
      a.update({key: int(value)})
   return a
