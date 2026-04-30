from itertools import combinations

nums = list(map(int, input().split()))
total = sum(nums)

found = False
for combo in combinations(range(6), 3):
    s = sum(nums[i] for i in combo)
    if s * 2 == total:
        found = True
        break

print('S' if found else 'N')