import sys

input_data = sys.stdin.read().split()
if len(input_data) >= 2:
    H = input_data[0]
    V = input_data[1]
    
    for i in range(len(H) - 1, -1, -1):
        j = V.rfind(H[i])
        if j != -1:
            print(f"{i + 1} {j + 1}")
            sys.exit()
            
    print("-1 -1")