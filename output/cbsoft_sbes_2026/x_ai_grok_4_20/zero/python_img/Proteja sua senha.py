
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
        mapping = {}
        for let in 'ABCDE':
            d1 = data[index]
            d2 = data[index + 1]
            mapping[let] = (d1, d2)
            index += 2
        seq = data[index:index + 6]
        index += 6
        for pos in range(6):
            let = seq[pos]
            d1, d2 = mapping[let]
            possible[pos] &= {d1, d2}
    
    password = []
    for s in possible:
        password.append(s.pop())
    
    print(f"Teste {test_num}")
    print(' '.join(password))
    print()
    test_num += 1
