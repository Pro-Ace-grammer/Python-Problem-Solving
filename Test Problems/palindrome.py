
def palin(st):
    temp = ''
    a = ord('a')-ord('A')
    for i in st:
        if 'A'<=i<='Z':
            temp = chr(ord(i)+a)+temp
        else:
            temp = i + temp
    print(temp)
    if temp == temp[::-1]:
        return 'Palindrome'
    else:
        return 'Not Palindrome'

print(palin(input('str: ')))
