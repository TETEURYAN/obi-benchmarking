import sys

data = sys.stdin.read().split()
A = int(data[0])
B = int(data[1])
C = int(data[2])
H = int(data[3])
L = int(data[4])

dims = [A, B, C]
possivel = False
for i in range(3):
    for j in range(3):
        if i != j:
            altura = dims[i]
            largura = dims[j]
            if altura <= H and largura <= L:
                possivel = True
print('S' if possivel else 'N')