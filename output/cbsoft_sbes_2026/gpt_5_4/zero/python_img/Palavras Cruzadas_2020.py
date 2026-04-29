h = input().strip()
v = input().strip()

pos_v = {}
for i, c in enumerate(v, 1):
    pos_v[c] = i

for i in range(len(h), 0, -1):
    c = h[i - 1]
    if c in pos_v:
        print(i, pos_v[c])
        break
else:
    print(-1, -1)