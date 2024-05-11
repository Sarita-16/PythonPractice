def evalRPN(tokens):
    stack = []
    operators = set(['+', '-', '*', '/'])

    for token in tokens:
        if token not in operators:
            stack.append(int(token))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if token == '+':
                stack.append(operand1 + operand2)
            elif token == '-':
                stack.append(operand1 - operand2)
            elif token == '*':
                stack.append(operand1 * operand2)
            elif token == '/':
                # Note: In Python 3, '/' operator always returns a float,
                # we use '//' operator for integer division.
                stack.append(int(operand1 / operand2))

    return stack.pop()

print("Enter the tokens : ")
#["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
tokens = list(map(str, input().split()))
print("Tokens : ", tokens)
print("Output of this expression : ", evalRPN(tokens))  # Output: 9
