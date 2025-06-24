n = 7
# for i in range(1, n+1):
#     for j in range(1,n+1):
#         if (i==1 and j not in (1,n)) or (j == 1 and i!=1) or (i == (n+1)//2) or (j==n and i != 1):
#             print('*',end=' ')
#         else:
#             print(' ', end = ' ')
#     print()

for i in range(1, n+1):
    for j in range(1,n+1):
        if (i==1 and j not in (1,n)) or (i<n//2+1 and i>1 and j==1) or (i==(n//2)+1 and j not in (1,n)) and (j==n and i>):
            print('*',end=' ')
        else:
            print(' ', end = ' ')
    print()