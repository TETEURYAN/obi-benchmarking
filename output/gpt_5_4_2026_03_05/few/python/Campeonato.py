import sys

data = list(map(int, sys.stdin.read().split()))
cv, ce, cs, fv, fe, fs = data

cp = 3 * cv + ce
fp = 3 * fv + fe

if cp > fp:
    print('C')
elif fp > cp:
    print('F')
else:
    if cs > fs:
        print('C')
    elif fs > cs:
        print('F')
    else:
        print('=')