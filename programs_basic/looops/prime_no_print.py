'''
To print the Prime Numbers in the given Range
'''
start = int(input('Enter Start value: '))
end = int(input('Enter the End value'))

for i in range(start,end+1):
    if i in (1,0):
        continue
    for j in range (2,i):
        if i%j==0:
            break
    else:
        print(i)
