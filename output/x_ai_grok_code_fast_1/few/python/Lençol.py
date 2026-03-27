import sys

input = sys.stdin.read
data = input().split()
A1 = int(data[0])
B1 = int(data[1])
A2 = int(data[2])
B2 = int(data[3])
A = int(data[4])
B = int(data[5])

def max_other(p, q, x):
    if p >= x and q >= x:
        return max(p, q)
    elif p >= x:
        return q
    elif q >= x:
        return p
    else:
        return 0

poss = False
# Check for X = A
mo1 = max_other(A1, B1, A)
mo2 = max_other(A2, B2, A)
if mo1 > 0 and mo2 > 0 and mo1 + mo2 >= B:
    poss = True
# Check for X = B
mo1 = max_other(A1, B1, B)
mo2 = max_other(A2, B2, B)
if mo1 > 0 and mo2 > 0 and mo1 + mo2 >= A:
    poss = True

print('S' if poss else 'N')