import sys

data = sys.stdin.read().split()
N = int(data[0])
strings = data[1:1 + N]
substrings = set()
for k in range(N):
    s = strings[k]
    if k >= 1:
        if s in substrings:
            print(s)
            sys.exit(0)
    for i in range(k):
        concat1 = strings[i] + s
        for j in range(11):
            substrings.add(concat1[j:j + 10])
        concat2 = s + strings[i]
        for j in range(11):
            substrings.add(concat2[j:j + 10])
print("ok")