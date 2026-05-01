n = int(input())
digits = list(map(int, input().split()))

best = None

for i in range(n):
    for j in range(i+1, n):
        # swap i and j
        digits[i], digits[j] = digits[j], digits[i]
        # check if divisible by 5 (last digit is 0 or 5)
        # also check no leading zero (first digit != 0, unless n==1)
        if digits[-1] in (0, 5) and (n == 1 or digits[0] != 0):
            if best is None or digits > best:
                best = digits[:]
        digits[i], digits[j] = digits[j], digits[i]

if best is None:
    print(-1)
else:
    print(*best)