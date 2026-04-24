import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

weights = list(map(int, input_data))
total = sum(weights)

if total % 3 != 0:
    print('N')
else:
    target = total // 3
    if target not in weights:
        print('N')
    else:
        weights.remove(target)
        possible = False
        for i in range(len(weights)):
            for j in range(i + 1, len(weights)):
                if weights[i] + weights[j] == target:
                    possible = True
                    break
            if possible:
                break
        
        if possible:
            print('S')
        else:
            print('N')