
import sys

input = sys.stdin.read
data = input().split()

index = 0
test_num = 1

while True:
    N = int(data[index])
    index += 1
    if N == 0:
        break
    
    possible = [set('0123456789') for _ in range(6)]
    
    for _ in range(N):
        digits = data[index:index+10]
        letters = data[index+10:index+16]
        index += 16
        
        mapping = {}
        for let_idx, let in enumerate(letters):
            d1 = digits[let_idx*2]
            d2 = digits[let_idx*2 + 1]
            mapping[let] = (d1, d2)
        
        for pos in range(6):
            let = letters[pos]
            d1, d2 = mapping[let]
            possible[pos] &= {d1, d2}
    
    password = []
    for s in possible:
        assert len(s) == 1
        password.append(next(iter(s)))
    
    print(f"Teste {test_num}")
    print(' '.join(password))
    print()
    test_num += 1
