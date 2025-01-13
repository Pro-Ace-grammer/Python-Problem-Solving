'''
WAP to covert any number into words
'''

num = int(input('Enter a number: '))

ones = ['zero','one','two','three','four','five','six','seven','eight','nine']
ten = ['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
tens = ['','','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninty']

364

if 0<=num<=9:
    print(ones[num])
elif 9<num<100:
    if str(num)[0]=='1':
        print(ten[num%10])
    elif num>=20:
        r = num%10
        print(tens[num//10]+' '+ones[r])
elif 100<=num<=999:
    print(ones[num//100]+' '+'Hundred',end=' and ')
    num = int(str(num)[1:])
    if str(num)[0]=='1':
        print(ten[num%10])
    elif num>=20:
        r = num%10
        print(tens[num//10]+' '+ones[r])
