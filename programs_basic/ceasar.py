st = input()
enc = ''

for i in st:
    if 'A'<=i<='Z':
        if 'X'<=i<='Z':
            enc += chr((ord(i)-26)+3)
        else:
            enc += chr(ord(i)+3)
    elif 'a'<=i<='z':
        if 'x'<=i<='z':
            enc += chr((ord(i)-26)+3)
        else:
            enc += chr(ord(i)+3)
    else:
        enc+=i


print(enc)