import random 

def encrypt(msg, key):
   msg = list(ord(i) for i in msg)
   k = random.randint(1, key["q"] //2)
   k1 = pow(key["y"], k, key["q"])
   c1 = pow(key["a"], k, key["q"])
   c2 = list(k1 * i % key["q"] for i in msg)
   return c1, c2