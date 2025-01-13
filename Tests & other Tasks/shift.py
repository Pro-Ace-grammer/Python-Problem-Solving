'''
shift
'''

def shift(s,goal):
    for i in range(len(s)):
        s = s[1:]+s[0]
        if s == goal:
            return True
    return False

print(shift(input('Str: '),input('goal: ')))
