import os
import __init__
import json
import base64
from io import BytesIO
from PIL import Image

open_file = __init__.open_file
file_writer = __init__.file_writer

def key_generation():
   var_keys = __init__.create_key(__init__.random_key_generation())
   __init__.keys(var_keys)

def enc(path, file_name, key, mode):
   if mode == 'p':
      msg = encode_photo(path)
   else:
      msg = open_file(path)
   __init__.encryption(msg, key, file_name)

def dec(file_name, out_file):
   public_key = open_file("./keys/public_key.txt")
   private_key = open_file("./keys/private_key.txt")
   public_key = __init__.toInt(json.loads(public_key))
   c1 = open("./ciphertext/controller/ciphertext.txt", "r").read()
   c2 = __init__.reconvert(__init__.ciphertext_file(file_name))
   en = int(c1), c2
   key = (public_key , int(private_key))
   print(key)
   __init__.decryption(en, key, out_file)

def encode_photo(path):
   with open(path, 'rb') as photo_file:
      encoded_photo = base64.b64encode(photo_file.read())
   return encoded_photo.decode('utf-8')

def decode_photo(path, file_name):
   dec(path, file_name)
   path_file = './' + file_name + '.txt'
   t = open(path_file, 'r').read()
   os.remove('./' + file_name + '.txt')
   x = t.encode('utf-8')
   im = Image.open(BytesIO(base64.b64decode(x)))
   im.save(file_name + '.png', 'PNG')