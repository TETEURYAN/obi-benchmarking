
import sys
from bisect import bisect_left

def main():
    data = sys.stdin.read().split()
    ptr = 0
    N = int(data[ptr])
    ptr += 1
    heights = list(map(int, data[ptr:ptr+N]))
    ptr += N
    Q = int(data[ptr])
    ptr += 1

    operations = []
    for _ in range(Q):
        T = int(data[ptr])
        I = int(data[ptr+1])
        X = int(data[ptr+2])
        operations.append((T, I, X))
        ptr += 3

    # Process operations
    output = []
    for op in operations:
        T, I, X = op
        if T == 0:
            heights.insert(I, X)
        else:
            D = X
            target_pos = I - 1
            target_height = heights[target_pos]
            threshold = target_height + D
            # Find the first position j < target_pos where heights[j] > threshold
            # Since heights is a list, we can scan from left to right up to target_pos
            found_pos = 0
            for j in range(target_pos):
                if heights[j] > threshold:
                    found_pos = j + 1
                    break
            output.append(str(found_pos))

    print('\n'.join(output))

if __name__ == "__main__":
    main()
