import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

n = int(input_data[0])
f = int(input_data[1])
c = [int(x) for x in input_data[2:n+2]]

low = 1
high = 10**18
ans = high

while low <= high:
    mid = (low + high) // 2
    
    coins = 0
    for cycle in c:
        coins += mid // cycle
        if coins >= f:
            break
            
    if coins >= f:
        ans = mid
        high = mid - 1
    else:
        low = mid + 1
        
print(ans)