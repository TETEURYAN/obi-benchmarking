
horizontal = input().strip()
vertical = input().strip()

best_h = -1
best_v = -1
max_h_pos = -1
max_v_pos = -1

for i in range(len(horizontal)):
    for j in range(len(vertical)):
        if horizontal[i] == vertical[j]:
            h_pos = i + 1
            v_pos = j + 1
            if h_pos > max_h_pos or (h_pos == max_h_pos and v_pos > max_v_pos):
                max_h_pos = h_pos
                max_v_pos = v_pos
                best_h = h_pos
                best_v = v_pos

if best_h == -1:
    print("-1 -1")
else:
    print(best_h, best_v)
