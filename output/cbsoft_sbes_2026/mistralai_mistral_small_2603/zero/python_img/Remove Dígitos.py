from collections import deque

def min_rounds_to_zero(n):
    visited = set()
    queue = deque()
    queue.append((n, 0))
    visited.add(n)

    while queue:
        current, steps = queue.popleft()

        if current == 0:
            return steps

        num_str = str(current)
        for digit in num_str:
            d = int(digit)
            if d != 0:
                next_num = current - d
                if next_num not in visited and next_num >= 0:
                    visited.add(next_num)
                    queue.append((next_num, steps + 1))

    return -1

n = int(input())
print(min_rounds_to_zero(n))