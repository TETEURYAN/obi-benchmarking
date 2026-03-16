import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

n = int(input_data[0])
q = int(input_data[1])

pref = [0] * (n + 1)
for i in range(n):
    pref[i+1] = pref[i] + int(input_data[2+i])

out = []
idx = 2 + n
for _ in range(q):
    l = int(input_data[idx])
    r = int(input_data[idx+1])
    idx += 2
    
    k = r - l + 1
    s = pref[r] - pref[l-1]
    out.append(str(11 * (k - 1) * s))

print('\n'.join(out))