def isValid(s):
    stack = []
    mapping = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    for i in s:
        if i in mapping.values():
            stack.append(i)
        elif i in mapping.keys():
            if not stack or mapping[i] != stack.pop():
                return False
        else:
            return False
    return not stack

s = input("Enter string : ")
result = isValid(s)
print(result)
