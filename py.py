import codecs, base64

def rot13(text): return codecs.encode(text, 'rot13')
def base64_enc(text): return base64.b64encode(text.encode()).decode()
def base64_dec(text): return base64.b64decode(text).decode()

op = input("1. ROT13, 2. Base64, 3. Exit\n")
txt = input("Texto: ")

if op == "1":print(f"ROT13: {rot13(txt)}")
elif op == "2":print(f"Base64: {base64_enc(txt)}")
