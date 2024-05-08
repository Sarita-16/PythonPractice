def simplifyPath(path):
    components = path.split('/')

    stack = []

    for i in components:
        if i == '' or i == '.':
            continue
        elif i == '..':
            if stack:
                stack.pop()
        else:
            stack.append(i)

    simplified_path = '/' + '/'.join(stack)

    return simplified_path


print(simplifyPath("/home/"))  # Output: "/home"
print(simplifyPath("/home//foo/"))  # Output: "/home/foo"
print(simplifyPath("/home/user/Documents/../Pictures"))  # Output: "/home/user/Pictures"
