# Example 5: find the GCD / HCF
def gcd(a,b,divisor):
    if divisor == 1:
        return 1
    elif a%divisor==0 and b%divisor==0:
        return divisor
    else:
        return gcd(a,b,divisor-1)

a = int(input())
b = int(input())
divisor = a if a<b else b
print(gcd(a,b,divisor))

