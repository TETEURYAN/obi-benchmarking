n, c, s = map(int, input().split())
commands = list(map(int, input().split()))

pos = 1
count = 0

for cmd in commands:
    pos = (pos - 1 + cmd) % n + 1
    if pos == s:
        count += 1

print(count)