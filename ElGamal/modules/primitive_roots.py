from math import sqrt, gcd

def cyclic_group(p):
    cyclic_group = []
    for i in range(2, p):
        if gcd(p, i) == 1:
            cyclic_group.append(i)
    return cyclic_group

def primitive_roots(p):
   if p > 6000:
      p = int(sqrt(p)) * 2
   cyclic = cyclic_group(p)
   max_value = 0
   value = {}
   for i in cyclic:
      for j in range(2, p):
         if (pow(i, j, p) == 1):
            if(j >= max_value):
               value.update({i: j})
               max_value = j
            break
   root = []
   for key, value in value.items():
      if(value == max_value):
         root.append(key)
   return root

