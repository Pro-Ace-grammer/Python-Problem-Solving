def maxScore(s: str) -> int:
    mx = -1
    for i in range(1,len(s)):
        left = s[:i]
        print(left)
        right = s[i:]
        print(right)
        sum_ = left.count('0')+right.count('1')
        if mx<sum_:
            mx = sum_
    print(mx)

maxScore('1111')