
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return

    ptr = 0
    N = int(data[ptr])
    ptr += 1
    M = int(data[ptr])
    ptr += 1

    weights = list(map(int, data[ptr:ptr+N]))
    ptr += N

    # Segment Tree to track min and max in each segment
    size = 1
    while size < N:
        size <<= 1
    seg_min = [float('inf')] * (2 * size)
    seg_max = [float('-inf')] * (2 * size)

    for i in range(N):
        seg_min[size + i] = weights[i]
        seg_max[size + i] = weights[i]

    for i in range(size - 1, 0, -1):
        seg_min[i] = min(seg_min[2 * i], seg_min[2 * i + 1])
        seg_max[i] = max(seg_max[2 * i], seg_max[2 * i + 1])

    def update(pos, value):
        pos += size
        seg_min[pos] = value
        seg_max[pos] = value
        pos >>= 1
        while pos >= 1:
            new_min = min(seg_min[2 * pos], seg_min[2 * pos + 1])
            new_max = max(seg_max[2 * pos], seg_max[2 * pos + 1])
            if seg_min[pos] == new_min and seg_max[pos] == new_max:
                break
            seg_min[pos] = new_min
            seg_max[pos] = new_max
            pos >>= 1

    def query_min(l, r):
        res = float('inf')
        l += size
        r += size
        while l <= r:
            if l % 2 == 1:
                res = min(res, seg_min[l])
                l += 1
            if r % 2 == 0:
                res = min(res, seg_min[r])
                r -= 1
            l >>= 1
            r >>= 1
        return res

    def query_max(l, r):
        res = float('-inf')
        l += size
        r += size
        while l <= r:
            if l % 2 == 1:
                res = max(res, seg_max[l])
                l += 1
            if r % 2 == 0:
                res = max(res, seg_max[r])
                r -= 1
            l >>= 1
            r >>= 1
        return res

    output = []
    for _ in range(M):
        op = int(data[ptr])
        ptr += 1
        if op == 1:
            p = int(data[ptr])
            ptr += 1
            i = int(data[ptr]) - 1
            ptr += 1
            weights[i] = p
            update(i, p)
        else:
            a = int(data[ptr]) - 1
            ptr += 1
            b = int(data[ptr]) - 1
            ptr += 1
            min_val = query_min(a, b)
            max_val = query_max(a, b)
            output.append(str(max_val - min_val))

    print('\n'.join(output))

if __name__ == "__main__":
    main()
