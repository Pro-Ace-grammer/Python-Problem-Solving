# Example 8: Count Occurences of a Character in a string.
def occurance(st,ch,count=0):
    if not st:
        return count
    elif ch == st[0]:
        return occurance(st[1:],ch, count+1)
    return occurance(st[1:],ch,count)

#OR
def count_char(st,ch):
    if not st:
        return 0
    return (st[0]==ch) + count_char(st[1:],ch)

print(occurance('Hellllo', 'l'))
print(count_char('Hellllo', 'l'))