import sys

input_data = sys.stdin.read().split()
if input_data:
    s = input_data[0]
    if len(s) == 8 and s[:3].isalpha() and s[3] == '-' and s[4:].isdigit():
        print(1)
    elif len(s) == 7 and s[:3].isalpha() and s[3].isdigit() and s[4].isalpha() and s[5:].isdigit():
        print(2)
    else:
        print(0)