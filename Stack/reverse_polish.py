"""
Make sure to understand that stacks are usually initialized
as empty lists.
"""

def evalRPN(tokens: list) -> int:

    stack = []

    for token in tokens:
        if token == '+':
            stack.append(stack.pop() + stack.pop())
        elif token == '-':
            a, b = stack.pop(), stack.pop()
            stack.append(b - a)
        elif token == '*':
            stack.append(stack.pop() * stack.pop())
        elif token == '/':
            a, b = stack.pop(), stack.pop()
            stack.append(int(float(b) / a))
        else:
            stack.append(int(token))

    return stack[0]