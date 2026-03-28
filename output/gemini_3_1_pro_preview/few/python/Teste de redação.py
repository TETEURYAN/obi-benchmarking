import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

n = int(input_data[0])
m = int(input_data[1])

words = []
for i in range(m):
    if i == 0:
        words.append("a")
    else:
        curr = i
        res = []
        while curr > 0:
            res.append(chr(97 + (curr % 26)))
            curr //= 26
        words.append("".join(res))

print(" ".join(words))