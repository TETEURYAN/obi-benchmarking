
import sys

def main():
    data = sys.stdin.read().split()
    ptr = 0
    N = int(data[ptr])
    L = int(data[ptr+1])
    H = int(data[ptr+2])
    ptr += 3
    s = list(map(int, data[ptr:ptr+N]))
    ptr += N
    m = list(map(int, data[ptr:ptr+N]))

    prefix_sum = [0] * (N + 1)
    for i in range(1, N + 1):
        prefix_sum[i] = prefix_sum[i-1] + s[i-1]

    marked_positions = []
    for i in range(N):
        if m[i] == 1:
            marked_positions.append(i)

    K = len(marked_positions)
    if K < L:
        print(0)
        return

    max_sum = -float('inf')

    for i in range(K):
        left = marked_positions[i]
        for j in range(i + L - 1, min(i + H, K)):
            right = marked_positions[j]
            current_sum = prefix_sum[right + 1] - prefix_sum[left]
            if current_sum > max_sum:
                max_sum = current_sum

    if max_sum == -float('inf'):
        print(0)
    else:
        print(max_sum)

if __name__ == '__main__':
    main()
