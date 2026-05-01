import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

N = int(input_data[0])
M = int(input_data[1])

A = set(int(x) for x in input_data[2:2+N])
B = [int(x) for x in input_data[2+N:2+N+M]]

set_B = set()
list_B_unique = []

for b in B:
    if b in set_B:
        continue
        
    if b in A:
        set_B.add(b)
        list_B_unique.append(b)
        continue
        
    valid = False
    for x in list_B_unique:
        if (b - x) in set_B:
            valid = True
            break
            
    if valid:
        set_B.add(b)
        list_B_unique.append(b)
    else:
        print(b)
        exit()
        
print("sim")