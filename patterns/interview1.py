# n = int(input())
# r_arr =1

# for j in range(1,n):
#     print('  '*(n*4),end='')
#     print('* '*r_arr)
#     r_arr+=1
# r_arr = n
# for i in range(1,n+1):
#     print('  '*(n-i),end='')
#     print('* '*i,end='')
#     if i == n:
#         print('e '*n,end='')
#     else:
#         print('  '*n,end='')

#     print('* '*n,end='')
#     if i == 1:
#         print('e '*n,end='')
#     else:
#         print('  '*n,end='')
#     print('* '*r_arr)
#     r_arr-=1

# for i in range(1,n):
#     print('  '*i,end='')
#     print('* '*(n-i))



n=3
sp=n//2
rows = n*2
mid = (n//2)+1

for i in range(1,rows):
    if(i<n):
        if(i<mid):
            print('- '*(n*2+mid), end='')
        else:
            print('- '*(n+mid),end='')
        

        # for j in range(1,((n//2)+n)+2):
        #     print("+ ",end='')
    if(i>=n and i<=((n//2))+n):
        print("- "*sp,end='')
        print("e "*((mid-sp)),end='')
        sp-=1

        if(i==((n//2))+n):
            print('o '*n,end='')
        else:
            print('- '*n,end='')
        

    if(i>=(n//2)+1 and i<=((n//2))+n):
        print((str(i)+" ")*n, end='')
    else:
        print('- '*n, end='')

    if(i==(n//2)+1):
        print("o "*n,end='')
    print()