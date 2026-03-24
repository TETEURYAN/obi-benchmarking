import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

n = int(input_data[0])
digits = "".join(input_data[1:])

for L in range(1, n + 1):
    if digits[0] == '0':
        break
        
    A_str = digits[:L]
    A = int(A_str)
    
    X = A
    pos = 0
    valid = True
    
    while pos < n:
        X_str = str(X)
        length = len(X_str)
        
        if digits[pos:pos+length] == X_str:
            pos += length
            X += 1
        else:
            valid = False
            break
            
    if valid and pos == n:
        print(A)
        break