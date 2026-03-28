import sys

input_data = sys.stdin.read().split()
if not input_data:
    sys.exit()

idx = 0
t = 1
while idx < len(input_data):
    a = int(input_data[idx])
    v = int(input_data[idx+1])
    idx += 2
    
    if a == 0 and v == 0:
        break
        
    counts = [0] * (a + 1)
    for _ in range(v):
        x = int(input_data[idx])
        y = int(input_data[idx+1])
        counts[x] += 1
        counts[y] += 1
        idx += 2
        
    max_count = max(counts[1:])
    best_airports = [str(i) for i in range(1, a + 1) if counts[i] == max_count]
    
    print(f"Teste {t}")
    print(" ".join(best_airports))
    print()
    
    t += 1