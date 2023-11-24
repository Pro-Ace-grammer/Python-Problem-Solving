
def pat(n):
    c = 'A'
    for i in range(0,n):
        for j in range(0,i+1):
            if c == 'Z':
                print(f'{c} ',end='')
                c = 'A'
            else:
                print(f'{c} ',end = '')
                c = chr(ord(c)+1)
        print()
pat(int(input('n: ')))
                
