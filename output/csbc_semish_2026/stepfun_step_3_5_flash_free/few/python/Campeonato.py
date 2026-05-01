import sys

data = sys.stdin.read().split()
if not data:
    exit()

Cv, Ce, Cs, Fv, Fe, Fs = map(int, data)

pontosC = 3 * Cv + Ce
pontosF = 3 * Fv + Fe

if pontosC > pontosF:
    print('C')
elif pontosF > pontosC:
    print('F')
else:
    if Cs > Fs:
        print('C')
    elif Fs > Cs:
        print('F')
    else:
        print('=')