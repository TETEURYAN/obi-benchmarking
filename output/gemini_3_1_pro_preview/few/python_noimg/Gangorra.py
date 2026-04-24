import sys

input_data = sys.stdin.read().split()
if input_data:
    p1, c1, p2, c2 = map(int, input_data[:4])
    left = p1 * c1
    right = p2 * c2
    
    if left == right:
        print(0)
    elif left > right:
        print(-1)
    else:
        print(1)