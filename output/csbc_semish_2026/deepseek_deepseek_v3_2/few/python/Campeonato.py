import sys

data = sys.stdin.read().strip().split()
if not data:
    exit()

Cv, Ce, Cs, Fv, Fe, Fs = map(int, data)

pontos_c = Cv * 3 + Ce
pontos_f = Fv * 3 + Fe

if pontos_c > pontos_f:
    print("C")
elif pontos_f > pontos_c:
    print("F")
else:
    if Cs > Fs:
        print("C")
    elif Fs > Cs:
        print("F")
    else:
        print("=")