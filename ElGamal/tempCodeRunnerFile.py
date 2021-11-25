var_keys = __init__.create_key(random_key_generation())
keys(var_keys)
msg = open_file("input.txt")
encryption(msg, var_keys[0])