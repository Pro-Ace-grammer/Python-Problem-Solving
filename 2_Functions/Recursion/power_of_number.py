# Example 4: Power of number
def power(n,pow):
    if pow == 0:
        return 1
    else:
        return n*power(n,pow-1)
    
print(pow(3,4))

