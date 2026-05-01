
h = input().strip()
v = input().strip()

best_h = -1
best_v = -1
max_h_idx = -1
max_v_idx = -1

for i in range(len(h)):
    for j in range(len(v)):
        if h[i] == v[j]:
            if i > max_h_idx or (i == max_h_idx and j > max_v_idx):
                max_h_idx = i
                max_v_idx = j
                best_h = i + 1
                best_v = j + 1

if best_h == -1:
    print(-1, -1)
else:
    print(best_h, best_v)
