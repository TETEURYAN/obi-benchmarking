import sys

s = sys.stdin.read().strip()

def is_upper(c):
    return 'A' <= c <= 'Z'

def is_digit(c):
    return '0' <= c <= '9'

ans = 0

if len(s) == 8:
    if is_upper(s[0]) and is_upper(s[1]) and is_upper(s[2]) and s[3] == '-' and is_digit(s[4]) and is_digit(s[5]) and is_digit(s[6]) and is_digit(s[7]):
        ans = 1
elif len(s) == 7:
    if is_upper(s[0]) and is_upper(s[1]) and is_upper(s[2]) and is_digit(s[3]) and is_upper(s[4]) and is_digit(s[5]) and is_digit(s[6]):
        ans = 2

print(ans)