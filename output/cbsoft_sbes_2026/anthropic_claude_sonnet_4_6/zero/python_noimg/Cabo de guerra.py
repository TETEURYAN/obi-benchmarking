from itertools import combinations

nums = list(map(int, input().split()))
total = sum(nums)

if total % 2 != 0:
    print('N')
else:
    half = total // 2
    found = False
    for combo in combinations(nums, 3):
        if sum(combo) == half:
            found = True
            break
    print('S' if found else 'N')