import sys

data = list(map(int, sys.stdin.read().split()))
if not data:
    sys.exit()

n = data[0]
v = data[1:1 + n]

best = 1

for a in range(1, n + 1):
    for b in range(a, n + 1):
        if a == b:
            cnt = 0
            for x in v:
                if x == a:
                    cnt = 1
                    break
            if cnt > best:
                best = cnt
            continue

        dp_a = 0
        dp_b = 0
        for x in v:
            if x == a:
                if dp_b + 1 > dp_a:
                    dp_a = dp_b + 1
            elif x == b:
                if dp_a + 1 > dp_b:
                    dp_b = dp_a + 1

        cur = dp_a if dp_a > dp_b else dp_b
        if cur > best:
            best = cur

print(best)