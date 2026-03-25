import sys

data = sys.stdin.read().split()
if not data:
    sys.exit()

n = int(data[0])
digits = ''.join(data[1:1 + n])

L = len(digits)

def add_one_str(s):
    arr = list(s)
    i = len(arr) - 1
    while i >= 0 and arr[i] == '9':
        arr[i] = '0'
        i -= 1
    if i < 0:
        return '1' + ''.join(arr)
    arr[i] = chr(ord(arr[i]) + 1)
    return ''.join(arr)

def can_parse_from(a_str):
    pos = 0
    cur = a_str
    while pos < L:
        lc = len(cur)
        if pos + lc > L or digits[pos:pos + lc] != cur:
            return False
        pos += lc
        cur = add_one_str(cur)
    return True

best = None

for first_len in range(1, L + 1):
    if digits[0] == '0':
        break
    a = digits[:first_len]
    if can_parse_from(a):
        if best is None or len(a) < len(best) or (len(a) == len(best) and a < best):
            best = a
        break

print(best)