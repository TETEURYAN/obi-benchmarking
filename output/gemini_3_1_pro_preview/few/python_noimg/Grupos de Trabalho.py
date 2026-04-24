import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

E = int(input_data[0])
M = int(input_data[1])
D = int(input_data[2])

idx = 3

same_group_reqs = []
for _ in range(M):
    same_group_reqs.append((int(input_data[idx]), int(input_data[idx+1])))
    idx += 2
    
diff_group_reqs = []
for _ in range(D):
    diff_group_reqs.append((int(input_data[idx]), int(input_data[idx+1])))
    idx += 2
    
group_of = [0] * (E + 1)

num_groups = E // 3
for g in range(1, num_groups + 1):
    group_of[int(input_data[idx])] = g
    group_of[int(input_data[idx+1])] = g
    group_of[int(input_data[idx+2])] = g
    idx += 3
    
violations = 0

for u, v in same_group_reqs:
    if group_of[u] != group_of[v]:
        violations += 1
        
for u, v in diff_group_reqs:
    if group_of[u] == group_of[v]:
        violations += 1
        
print(violations)