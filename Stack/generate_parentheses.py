"""
Drill recursion problems.
"""

def generate_parentheses(n: int) -> list:
    stack = []
    valid = []

    def backtrack(open_n, closed_n):
        if open_n == closed_n == n:
            valid.append("".join(stack))
            return

        if open_n < n:
            stack.append('(')
            backtrack(open_n + 1, closed_n)
            stack.pop()

        if closed_n < open_n:
            stack.append(')')
            backtrack(open_n, closed_n + 1)
            stack.pop()

    backtrack(0, 0)
    return valid