import sys

def median(lst):
    s = sorted(lst)
    n = len(s)
    return s[n // 2]

input_data = sys.stdin.read().split()
idx = 0
test_num = 0

while idx < len(input_data):
    S = int(input_data[idx]); idx += 1
    if S == 0:
        break
    test_num += 1
    xs = []
    ys = []
    for _ in range(S):
        x = int(input_data[idx]); idx += 1
        y = int(input_data[idx]); idx += 1
        xs.append(x)
        ys.append(y)
    
    mx = median(xs)
    my = median(ys)
    
    print(f"Teste {test_num}")
    print(f"{mx} {my}")
    print()