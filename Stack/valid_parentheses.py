"""
I struggled with this one, partially because the concept of stacks
is pretty new me, but also because I seem to lack the vision that is
necessary to think solutions through. This is likely to improve the more
I grind.
"""


def is_valid_first(s: str):
    list_s = list(s)

    bracket_map = {"(": ")",
                   "[": "]",
                   "{": "}"}

    for bracket in list_s:
        last = list_s.pop()

        if bracket_map[bracket] != last:
            return False

    return True


def is_valid_second(s:str):

    close_to_open =  {')': '(',
                      ']': '[',
                      '}': '{'}
    stack = []

    for bracket in s:
        if bracket not in close_to_open:
            stack.append(bracket)
            continue

        if not stack or stack[-1] != close_to_open[bracket]:
            return False

        stack.pop()

    return True if not stack else False














