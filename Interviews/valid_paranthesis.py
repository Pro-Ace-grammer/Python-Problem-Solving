'''
{{[{}{}()((({})))]}}
'''
# Program to check valid paranthesis.
pairs = {'}':'{', ')':'(', ']':'['} # Dictionary of paranthesis pairs

def isValidParanth(st):
    stack = []
    for ch in st:
        if ch in list(pairs.values()):
            stack.append(ch)
        elif ch in pairs:
            if stack[-1] == pairs[ch]:
                stack.pop()
            else:
                return False
    else:
        return True

print(isValidParanth('[{]}'))
