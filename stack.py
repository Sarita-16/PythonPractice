# This is used to return -infinite whenever our stack is empty
from sys import maxsize

# Create a Stack
def createStack():
    stack = []
    return stack


# Length of stack = 0 the stack is EMPTY
def isEmpty(stack):
    return len(stack) == 0


# Use Append to ADD item in stack
def push(stack, item):
    stack.append(item)
    print(item + " pushed to stack :) ")


# POP removes the topmost or last item in stack
def pop(stack):
    if isEmpty(stack):
        print("Stack Underflow :(")
        return str(-maxsize - 1)        # return minus infinite
    return stack.pop()


# PEEK
def peek(stack):
    if isEmpty(stack):
        return str(-maxsize - 1)        # return minus infinite
    return stack[len(stack) - 1]


# Driver Program
stack = createStack()

push(stack, str(5))
push(stack, str(10))
push(stack, str(15))

print(pop(stack) + " popped from stack :] ")

print(peek(stack) + " peeked from stack :} ")


