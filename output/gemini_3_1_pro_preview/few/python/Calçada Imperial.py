import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

n = int(input_data[0])
v = [int(x) for x in input_data[1:n+1]]

if n <= 1:
    print(n)
    exit()

pos = {}
for i, x in enumerate(v):
    if x not in pos:
        pos[x] = []
    pos[x].append(i)

unique_elements = list(pos.keys())
if len(unique_elements) == 1:
    print(1)
    exit()

max_len = 1
len_unique = len(unique_elements)

for i in range(len_unique):
    a = unique_elements[i]
    pos_a = pos[a]
    len_a = len(pos_a)
    for j in range(i + 1, len_unique):
        b = unique_elements[j]
        pos_b = pos[b]
        len_b = len(pos_b)
        
        idx_a = 0
        idx_b = 0
        count = 0
        last_was_a = None
        
        while idx_a < len_a or idx_b < len_b:
            if idx_a < len_a and (idx_b == len_b or pos_a[idx_a] < pos_b[idx_b]):
                if last_was_a is not True:
                    count += 1
                    last_was_a = True
                idx_a += 1
            else:
                if last_was_a is not False:
                    count += 1
                    last_was_a = False
                idx_b += 1
                
        if count > max_len:
            max_len = count

print(max_len)