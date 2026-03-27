import sys

data = sys.stdin.read().split()
Cv, Ce, Cs, Fv, Fe, Fs = map(int, data)

pontos_C = Cv * 3 + Ce
pontos_F = Fv * 3 + Fe

if pontos_C > pontos_F:
    print('C')
elif pontos_C < pontos_F:
    print('F')
else:
    if Cs > Fs:
        print('C')
    elif Cs < Fs:
        print('F')
    else:
        print('=')