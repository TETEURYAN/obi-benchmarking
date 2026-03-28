import sys

data = sys.stdin.read().split()
if not data:
    sys.exit()

n = int(data[0])
strings = data[1:1 + n]

prefix_count = {}
suffix_count = {}
full_count = {}

for s in strings:
    if full_count.get(s, 0) > 0:
        print(s)
        sys.exit()

    invalid = False

    for i in range(1, 10):
        if prefix_count.get(s[:i], 0) > 0 and suffix_count.get(s[i:], 0) > 0:
            invalid = True
            break

    if invalid:
        print(s)
        sys.exit()

    full_count[s] = full_count.get(s, 0) + 1

    for i in range(1, 10):
        p = s[:i]
        q = s[i:]
        prefix_count[p] = prefix_count.get(p, 0) + 1
        suffix_count[q] = suffix_count.get(q, 0) + 1

print("ok")