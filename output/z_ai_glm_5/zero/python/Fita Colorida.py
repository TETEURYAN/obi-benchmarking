
import sys

def solve():
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        n = int(next(iterator))
    except StopIteration:
        return

    tape = []
    for _ in range(n):
        tape.append(int(next(iterator)))
    
    # Initialize distances with a large number (infinity)
    # N <= 10000, so N+1 is a safe upper bound
    distances = [n + 1] * n
    
    # Pass 1: Left to Right
    # Calculate distance to the nearest 0 to the left
    last_zero = -1
    for i in range(n):
        if tape[i] == 0:
            distances[i] = 0
            last_zero = i
        elif last_zero != -1:
            distances[i] = i - last_zero
            
    # Pass 2: Right to Left
    # Calculate distance to the nearest 0 to the right and take the minimum
    next_zero = -1
    for i in range(n - 1, -1, -1):
        if tape[i] == 0:
            next_zero = i
        elif next_zero != -1:
            dist = next_zero - i
            if dist < distances[i]:
                distances[i] = dist
    
    # Apply the cap of 9 and format output
    result = [str(min(d, 9)) for d in distances]
    print(" ".join(result))

if __name__ == '__main__':
    solve()
