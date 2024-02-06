def createStack():
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

print(str(peek(stack)) + " is the Top most item :}")

