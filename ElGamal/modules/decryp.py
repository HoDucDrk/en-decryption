def decrypt(en, keys):
   pu, pr = keys
   k = pow(en[0], pr, pu["q"])
   dec = list(i * pow(k, -1, pu["q"]) % pu["q"] for i in en[1])
   return "".join(chr(i) for i in dec)