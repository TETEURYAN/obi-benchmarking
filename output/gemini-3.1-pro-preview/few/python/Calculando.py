import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

idx = 0
test_case = 1
while idx < len(input_data):
    m = int(input_data[idx])
    if m == 0:
        break
    
    expr = input_data[idx+1]
    
    res = 0
    current_num = 0
    sign = 1
    for char in expr:
        if char == '+':
            res += sign * current_num
            current_num = 0
            sign = 1
        elif char == '-':
            res += sign * current_num
            current_num = 0
            sign = -1
        else:
            current_num = current_num * 10 + int(char)
    res += sign * current_num
    
    print(f"Teste {test_case}")
    print(res)
    print()
    
    test_case += 1
    idx += 2