def facto(n):
    if n==1 or n==0:
        return 1
    else:
        return n * facto(n-1)
    
print(facto(5))