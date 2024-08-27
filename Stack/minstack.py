"""
Problem-solving was mostly good on my end, but I wasted a LOT of time
because I forgot the principles of stacks. Remember, top/peek = obtain the
last element in the stack, and pop = remove the last element in the stack.
"""

class MinStack:
    def __init__(self):
        self.bottom_val = float('inf')
        self.stack = []

        self.bottom_list = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if val <= self.bottom_val:
            self.bottom_val = val
            self.bottom_list.append(val)

    def pop(self) -> None:
        popped_elem = self.stack[-1]
        self.stack = self.stack[:-1]

        if popped_elem == self.bottom_val:
            self.bottom_list = self.bottom_list[:-1]
            self.bottom_val = self.bottom_list[-1] if self.bottom_list else float('inf')

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.bottom_val