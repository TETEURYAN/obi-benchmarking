import sys

input_data = sys.stdin.read().split()
if not input_data:
    exit()

Cv = int(input_data[0])
Ce = int(input_data[1])
Cs = int(input_data[2])
Fv = int(input_data[3])
Fe = int(input_data[4])
Fs = int(input_data[5])

Cp = Cv * 3 + Ce
Fp = Fv * 3 + Fe

if Cp > Fp:
    print('C')
elif Fp > Cp:
    print('F')
else:
    if Cs > Fs:
        print('C')
    elif Fs > Cs:
        print('F')
    else:
        print('=')