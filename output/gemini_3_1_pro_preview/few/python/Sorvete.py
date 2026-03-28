import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

idx = 0
test_case = 1
while idx < len(input_data):
    P = int(input_data[idx])
    S = int(input_data[idx+1])
    idx += 2
    
    if P == 0 and S == 0:
        break
        
    intervals = []
    for _ in range(S):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        intervals.append([u, v])
        idx += 2
        
    intervals.sort(key=lambda x: (x[0], x[1]))
    
    merged = []
    for u, v in intervals:
        if not merged:
            merged.append([u, v])
        else:
            if u <= merged[-1][1]:
                if v > merged[-1][1]:
                    merged[-1][1] = v
            else:
                merged.append([u, v])
                
    print(f"Teste {test_case}")
    for u, v in merged:
        print(f"{u} {v}")
    print()
    
    test_case += 1