
N = int(input())
tab = []
for _ in range(N):
    tab.append(int(input()))

for i in range(N):
    minas = 0
    if i > 0:
        minas += tab[i-1]
    minas += tab[i]
    if i < N-1:
        minas += tab[i+1]
    print(minas)
