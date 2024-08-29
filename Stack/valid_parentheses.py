"""
On my second read-through, I struggled a lot less; I was able to think through the concept of stacks a lot 
more efficiently. It took about ~15, which is not the best for an easy problem, but I do think my problem-solving
skills are improving somewhat. 
"""


def is_valid_first(s: str):
    """Incorrect solution."""
    
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














