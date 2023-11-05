a = 'abcd'
b = 'efgh'
op = ''
i=0
j = len(b)-1
while i< len(a):
    op = op + a[i] + b[j]
    i+=1
    j-=1
print(op)
