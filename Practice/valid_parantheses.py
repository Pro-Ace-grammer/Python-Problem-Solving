def valid_parantheses(st)->bool:
    hashmap = {"}":"{","]":"[",")":"("}
    stack = []
    for char in st:
        if char not in hashmap:
            stack.append(char)
        elif stack and stack[-1] == hashmap[char]:
            stack.pop()
        else:
            return False
    return True

st = "()[[{]}]"
print(valid_parantheses(st))