import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

idx = 0
test_case = 1

while idx < len(input_data):
    x = int(input_data[idx])
    y = int(input_data[idx+1])
    n = int(input_data[idx+2])
    idx += 3
    
    if x == 0 and y == 0 and n == 0:
        break
        
    items = []
    for _ in range(n):
        items.append(int(input_data[idx]))
        idx += 1
        
    total_chest = sum(items)
    total_sum = x + y + total_chest
    
    print(f"Teste {test_case}")
    test_case += 1
    
    if total_sum % 2 != 0:
        print("N\n")
        continue
        
    target = total_sum // 2
    needed_x = target - x
    needed_y = target - y
    
    if needed_x < 0 or needed_y < 0:
        print("N\n")
        continue
        
    dp = 1
    for item in items:
        dp |= (dp << item)
        
    if (dp >> needed_x) & 1:
        print("S\n")
    else:
        print("N\n")