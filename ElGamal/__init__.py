from modules.create_key import create_key
from modules.prime import prime
from modules.prmordial_root import primordial_root
from modules.encryp import encrypt
from modules.decryp import decrypt
import random

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

def random_key_generation():
   p = prime()
   a = primordial_root(p)
   return p, random.choice(a)

def ciphertext_file(path):
   file = open(path, "rb")
   return bytes(file.read()).decode("utf-8")

def encryption(msg, public_key, file_name):
   en = encrypt(msg, public_key)
   file_writer("./ciphertext/" + file_name + ".txt", "wb+", convert_string_to_bytes(en[1]).encode("utf-8"))
   file_writer("./ciphertext/ciphertext.txt", "w+", str(en[0]))

def decryption(en, keys, file_name):
   dec = decrypt(en, keys)
   output = open(file_name + ".txt", "w+")
   output.write(dec)

def keys(keys):
   key = str(keys[0]).replace('\'', '\"')
   file_writer("./keys/public_key.txt", "w+", key)
   file_writer("./keys/private_key.txt", "w+", keys[1])