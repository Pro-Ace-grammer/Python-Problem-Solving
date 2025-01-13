st = 'Pallavi'
lis = ['']
key = 3
enc=''

for i in range(len(st)):
    if (i+1)%key == 0:
        lis[-1]+=st[i]
        lis.append('\n')
        lis.append('')
    else:
        lis[-1] += st[i]

if len(lis[-1])<key:
    lis[-1] += '*'*(key - len(lis[-1]))
    

for i in range(key):
    for el in lis:
        if el != '\n' or el != '*':
            enc += el[i]
        else:
            continue

print(enc)