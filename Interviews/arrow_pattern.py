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

'''
                                    e 
                                    e e 
                * * * * * o o o o o e e e 
                * * * * *           e e 
    e           * * * * *           e 
  e e           * * * * * 
e e e o o o o o * * * * * 
  e e           
    e     

    
'''


n=int(input("Enter a number: "))
n = n if n%2!=0 else n+1
spl=n//2
spr=0
rows = n*2
mid = (n//2)+1
up_mid = (n//2)+n

for i in range(1,rows):
    if(i<n):
        if(i<mid):
            print('  '*(n*2+mid), end='')
        else:
            print('  '*(n+mid),end='')

        # for j in range(1,((n//2)+n)+2):
        #     print("+ ",end='')
    if(i>=n and i<=up_mid):
        print("  "*spl,end='')
        print("e "*((mid-spl)),end='')
        spl-=1

        if(i==up_mid):
            print('o '*n,end='')
            spl = 1
        else:
            print('  '*n,end='')
    
    if(i>(n//2)+n):
        print("  "*spl,end='')
        print("e "*((mid-spl)),end='')
        spl += 1
    


    if(i>=mid and i<=up_mid):
        print('c '*n, end='')
    else:
        print('  '*n, end='')

    if(i>=mid and i<=n):
        if(i==mid):
            print("o "*n,end='')
        else:
            print("  "*n,end='')
        print("e "*(mid-spr),end='')
        spr+=1

    if i<mid:
        print('e '*i,end='')

    print()