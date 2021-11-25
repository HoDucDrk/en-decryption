import random
def create_key(values):
   q, a = values
   x = random.randint(1, q - 1)
   return {
      "q": q, 
      "a": a, 
      "y": pow(a, x, q)
   }, x