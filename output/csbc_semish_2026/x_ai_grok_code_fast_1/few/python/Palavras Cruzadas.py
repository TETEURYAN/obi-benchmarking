import sys

input_data = sys.stdin.read().split()
hor = input_data[0]
ver = input_data[1]

pos_hor = [[] for _ in range(26)]
pos_ver = [[] for _ in range(26)]

for i in range(len(hor)):
    c = ord(hor[i]) - ord('A')
    pos_hor[c].append(i + 1)

for i in range(len(ver)):
    c = ord(ver[i]) - ord('A')
    pos_ver[c].append(i + 1)

best_hor = -1
best_ver = -1
max_hor_pos = -1

for c in range(26):
    if pos_hor[c] and pos_ver[c]:
        curr_max_hor = max(pos_hor[c])
        curr_max_ver = max(pos_ver[c])
        if curr_max_hor > max_hor_pos:
            max_hor_pos = curr_max_hor
            best_hor = curr_max_hor
            best_ver = curr_max_ver
        elif curr_max_hor == max_hor_pos:
            if curr_max_ver > best_ver:
                best_ver = curr_max_ver

print(best_hor, best_ver)