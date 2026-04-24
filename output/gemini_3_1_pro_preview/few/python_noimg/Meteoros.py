import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

idx = 0
teste = 1
while idx < len(input_data):
    x1 = int(input_data[idx])
    y1 = int(input_data[idx+1])
    x2 = int(input_data[idx+2])
    y2 = int(input_data[idx+3])
    idx += 4
    
    if x1 == 0 and y1 == 0 and x2 == 0 and y2 == 0:
        break
        
    n = int(input_data[idx])
    idx += 1
    
    count = 0
    for _ in range(n):
        x = int(input_data[idx])
        y = int(input_data[idx+1])
        idx += 2
        
        if x1 <= x <= x2 and y2 <= y <= y1:
            count += 1
            
    print(f"Teste {teste}")
    print(count)
    print()
    
    teste += 1