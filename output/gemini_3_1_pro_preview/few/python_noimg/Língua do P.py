import sys

input_data = sys.stdin.read().rstrip('\r\n')
if input_data:
    words = input_data.split(' ')
    decoded = [word[1::2] for word in words]
    print(' '.join(decoded))