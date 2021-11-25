from math import sqrt
import random

def luyThua(q, a):
   for i in range(1, int(sqrt(q))):
      if(pow(a, i, q) == 1):
         return i

def find_number(q):
   arr = {}
   for key in range (1, q - 1):
      k = luyThua(q, key)
      if k != None:
         arr.update({key: k})
   return arr

def find_max(dict):
   arr = list(dict.values())
   return max(arr)

def primordial_root(dic):
   x = find_number(dic)
   root = []
   for key, value in x.items():
      if value == find_max(x):
         root.append(key)
   return root