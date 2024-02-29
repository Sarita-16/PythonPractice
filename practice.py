'''def createStack():
    stack = []
    return stack


def isEmpty(stack):
    return len(stack) == 0


def push(stack, item):
    stack.append(item)
    print(item + " is pushed :) ")


def pop(stack):
    if isEmpty(stack):
        return "Stack is Underflow :( nothing "
    return stack.pop()


def peek(stack):
    if isEmpty(stack):
        return "Stack is Underflow :( So, nothing "
    return stack[len(stack)-1]


stack = createStack()

push(stack, str(10))
push(stack, str(20))

print(str(pop(stack)) + " is Popped :] ")
print(str(pop(stack)) + " is Popped :] ")
print(str(pop(stack)) + " is Popped :] ")
#print(str(pop(stack)) + " is Popped :] ")

print(str(peek(stack)) + " is the Top most item :}")        '''



'''
a, b = list(map(int, input(). split(" ")))

if a >= 1 and b >= 1 and a <= 100 and b <= 100:
    if a <= 10 and b >= 10:
        print("true", end=" ")
    else:
        print("false", end=" ")
    if a % 2 == 0 or b % 2 == 0:
        print("true", end=" ")
    else:
        print("false", end=" ")
    if a != b:
        print("true", end=" ")
    else:
        print("false", end=" ")     '''


'''
a = 2
b = 3
c = 4
d = 5
result = (a + b + c + d)/4
print(result)

# f to c
f  = int(input())
c = (f - 32) * (5/9)
print(c)        '''


a, b = list(map(int, input().split(" ")))

a = a + b
b = a - b
a = a - b

print(a, b)