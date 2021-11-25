import __init__
import random
import json

open_file = __init__.open_file
file_writer = __init__.file_writer

def random_key_generation():
   p = __init__.prime()
   a = __init__.primordial_root(p)
   return p, random.choice(a)

def ciphertext_file(path):
   file = open(path, "rb")
   return bytes(file.read()).decode("utf-8")
    
def keys(keys):
   key = str(keys[0]).replace('\'', '\"')
   file_writer("./keys/public_key.txt", "w+", key)
   file_writer("./keys/private_key.txt", "w+", keys[1])


def encryption(msg, public_key):
   en = __init__.encrypt(msg, public_key)
   file_name = input("Enter name file: ")
   file_writer("./ciphertext/" + file_name + ".txt", "wb+", __init__.convert_string_to_bytes(en[1]).encode("utf-8"))
   file_writer("./ciphertext/ciphertext.txt", "w+", str(en[0]))

def decryption(en, keys):
   dec = __init__.decrypt(en, keys)
   file_name = input("Enter name file: ")
   output = open(file_name + ".txt", "w+")
   output.write(dec)


def key_generation():
   var_keys = __init__.create_key(random_key_generation())
   keys(var_keys)

def enc():
   public_key = __init__.toInt(json.loads(open_file("./keys/public_key.txt")))
   msg = open_file("input.txt")
   print(public_key)
   encryption(msg, public_key)
# public_key, private_key = var_keys


def dec():
   public_key = open_file("./keys/public_key.txt")
   private_key = open_file("./keys/private_key.txt")
   public_key = __init__.toInt(json.loads(public_key))
   c1 = open("./ciphertext/ciphertext.txt", "r").read()
   c2 = __init__.reconvert(ciphertext_file("./ciphertext/test.txt"))
   en = int(c1), c2
   key = (public_key , int(private_key))
   print(key)
   decryption(en, key)

# enc()