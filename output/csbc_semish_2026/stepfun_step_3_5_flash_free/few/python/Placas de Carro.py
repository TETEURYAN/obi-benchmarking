import sys

def is_antigo(s):
    if len(s) != 8:
        return False
    if not (s[0].isalpha() and s[1].isalpha() and s[2].isalpha()):
        return False
    if s[3] != '-':
        return False
    if not (s[4].isdigit() and s[5].isdigit() and s[6].isdigit() and s[7].isdigit()):
        return False
    return True

def is_novo(s):
    if len(s) != 7:
        return False
    if not (s[0].isalpha() and s[1].isalpha() and s[2].isalpha()):
        return False
    if not s[3].isdigit():
        return False
    if not s[4].isalpha():
        return False
    if not (s[5].isdigit() and s[6].isdigit()):
        return False
    return True

placa = sys.stdin.read().strip()

if is_antigo(placa):
    print(1)
elif is_novo(placa):
    print(2)
else:
    print(0)