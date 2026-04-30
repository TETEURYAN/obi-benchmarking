
import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])
M = int(data[1])
queries = data[2:]

ft = [0] * (N + 2)
diff = [0] * (N + 2)

idx = 0
output = []

for _ in range(M):
    tp = int(queries[idx])
    idx += 1
    if tp == 3:
        i = int(queries[idx])
        idx += 1
        val = 0
        pos = i
        while pos > 0:
            val += ft[pos]
            pos -= pos & -pos
        val += (i * diff[0])
        pos = i
        while pos > 0:
            val += diff[pos] * (i - pos + 1)
            pos -= pos & -pos
        output.append(str(val))
    else:
        i = int(queries[idx])
        idx += 1
        v = int(queries[idx])
        idx += 1
        if tp == 1:
            r = min(N, i + v - 1)
            l = i
            k = v
            # add to ft: +k at l, -k at r+1
            pos = l
            while pos <= N:
                ft[pos] += k
                pos += pos & -pos
            if r + 1 <= N:
                pos = r + 1
                while pos <= N:
                    ft[pos] -= k
                    pos += pos & -pos
            # add to diff: -1 at l, +1 at r+1
            pos = l
            while pos <= N:
                diff[pos] -= 1
                pos += pos & -pos
            if r + 1 <= N:
                pos = r + 1
                while pos <= N:
                    diff[pos] += 1
                    pos += pos & -pos
            # constant part for diff
            diff[0] += (k - l + 1)
            if r + 1 <= N:
                diff[0] -= (k - (r - l + 1) - l + 1)
        else:
            r = max(1, i - v + 1)
            l = i
            k = v
            len_seg = l - r + 1
            # ft part: +k at r, -k at l+1
            pos = r
            while pos <= N:
                ft[pos] += k
                pos += pos & -pos
            if l + 1 <= N:
                pos = l + 1
                while pos <= N:
                    ft[pos] -= k
                    pos += pos & -pos
            # diff part: +1 at r, -1 at l+1
            pos = r
            while pos <= N:
                diff[pos] += 1
                pos += pos & -pos
            if l + 1 <= N:
                pos = l + 1
                while pos <= N:
                    diff[pos] -= 1
                    pos += pos & -pos
            # constant part
            diff[0] += (k - len_seg + 1)
            if l + 1 <= N:
                diff[0] -= (k - len_seg - len_seg + 1)

print('\n'.join(output))
