def __init__(self):
    self.d_struct = dict()


def set(self, key: str, value: str, timestamp: int) -> None:
    self.d_struct[key] = self.d_struct.get(key, [])
    self.d_struct[key].append((value, timestamp))


def get(self, key: str, timestamp: int) -> str:
    # {'alice': [("happy", 1)]}
    time_log = self.d_struct[key]

    if not time_log:
        return ""

    left, right = 0, len(time_log) - 1

    while left <= right:
        midpoint = (left + right) // 2

        if time_log[midpoint][1] == timestamp:
            return time_log[midpoint][0]

        elif left == right:
            return time_log[-1][0]

        elif time_log[midpoint][1] < timestamp:
            left = midpoint + 1

        elif time_log[midpoint][1] > timestamp:
            right = midpoint - 1